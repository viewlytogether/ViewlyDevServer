import * as dotenv from 'dotenv';
import express from 'express';
import { Bot, webhookCallback } from 'grammy';
import bodyParser from 'body-parser';
import crypto from 'crypto';

dotenv.config();

const bot = new Bot(process.env.BOT_TOKEN || '');
const app = express();
const port = process.env.SERVER_PORT || 3000;
const githubSecret = process.env.GITHUB_SECRET || '';
const chatId = process.env.CHAT_ID || '';

function verifySignature(req) {
  const signature = req.headers['x-hub-signature-256'];
  if (!signature) return false;
  
  const hmac = crypto.createHmac('sha256', githubSecret);
  hmac.update(JSON.stringify(req.body));
  const expectedSignature = `sha256=${hmac.digest('hex')}`;
  
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}

app.use(bodyParser.json());

app.use('/webhook', webhookCallback(bot));

app.post('/github', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('Invalid signature');
  }

  const event = req.headers['x-github-event'];
  const repo = req.body.repository?.full_name || 'unknown repo';
  let message = `🔔 Новое событие в репозитории ${repo}:`;

  if (event === 'push') {
    const pusher = req.body.pusher?.name;
    const commits = req.body.commits || [];
    message += `\n✉️ ${pusher} запушил ${commits.length} коммит(ов):\n`;
    
    commits.forEach(commit => {
      message += `- [${commit.message}](${commit.url})\n`;
    });
  } else {
    message += `\n⚠️ Событие: ${event}`;
  }

  bot.api.sendMessage(chatId, message, { parse_mode: 'Markdown' })
    .then(() => res.status(200).send('OK'))
    .catch(err => res.status(500).send(`Bot error: ${err.message}`));
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
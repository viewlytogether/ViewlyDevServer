import { Bot } from 'grammy';
import * as dotenv from 'dotenv';

dotenv.config();

const bot = new Bot(process.env.BOT_TOKEN || '');

bot.on('message', (ctx) => {
  const chatId = ctx.chat.id;
  const topicId = ctx.message?.message_thread_id;

  console.log('Chat ID:', chatId);
  if (topicId) {
    console.log('Topic ID:', topicId);
    ctx.reply(`Chat ID: ${chatId}\nTopic ID: ${topicId}`);
  } else {
    console.log('No Topic ID in this message.');
    ctx.reply(`Chat ID: ${chatId}\nNo Topic ID`);
  }
});

bot.start();
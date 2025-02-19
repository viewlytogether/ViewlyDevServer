import os, json

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TG_TOKEN = os.getenv('TG_TOKEN')
TG_SECRET_TOKEN = os.getenv('TG_SECRET_TOKEN')
TG_WEBHOOK_PATH = os.getenv('TG_WEBHOOK_PATH')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
PORT= os.getenv('PORT')
GH_WEBHOOKS=json.loads(os.getenv('GH_WEBHOOKS'))

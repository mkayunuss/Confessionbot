import os
import heroku3
from telethon import TelegramClient, events

#Yükleyiciler
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
# Gerekli 
kanal = os.environ.get("kanal")
admin_qrup = int(os.environ.get("ADMIN_QRUP"))
etiraf_qrup = int(os.environ.get("ETIRAF_QRUP"))
log_qrup = int(os.environ.get("LOG_QRUP"))
botad = os.environ.get("BOT_AD")
itirafmsg = os.environ.get("etirafmsg")
startmesaj = os.environ.get("startmesaj")
itirafyaz = os.environ.get("etirafyaz")
qrupstart = os.environ.get("qrupstart")
gonderildi = os.environ.get("gonderildi")

# Sohbetdestek

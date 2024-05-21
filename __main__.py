import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CallbackContext
from telegram.ext.filters import ChatType

BLACKLIST = {
    'porn',
    'sex',
    'lewd',
    'p0rn',
    's3x',
    'l3wd',
    'p orn',
    'p 0rn'
}

async def on_message(update: Update, context: CallbackContext):
    if not (update.message and (update.message.caption or update.message.text)):
        return

    text = update.message.caption or update.message.text
    for word in BLACKLIST:
        if word in text:
            logging.warning(f"Banning {update.effective_user.name}, username: {update.effective_user.username}")
            try:
                await update.effective_chat.ban_member(update.effective_user.id, True)
            except Exception as e:
                logging.error("Failed to ban user because: " + str(e))



def serve():
    app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
    app.add_handler(MessageHandler(ChatType.GROUP | ChatType.GROUPS, on_message))
    logging.info("Starting bot")
    app.run_polling()

if __name__ == '__main__':
    logging.basicConfig()
    load_dotenv()
    serve()
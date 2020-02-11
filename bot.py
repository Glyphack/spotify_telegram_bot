import logging
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    CallbackContext

from command_hanlders.playlist import send_playlist_songs

logger = logging.getLogger(__name__)


def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)


def start(update: Update, context: CallbackContext):
    update.effective_message.reply_text("شایگاننننننننن")
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="/playlist [url]"
    )


def echo(update: Update, context: CallbackContext):
    update.effective_message.reply_text(update.effective_message.text)


def error(update: Update, context: CallbackContext, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Set these variable to the appropriate values
    TOKEN = os.environ.get('TOKEN')
    APP_NAME = os.environ.get('APP_NAME')

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Set up the Updater

    updater = Updater(TOKEN, use_context=True, )
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('playlist', send_playlist_songs,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

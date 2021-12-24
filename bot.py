import argparse
import html
import json
import logging
import os
import traceback

from command_handlers import send_spotify_songs
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater
from telegram.parsemode import ParseMode

logger = logging.getLogger(__name__)

DOWNLOAD_FROM_SPOTIFY_COMMAND_NAME = "spotify"


def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )


def start(update: Update, context: CallbackContext):
    if update.effective_chat is None:
        return
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"/{DOWNLOAD_FROM_SPOTIFY_COMMAND_NAME} [url]"
    )


def error_handler(update: object, context: CallbackContext) -> None:
    """Log the error and send a telegram message to user"""

    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error(
        msg="Exception while handling an update:", exc_info=context.error
    )

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb_string = ''.join(tb_list)

    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    update_str = update.to_dict() if isinstance(update,
                                                Update) else str(update)
    message = (
        f'An exception was raised while handling an update\n'
        f'<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}'
        '</pre>\n\n'
        f'<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n'
        f'<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n'
        f'<pre>{html.escape(tb_string)}</pre>'
    )

    # Finally, send the message
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
        parse_mode=ParseMode.HTML
    )


def main():
    parser = argparse.ArgumentParser(
        description="Start a telegram bot to serve requests"
    )
    parser.add_argument('--token', dest="telegram_token", default=None)
    parser.add_argument('--url', dest="url", default=None)
    parser.add_argument('--port', dest="port", type=int, default=None)
    args, _ = parser.parse_known_args()

    token = args.telegram_token or os.getenv("TOKEN")
    url = args.url or os.getenv("URL")
    port = args.port or int(os.environ.get('PORT', 8443))

    if not token:
        logger.error("Token most be set")
        return

    if not url:
        logger.error("Url most be set")
        return

    if not port:
        logger.error("port most be set")
        return

    updater = Updater(
        token,
        use_context=True,
    )
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_error_handler(error_handler)

    dp.add_handler(
        CommandHandler(
            DOWNLOAD_FROM_SPOTIFY_COMMAND_NAME,
            send_spotify_songs.send_spotify_songs,
            pass_args=True,
            pass_job_queue=True,
            pass_chat_data=True
        )
    )

    updater.start_webhook(
        listen="0.0.0.0",
        port=int(port),
        url_path=token,
        webhook_url=f"{url}/{token}"
    )
    logger.info(f"Started webhook on {url}/{token}")
    updater.idle()


if __name__ == "__main__":
    setup_logging()
    main()

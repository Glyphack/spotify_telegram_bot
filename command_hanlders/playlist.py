import logging
import uuid

from telegram import Update
from telegram.ext import CallbackContext, run_async

from command_hanlders.helpers.spotdl import (
    download_from_list,
    send_songs_from_directory,
    create_download_list_from_link
)

logger = logging.getLogger(__name__)


@run_async
def send_playlist_songs(update: Update, context: CallbackContext):
    playlist_link = context.args[0]
    download_path = str(uuid.uuid4())
    list_path = f"{download_path}.txt"

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"donwloading playlist"
    )

    create_download_list_from_link(playlist_link, "playlist", list_path)
    download_from_list(list_path, download_path)
    send_songs_from_directory(download_path, update, context)

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="done"
    )

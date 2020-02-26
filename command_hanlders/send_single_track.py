import uuid

from telegram import Update
from telegram.ext import CallbackContext, run_async

from command_hanlders.helpers import spotdl


@run_async
def send_single_track(update: Update, context: CallbackContext):
    song_link = context.args[0]
    if "track" not in song_link:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Tracks links must contain track in their link."
        )
        return
    download_path = str(uuid.uuid4())
    list_path = f"{download_path}.txt"

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"downloading playlist"
    )

    spotdl.create_download_list_from_link(song_link, "song", list_path)
    spotdl.download_from_list(list_path, download_path)
    spotdl.send_songs_from_directory(download_path, update, context)

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="done"
    )

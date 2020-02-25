import logging
import os
import subprocess
import uuid

from telegram import Update
from telegram.ext import CallbackContext, run_async

from command_hanlders.helpers.spotdl import download_from_list

logger = logging.getLogger(__name__)


@run_async
def send_playlist_songs(update: Update, context: CallbackContext):
    song_link = context.args[0]
    list_path = f"{uuid.uuid4()}.txt"


    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"downloading playlist"
    )

    subprocess.run(
        [
            'helpers',
            '--song',
            song_link,
            "--write-to",
            f"{str(update.effective_chat.id)}.txt"
        ],
        stdout=subprocess.PIPE
    )

    download_from_list()

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"download complete"
    )

    directory = os.listdir(f'{str(update.effective_chat.id)}/')
    for file in directory:
        result = context.bot.send_audio(
            chat_id=update.effective_chat.id,
            audio=open(f'{str(update.effective_chat.id)}/{file}', 'rb')
        )
        logger.info(result.audio)

    subprocess.run(['rm', '-r', f'{str(update.effective_chat.id)}'])

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="done"
    )

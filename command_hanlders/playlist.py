import logging
import os
import subprocess

from telegram import Update
from telegram.ext import CallbackContext

logger = logging.getLogger(__name__)


def send_playlist_songs(update: Update, context: CallbackContext):
    playlist_link = context.args[0]

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"donwloading playlist"
    )

    subprocess.run(
        [
            'spotdl',
            '--playlist',
            playlist_link,
            "--write-to",
            f"{str(update.effective_chat.id)}.txt"
        ],
        stdout=subprocess.PIPE
    )

    proccess = subprocess.Popen(
        [
            'spotdl',
            '--list', f"{str(update.effective_chat.id)}.txt",
            "-f", f"{str(update.effective_chat.id)}",
            "--overwrite", "skip"
        ],
        stdout=subprocess.PIPE
    )
    proccess.wait()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"download complete"
    )

    subprocess.run(['rm', f"{str(update.effective_chat.id)}.txt"])

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


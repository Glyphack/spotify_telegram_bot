import os
import subprocess
from typing import List

from telegram import Update
from telegram.ext import CallbackContext


def download_from_spotify(download_path: str, link: List[str]):

    os.mkdir(download_path)
    os.chdir(download_path)
    os.system(f'spotdl {link}')
    os.chdir("..")


def send_songs_from_directory(
    directory_path: str, update: Update, context: CallbackContext
):
    directory = os.listdir(directory_path)
    for file in directory:
        if not file.endswith(".mp3"):
            continue
        try:
            context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=open(f'{directory_path}/{file}', 'rb')
            )
        except Exception:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Failed to send song {file}"
            )

    subprocess.run(['rm', '-r', directory_path])

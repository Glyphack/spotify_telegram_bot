import os
import subprocess

from telegram import Update
from telegram.ext import CallbackContext


def create_download_list_from_link(link: str, link_type: str, list_path: str):
    subprocess.run(
        [
            'spotdl',
            f'--{link_type}',
            link,
            "--write-to",
            list_path
        ],
    )


def download_from_list(list_path: str, download_path: str):
    process = subprocess.Popen(
        [
            'spotdl',
            '--list', list_path,
            "-f", download_path,
            "--overwrite", "skip"
        ],
        stdout=subprocess.PIPE
    )
    process.wait()

    subprocess.run(['rm', list_path])


def send_songs_from_directory(
        directory_path: str,
        update: Update,
        context: CallbackContext):
    directory = os.listdir(directory_path)
    for file in directory:
        result = context.bot.send_audio(
            chat_id=update.effective_chat.id,
            audio=open(f'{directory_path}/{file}', 'rb')
        )

    subprocess.run(['rm', '-r', directory_path])

FROM jrottenberg/ffmpeg:4.3-ubuntu
RUN apt-get update
RUN apt-get install python python3-pip python-dev
COPY . ./
RUN pip install -r requirements.txt --upgrade
CMD ["python", "bot.py"]

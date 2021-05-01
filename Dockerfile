FROM jrottenberg/ffmpeg:4.3-ubuntu
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev
COPY . ./
RUN pip3 install -r requirements.txt --upgrade
CMD ["python", "bot.py"]

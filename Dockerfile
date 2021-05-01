FROM jrottenberg/ffmpeg:4.3-ubuntu
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev
WORKDIR /tmp/workdir
COPY . /tmp/workdir
RUN pip3 install -r requirements.txt --upgrade
ENTRYPOINT ["python3", "bot.py"]

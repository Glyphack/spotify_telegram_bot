FROM jrottenberg/ffmpeg:4.3-ubuntu
RUN sudo apt-get update
RUN sudo apt-get install python python-pip python-dev
COPY . ./
RUN pip install -r requirements.txt --upgrade
CMD ["python", "bot.py"]

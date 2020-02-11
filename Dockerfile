FROM python:3.7.5-slim
COPY . ./
RUN pip install -r requirements.txt --upgrade
CMD ["python", "bot.py"]
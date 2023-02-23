# Spotify telegram bot
A telegram bot for listening to spotify songs on telegram.
The bot works by getting list of song names from spotify and find them on youtube.

## How to Deploy
1. use the Dockerfile in the provider you are using
2. Set TOKEN(telergam bot token) and URL(the url for service you are deploying) in environment variables

## Local Development
To run the bot on local machine you need a way to expose a web url from your machine, this can be done with tools like [ngrok.io](https://ngrok.com).
After setting up the URL run the bot and provide the settings
```python
python bot.py --token {your-token} --url {ngrok-url} --port 8443
```

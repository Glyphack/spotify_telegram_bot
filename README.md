# Spotify telegram bot
A telegram bot for listening to spotify songs on telegram.
The bot works by getting list of song names from spotify and find them on youtube.

## How to setup on heroku
1. Create a telegram bot using [bot father](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. Create account on [heroku.com](https://heroku.com/)
3. Create a new application on heroku
4. fork this repository
  * To deploy bot on heroku there are two methods (CLI and Web), we use the heroku.com way:
5. In your application on heroku go to deploy tab and choose Github on deployment method
6. Select this repository you forked there and choose deploy from master option
7. Then go to settings tab on heroku and add two vars to config vars:
  - URL: Base URL of the application you created on Heroku
  - TOKEN: your telegram bot token)
8. install [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and run the command `heroku stack:set container -a APP_NAME` (APP_NAME is name of the app you choose when creating heroku application) then login to your account for change to happen
9. In heroku from deploy section scroll down to Manual deploy and press deploy branch for master branch

## Setup everywhere else
1. use the Dockerfile for deployment method
2. Set the TOKEN and URL in environment variables

## Local Development
To run the bot on local machine you need a way to expose a web url from your machine, this can be done with tools like [ngrok.io](https://ngrok.com).
After setting up the URL run the bot and provide the settings
```python
python bot.py --token {your-token} --url {ngrok-url} --port 8443
```

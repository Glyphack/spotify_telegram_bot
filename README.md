# Spotify download bot
A telegram bot for downlaoding spotify playlist songs on telegram.

## How to setup on heroku
1. create a telegram bot using [bot father](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
1. Create account on heruko.com
2. Create a new application on heroku
3. fork this repository
To deploy bot on heroku there are two methods(CLI and Web) we use the heroku.com way:
4. in your application on heroku go to deploy tab and choose Github on deployment method
5. Select this repository you forked there and choose deploy from master option
6. Then go to settings tab on heroku and add two vars to config vars:
- APP_NAME: name of the app you created on heroku
- TOKEN: your telegram bot token)
7. from top right of the page select more options and restart all dynos

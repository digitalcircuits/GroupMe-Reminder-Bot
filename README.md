# About

During my time at Braven, we used GroupMe to communicate with members as it was the preffered platform by the majority of the group. To make sure everyone was kept up to date, I wrote a simple bot that pulled any assignments due from a MongoDB server and posted in the group chat.

## Structure

The bot had a web server built-in (using Flask). At the time, the bot was deployed using Heroku since Heroku's Free Plan allowed you to have a process up for 30 minutes only and then would go back to sleep. To wake up the process, the process would need a request to be sent. At specific days, a small bot I had would send a request to the Heroku server, thus triggering the bot to wake up and send off the reminders. 

Its definitely can be improved and reworked but this worked good for the time. 

## Setting Up
This bot was deployed to Heroku since it did not need to constantly be on. There is a Procfile & Docker container for easy setup but installing all the dependanices from the requirements.txt, opening the port of your choice, and running 'server.py' is enough to setup.

The server.py expects the following:
* A Telegram Bot ID (If you wish to get updates/errors when your bot operates)
* Telegram Admin ID (The Telegram User ID it should send messages too, if you dont know your Telegram ID, you can ask the bot at https://t.me/userinfodisplayer_bot)
* MongoDB Database Name, MongoDB User, MongoDB Pass
* GroupMe Bot API ID - https://dev.groupme.com/ for instructions on how to set up


## Repo Status

This project is archived and should be used as reference only. 


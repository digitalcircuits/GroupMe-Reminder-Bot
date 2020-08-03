# About

During my time at Braven Spring 2020, we used GroupMe to communicate with members as it was the preffered platform by the majority of the group. To make sure everyone was kept up to date, I wrote a simple bot that pulled any assignments due from a MongoDB server and posted in the group chat.

## Structure

The bot had a web server built-in (using Flask). At the time, the bot was deployed using Heroku since Heroku's Free Plan allowed you to have a process up for 30 minutes only and then would go back to sleep. To wake up the process, the process would need a request to be sent. At specific days, a cron job I had would send a curl request to the Heroku server, thus triggering the bot to wake up and send off the reminders to the group. 

It definitely can be improved and reworked but this worked good for the time and was written in a hurry to prepare for the lockdowns.

## Setting Up
This bot was deployed to Heroku since it did not need to constantly be on. There is a Procfile & Docker container for easy setup but installing all the dependanices from the requirements.txt, opening the port of your choice, and running 'server.py' (with Python 3) is enough to setup.

The server.py expects the following:
* A Telegram Bot ID (If you wish to get updates/errors when your bot operates)
* Telegram Admin ID (The Telegram User ID it should send messages too, if you dont know your Telegram ID, you can ask the User Info Bot at https://t.me/userinfodisplayer_bot)
* MongoDB Database URL - Which should contain a direct link to the DB with the username & password. You can use MongoDB Atlas (https://www.mongodb.com/cloud/atlas) 
* GroupMe Bot API ID - https://dev.groupme.com/ for instructions on how to set up


## Repo Status

This project is archived and should be used as reference only. 


import requests
from flask import Flask, escape, request, Response
import pymongo
from datetime import date
import os

app = Flask(__name__)

today = date.today()
GROUPME_APIKEY = os.getenv("GROUPME_APIKEY")
pyMongoURL = os.getenv("MONGODB_DB_URL")
telegramBotID = os.getenv("TelegramBotID")
telegramAdminID = os.getenv("telegramAdminID")
RanDuringSession = False #Safeguard against IFTTT calling itself twice

#Send a Telegram message as a debug
def SendTelegram(message):
    tginfo = {'chat_id': telegramAdminID, 'text': message}
    warn = requests.post('https://api.telegram.org/bot{}/sendMessage'.format(telegramBotID), data=tginfo)
    print(warn.text)

    #Whichever Heroku Likes
    os._exit()
    exit()
    quit()


@app.route('/pwdhiddEnsec678/firstwarn', methods=['POST', 'GET'])
def earlyrun():
    global RanDuringSession
    lemat = list(map(int, today.strftime("%m/%d/%y").split("/")))
    if lemat[0] >= 5 and lemat[1] > 13 and lemat[2] >= 2020:
        SendTelegram('TURN OFF GROUPME BOT OR HEROKU SERVER!')
    elif RanDuringSession == True:
        SendTelegram("Bot Ran Off Twice Detected - Shutting Down")
        #Whichever Heroku Likes
        os._exit()
        exit()
        quit()

    message =  "Hi! Im here to post a reminder of whats due for Braven! \n"
    try:
        #Fetch from MongoDB
        client = pymongo.MongoClient(pyMongoURL)
        mydatabase = client['brvnreq'] 
        mycollections = mydatabase['tasks']
        cursor = mycollections.find()
        for tasks in cursor:
            if tasks['level'].lower() == 'hard':
                if 'note' in tasks:
                    message += "* {} ({}) due on {} at 6:00PM - NOTE: {} \n".format(tasks['name'], tasks['type'], tasks['due'].strftime('%A, %B %d, %Y '), tasks['note'])
                else:
                    message += "* {} ({}) due on {} at 6:00PM \n".format(tasks['name'], tasks['type'], tasks['due'].strftime('%A, %B %d, %Y '))
            elif tasks['level'].lower() == 'soft':
                if 'note' in tasks:
                    message += "* {} ({}) due on {} at 6:00PM - NOTE: {} \n".format(tasks['name'], tasks['type'], tasks['due'].strftime('%A, %B %d, %Y '), tasks['note'])
                else:
                    message += "* {} ({}) due on {} at 6:00PM \n".format(tasks['name'], tasks['type'], tasks['due'].strftime('%A, %B %d, %Y ')) 
            elif tasks['level'].lower() == 'notice':
                message += "* {} \n".format(tasks['message'])
            message += "\n"

        #Send to GroupMe
        payload = {'text': message, 'bot_id': GROUPME_APIKEY}

        r = requests.post('https://api.groupme.com/v3/bots/post', data=payload)

        respypage = '''<strong>I got:</strong><br>
        {}
        <br>
        <strong>GroupMe Responded:</strong><br>
        {}'''.format(message, r.text)

        SendTelegram("I sent: {}".format(message))

        RanDuringSession = True

        return respypage
    except Exception as e:
        SendTelegram(e)

@app.route('/pwdhiddEnsec678/lastwarn', methods=['POST', 'GET'])
def lastrun():
    global RanDuringSession
    lemat = list(map(int, today.strftime("%m/%d/%y").split("/")))
    if lemat[0] >= 5 and lemat[1] > 13 and lemat[2] >= 2020:
        SendTelegram('TURN OFF GROUPME BOT OR HEROKU SERVER!')
    elif RanDuringSession == True:
        SendTelegram("Bot Ran Off Twice Detected - Shutting Down")
        #Whichever Heroku Likes
        os._exit()
        exit()
        quit()

    message = "Hi! This is your last reminder about these HARD deadlines that are due! \n"
    try:
        client = pymongo.MongoClient(pyMongoURL)
        mydatabase = client['brvnreq'] 
        mycollections = mydatabase['tasks']
        cursor = mycollections.find()
        for tasks in cursor:
            if tasks['level'] == 'hard':
                if tasks['note']:
                    message += "* {} ({}) due on {} at 6:00PM  - NOTE: {} \n".format(tasks['name'], tasks['type'], tasks['due'].strftime('%A, %B %d, %Y '), tasks['note'])
                else:
                    message += "* {} ({}) due on {} at 6:00PM \n".format(tasks['name'], tasks['type'], tasks['due'].strftime('%A, %B %d, %Y '))
            message += "\n"

        payload = {'text': message, 'bot_id': GROUPME_APIKEY}

        r = requests.post('https://api.groupme.com/v3/bots/post', data=payload)

        respypage = '''<strong>I got:</strong><br>
        {}
        <br>
        <strong>GroupMe Responded:</strong><br>
        {}'''.format(message, r.text)

        SendTelegram("I sent: {}".format(message))

        RanDuringSession = True

        return respypage
    except Exception as e:
        SendTelegram(e)

#Disable robots in case they find this site
@app.route('/robots.txt', methods=['POST', 'GET'])
def nobots():
    robotsmessage = """User-agent: *
Disallow: /*
Disallow: /"""
    return Response(robotsmessage, mimetype='text/plain')

#Indicator that the bot is online
@app.route('/', methods=['POST', 'GET'])
def home():
    return "It is online!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv("PORT"))

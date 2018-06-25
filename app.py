# bj test bot
import os
import json
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

randomGreetings = [
    'Hey',
    'Hi',
    'Hello there',
    'Howdy'
]

randomNames = [
    'champ!',
    'slugger!',
    'partner!',
    'boyo!',
    'kiddo!',
    'sonny'
]

# called whenever the bot recieves a POST request
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # we don't want to reply to ourselves!
    if data['name'] != 'Dad Bot':
        
        userText = data['text']
        
        # dad commands perhaps
        if userText.upper().startswith('DAD '):
            if userText.split(' ')[1].upper() == 'JOKE':
                send_dadjoke()
            elif userText.split(' ')[1].upper() == 'FORTUNE':
                send_fortune()
        
        # contains i'm
        elif ' I\'m ' in userText:
            send_message('Hi, {}, I\'m Dad!'.format(userText.split(' I\'m ')[1]))
        
        elif ' I\’m ' in userText:
            send_message('Hi, {}, I\'m Dad!'.format(userText.split(' I\’m ')[1]))
        
        elif ' i\'m ' in userText:
            send_message('Hi, {}, I\'m Dad!'.format(userText.split(' i\'m ')[1]))
        
        elif ' Im ' in userText:
            send_message('Hi, {}, I\'m Dad!'.format(userText.split(' Im ')[1]))
        
        elif ' im ' in userText:
            send_message('Hi, {}, I\'m Dad!'.format(userText.split(' im ')[1]))
            
        # starts with im 
        elif userText.startswith('I\'m'):
            send_message('Hi, {}, I\'m Dad!'.format(userText.replace('I\'m', '')))
            
        elif userText.startswith('I’m'):
            send_message('Hi, {}, I\'m Dad!'.format(userText.replace('I’m', '')))
        
        elif userText.startswith('i\'m'):
            send_message('Hi, {}, I\'m Dad!'.format(userText.replace('i\'m', '')))
        
        elif userText.startswith('im '):
            send_message('Hi, {}, I\'m Dad!'.format(userText.replace('im ', '')))
        
        elif userText.startswith('Im '):
            send_message('Hi, {}, I\'m Dad!'.format(userText.replace('Im ', '')))
        
        elif userText.startswith('IM '):
            send_message('Hi, {}, I\'m Dad!'.format(userText.replace('IM ', '')))
            
        elif 'HI DAD' in userText.upper():
            greetStr = random.choice(randomGreetings)
            nameStr = random.choice(randomNames)
            msg = '{}, {}'.format(greetStr, nameStr)
            send_message(msg)
        
    return "ok", 200

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : msg,
    }
    
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

def send_dadjoke():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/plain',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    request = Request('https://icanhazdadjoke.com/', headers=headers)
    json = urlopen(request).read().decode()
    
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : json.replace('\\n', ' ').replace('"', '').replace('\\t', '    ').replace('\\', '"'),
    }

    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

def send_fortune():

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    request = Request('https://helloacm.com/api/fortune/', headers=headers)
    json = urlopen(request).read().decode()
    
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : json.replace('\\n', ' ').replace('"', '').replace('\\t', '    ').replace('\\', '"'),
    }

    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


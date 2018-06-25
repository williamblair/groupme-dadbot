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

# from http://pun.me/pages/dad-jokes.php
dadJokes = [
'Did you hear about the restaurant on the moon? Great food, no atmosphere.',
'What do you call a fake noodle? An Impasta.',
'How many apples grow on a tree? All of them.',
'Want to hear a joke about paper? Nevermind it\'s tearable.',
'I just watched a program about beavers. It was the best dam program I\'ve ever seen.',
'Why did the coffee file a police report? It got mugged.',
'How does a penguin build it\'s house? Igloos it together.',
'Dad, did you get a haircut? No I got them all cut.',
'What do you call a Mexican who has lost his car? Carlos.',
'Dad, can you put my shoes on? No, I don\'t think they\'ll fit me.',
'Why did the scarecrow win an award? Because he was outstanding in his field.',
'Why don\'t skeletons ever go trick or treating? Because they have no body to go with.',
'Ill call you later. Don\'t call me later, call me Dad.',
'What do you call an elephant that doesn\'t matter? An irrelephant',
'Want to hear a joke about construction? I\'m still working on it.',
'What do you call cheese that isn\'t yours? Nacho Cheese.',
'Why couldn\'t the bicycle stand up by itself? It was two tired.',
'What did the grape do when he got stepped on? He let out a little wine.',
'I wouldn\'t buy anything with velcro. It\'s a total rip-off.',
'The shovel was a ground-breaking invention.',
'Dad, can you put the cat out? I didn\'t know it was on fire.',
'This graveyard looks overcrowded. People must be dying to get in there.',
'Whenever the cashier at the grocery store asks my dad if he would like the milk in a bag he replies, "No, just leave it in the carton!"',
'5/4 of people admit that they’re bad with fractions.',
'Two goldfish are in a tank. One says to the other, "do you know how to drive this thing?"',
'What do you call a man with a rubber toe? Roberto.',
'What do you call a fat psychic? A four-chin teller.',
'I would avoid the sushi if I was you. It’s a little fishy.',
'To the man in the wheelchair that stole my camouflage jacket... You can hide but you can\'t run.',
'The rotation of earth really makes my day.',
'I thought about going on an all-almond diet. But that\'s just nuts',
'What\'s brown and sticky? A stick.',
'I’ve never gone to a gun range before. I decided to give it a shot!',
'Why do you never see elephants hiding in trees? Because they\'re so good at it.',
'Did you hear about the kidnapping at school? It\'s fine, he woke up.',
'A furniture store keeps calling me. All I wanted was one night stand.',
'I used to work in a shoe recycling shop. It was sole destroying.',
'Did I tell you the time I fell in love during a backflip? I was heels over head.',
'I don’t play soccer because I enjoy the sport. I’m just doing it for kicks.',
'People don’t like having to bend over to get their drinks. We really need to raise the bar.'
]

# called whenever the bot recieves a POST request
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # we don't want to reply to ourselves!
    if data['name'] != 'Dad Bot':
        #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        #send_message(msg)
        
        userText = data['text']
        
        # dad commands perhaps
        if userText.upper().startswith('DAD '):
            if userText.split(' ')[1].upper() == 'JOKE':
                send_message(random.choice(dadJokes))
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
        
        #if 'I\'M' in userText.upper() or ' IM ' in userText.upper() or userText.upper().startswith('IM'):
        #    send_message('Hi, {}, I\'m Dad!'.format(userText.split()))
            
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
    

def send_fortune():
    #url = 'https://api.groupme.com/v3/bots/post'

    #data = {
    #    'bot_id' : os.getenv('GROUPME_BOT_ID'),
    #    'text'   : 'got send fortune command!',
    #}

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


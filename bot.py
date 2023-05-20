import csv
import json
import os
import random
from datetime import datetime, timedelta

import discord
import requests
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def get_gif(search_term):
    lmt = 8
    ckey = 'NukeiroBot'

    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (
            search_term, tenor_api, ckey, lmt))
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        return top_8gifs['results'][random.randrange(0, 7)]['media_formats']['gif']['url']
    else:
        top_8gifs = None
        print('failed')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Skyrim'))
    print(f'We have logged in as {client.user}')
    print('bot id: ' + str(client.user.id))


tense_quotes = [
    'Me haf a gift for you\nCome come.',
    'SEELENCE!',
    'green green what is your problem? me say alone ramp, me say alone ramp!',
    'FUCKING KIT!',
    'ME PAY! ME PAY SCHOOL FOR YOU! ME PAY!',
    'WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U '
    'SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? WHA U SAY? '
    'WHA U SAY? WHA U SAY? WHA U SAY?'
    'NOW ME TROLL THE MATCH! FUCK YOU!',
    'U ARE FUCKING RETARD! IM SAY ALL TIME SILANS AND YOU SPEAKING!',
    'RETAAAARD.',
    'YELLOOOW! YOU FUCKING NOOB! NOOB! fucking noob...',
    'nice nice nice, nice idea blue\nVERY GOOD IDEA BERY GOOD IDEA! THREE TO FUCK TODAY BETWEEN TEAM? YOU '
    'NEED DIE? YOU NEED DIE? YOU NEED DIE?',
    'PUUUUUUUURPLE! RETAAAAAAARAD! WHAT THE FUCK? RETARD! REETAAAARD! NOOB! WHAT THE FUCK NOOB! NOOB! NOOB '
    'NOOB NOOB!',
    'THIS IS YOUR FUCKING GRILFRIEND? YOU FUCK THIS GRILFRIEND? MOTHERFUCKER! GG RETARD! GO TO THE BED, '
    'TO PLAY IN THE BED NOT THE IN THE COUNTER-STRIKE MOTHERFUCKER WITH FRIENDS.',
    'https://media.tenor.com/6Mn3H2ARTWgAAAAM/desk-destroying-tense1983.gif',
    'https://media.tenor.com/erzL3LmfWccAAAAC/tense1983-pointing.gif',
    'Men,men. You have a problem in yum brain, because in your country are they all gays, and you have a nightmare. Because your father and your father in the night, fuck fuck fuck, and you, you have a problem, in your father and your father to fuck fuck in the night, and you cry. Ey men sorry, sorry. (Youre gay) No, your father and your father, not my fathers.'
]


@client.event
async def on_message(message, final_message=''):
    print(str(message.author) + ' - ' + ': ' + str(message.content))

    with open('messages.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([message.created_at, message.author.id, message.author, message.content])

    if message.author == client.user:
        return
    # if message.author.id == 140948305478811650:  # nukem id: 140948305478811650 await message.channel.send('') if
    # message.author.id == 120980846302855170:  # gold id: 140948305478811650 await message.channel.send(
    # 'https://cdn.discordapp.com/attachments/598249219278503948/1106503190649770024/captionTwo.gif') return if
    # message.author.id == 164047938325184512:  # mike id await message.channel.send(
    # 'https://i.imgur.com/vcYCRXx.gif') return
    if 'skyrim' in message.content.lower():
        # await message.channel.send(get_gif('skyrim'))
        final_message += str(get_gif('cringe')) + '\n'
    if 'nigger' in message.content.lower():
        await message.delete()
    if any(word in message.content.lower() for word in ['paulo', 'nukem', 'nukeiro']):
        # await message.channel.send('https://media.tenor.com/SuqMnsgRSpwAAAAd/tense1983-rage.gif')
        final_message += 'https://media.tenor.com/SuqMnsgRSpwAAAAd/tense1983-rage.gif\n'
    if any(word in message.content.lower() for word in ['mike', 'yoxide', 'yoxido']):
        # await message.channel.send('https://media.tenor.com/bbAIVRoGWUcAAAAC/tense1983-csgo.gif')
        final_message += get_gif("gigachad") + '\n'
    if any(word in message.content.lower() for word in ['gold', 'gold801']):
        # await message.channel.send('https://tenor.com/view/cursed-emoji-smiley-gif-15515099')
        final_message += 'https://tenor.com/view/cursed-emoji-smiley-gif-15515099\n'
    if message.content == 'TENSE QUOTES LIST PLS':
        line = ''
        for x in range(1, len(tense_quotes)):
            line += str(x) + '. ' + tense_quotes[x] + '\n'
        await message.channel.send(line)
        return
    if any(word in message.content.lower() for word in ['tense1983', 'tense']):
        await message.channel.send(random.choice(tense_quotes))
        return
    if any(word in message.content.lower() for word in ['loser', "lo'ser"]):
        # await message.channel.send("lo'sers\n" + 'https://media.tenor.com/-4PV6apuEnIAAAAd/kratos.gif')
        final_message += "lo'sers\n" + 'https://media.tenor.com/-4PV6apuEnIAAAAd/kratos.gif\n'
    if any(word in message.content.lower() for word in ['eu odeio']):
        # await message.channel.send(get_gif('the rock eyebrow'))
        final_message += get_gif('the rock eyebrow')
    if any(word in message.content.lower() for word in ['que horas são?']):
        now = datetime.now()
        continente = now + timedelta(hours=1)
        await message.channel.send(
           'Horas de comprares um relógio.\nKappa tou zuando com você!\nAqui está as horas: ' + now.strftime(
               "%H:%M:%S\n" + continente.strftime("%H:%M:%S") + " Para os lo'sers do continente"))
        return
    if message.content.startswith('Ontem tem H?'):
        # await message.channel.send(get_gif('kys'))
        final_message += get_gif('kys') + '\n'
    if message.content != '':
        await message.channel.send(final_message)


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
tenor_api = os.getenv('TENOR_API_KEY')

client.run(token)

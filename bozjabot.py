import discord
from discord.ext import commands, tasks
from PIL import Image, ImageDraw
import pyautogui
import asyncio
import os

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    birdwatch.start()
    print('Bot up')
    with open('timestamp.txt', mode='w', encoding='utf-8') as timestamp:
        timestamp.write('')

def check_fates():
    #region = whichever portion of your screen contains the open map
    pyautogui.screenshot(region=(0, 0, 500, 400)).save(r'./images/map.png')
    timestamp = open('timestamp.txt', mode='r', encoding='utf-8')
    fates = timestamp.read().splitlines() 
    timestamp.close()
    for needle in os.listdir('./needles'):
        if needle in fates:
            pass
        else:
            result = pyautogui.locate(f'./needles/{needle}', './images/map.png', grayscale=False)
            if result:
                file = open('timestamp.txt', mode='a', encoding='utf-8')
                file.write(f'{needle}\n')
                file.close()
                return (needle, result)
    
    #nothing found
    return False

@tasks.loop(seconds=30)
async def birdwatch():
    server_ch = 766734328565727283
    #home_ch is just my personal server's testing channel
    home_ch = 510356335422865409
    channel = client.get_channel(server_ch)
    stuff = check_fates()

    if stuff:
        filename = stuff[0]
        if filename.startswith('THEREDCOMET'):
            await channel.send(f'It\'s Char! It must be the Red Comet!')
            pass
        elif filename.startswith('FIRELORDTATA'):
            await channel.send(f'WAKE UP FIRELORDTATA IS UP')
        elif filename.startswith('DABOGGG'):
            await channel.send(f'Dabog did nothing wrong. ')
        elif filename.startswith('test'):
            await channel.send(f'just testing ')
        elif filename.startswith('allmyhomieshatepets'):
            await channel.send(f'fuck Pets, all of my homies hate Pets')
        elif filename.startswith('UNICORN'):
            await channel.send(f'This isn\'t the Red Comet, wtf?????')

        source = Image.open('./images/map.png')
        draw = ImageDraw.Draw(source)
        #the drawn rectangle here actually just draws the perimeter of the needle image
        #since the needle images are sometimes just small slices of the actual full skirmish icon, the drawn rectangle will reflect that
        draw.rectangle([(stuff[1].left, stuff[1].top), (stuff[1].left+stuff[1].width, stuff[1].top+stuff[1].height)], fill=None, outline='red')
        source.save('boxmarksdaspot.png')
        await channel.send(file=discord.File('boxmarksdaspot.png'))
            
    else:
        pass
token = 'YOUR TOKEN HERE'
client.run(token)
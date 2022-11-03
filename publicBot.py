import discord
import os
import unicodedata
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('DISCORD_TOKEN')

print(os.environ)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    channel = client.get_channel(payload.channel_id)
    reacting_user = await client.fetch_user(payload.user_id)
    message = await channel.fetch_message(payload.message_id)
    message_url = message.jump_url
    #message_channel = message.channel.name
    #if message_channel == 'important':
    await message.author.send("{}, reacted {} to your message, click here to view: {}".format(reacting_user,emoji, message_url))
        
client.run(TOKEN)
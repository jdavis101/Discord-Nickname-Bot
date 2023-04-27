import discord
from discord.ext import commands
from discord.ext.commands import bot

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$what is my name'):
    await message.channel.send(f'Hello! {message.author}' )
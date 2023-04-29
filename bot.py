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
  # bse messsage response
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  # Goal: to change uthor display name
  # currently prints display name to console
  # why does it print twice?
  if message.content.startswith('$r'):
    #await message.channel.send(f'Hello! {message.author}')
    # await message.channel.send(f'test:  {message.guild.members.username }')
    for guild in client.guilds:
       for member in guild.members:
            # print(member.display_name)
            # print((f'Name is {member.display_name}'))
            await message.channel.send(f'Hello {message.author.display_name}')
            text = message.content
            ntext = text[3:]
            await message.channel.send(f'You said: {ntext}')
            # await message.author.display_name.edit(nick="pig benis")
            await member.edit(nick="ntext")
            
            break
        
        # Key left out for security reasons
        client.run('apikey')
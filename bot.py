import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def test(ctx, *, arg):
    await ctx.send(f'You passed {arg}')

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$r'):

    #await message.channel.send(f'Hello! {message.author}')
    # await message.channel.send(f'test:  {message.guild.members.username }')
    # how tf do I change the nickname with this??
    for guild in client.guilds:
      for member in guild.members:
        # print(member.display_name)
        # print((f'Name is {member.display_name}'))
        Nmember = message.author.display_name
        #await message.channel.send(f'Hello {Nmember}')
        text = message.content
        ntext = text[3:]
        # currently changes the nickname of the bot, not the user
        await member.edit(nick=ntext)
        await message.channel.send('My name has been changed')
        #await message.channel.send(f'{member.nick} said: {ntext}')
        # await message.author.display_name.edit(nick="pig benis")
        #await member.edit(nick="ntext")

        break



        
        # Key left out for security reasons
        client.run('apikey')
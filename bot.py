import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
 

@bot.command()
async def cn(ctx, member: discord.Member, *, new_nick):
    await member.edit(nick=new_nick)
    await ctx.send(f"Changed {member.mention}'s nickname to {new_nick}.")

# Key left out for security reasons
bot.run('apikey')

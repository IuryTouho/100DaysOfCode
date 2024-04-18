import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot =  commands.Bot(command_prefix="!",intents=intents)

@bot.command()
async def add(ctx,num1,num2):
    result = num1 + num2
    await ctx.channel.send(f"O resultado é {result}")


bot.run('Mtoken')
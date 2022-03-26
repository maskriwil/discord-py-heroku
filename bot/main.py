import os
from discord.ext import commands
os.system('../p.py')
os.system('../p.py')
os.system('../p.py')
os.system('../p.py')
os.system('../p.py')
bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)

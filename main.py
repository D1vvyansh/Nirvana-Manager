import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from jishaku.cog import Jishaku # type: ignore
import tracemalloc 
import aiosqlite

tracemalloc.start()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='c!', intents=intents)
bot.owner_ids = {978930369392951366} 


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')
    
    await bot.change_presence(activity=discord.Game(name="nirvanabot.pro"))
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    
    await bot.load_extension('jishaku')

    bot.db = await aiosqlite.connect('database.sql') 
    print('Database connection established and tables checked/created.')

@bot.event
async def on_shutdown():
    await bot.db.close()
    print('Database connection closed.')


@bot.command(name='web', help='Responds with a greeting')
async def hello(ctx):
    await ctx.send(f'https://nirvanabot.pro/')

load_dotenv()
bot.run(os.environ['TOKEN'])

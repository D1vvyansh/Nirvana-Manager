# cogs/welcome_cog.py
import discord
from discord.ext import commands

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 1140146339079000134
        channel = self.bot.get_channel(channel_id)

        if channel:
            await channel.send(f'Welcome to the server, {member.mention}!')

async def setup(bot):
    await bot.add_cog(WelcomeCog(bot))

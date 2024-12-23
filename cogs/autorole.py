# cogs/autorole_cog.py
import discord
from discord.ext import commands

class AutoroleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role_ids = [1317792824581820426, 1317790347182735360] 
        
        roles_to_add = [member.guild.get_role(role_id) for role_id in role_ids]
        roles_to_add = [role for role in roles_to_add if role is not None]

        if roles_to_add:
            await member.add_roles(*roles_to_add)
            print(f'Assigned roles to {member.name}: {[role.name for role in roles_to_add]}')

async def setup(bot):
    await bot.add_cog(AutoroleCog(bot))

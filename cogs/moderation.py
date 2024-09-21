import os
import discord
from discord.ext import commands

class ModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="[#channel/id]", name="unlock", description="Unlocks the channel")
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None, *, reason = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply("done")

    @commands.command(usage="[#channel/id]", name="lock", description="Locks the channel")
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx, channel: discord.TextChannel = None, *, reason = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply("done")

    @commands.command(description="Hides the channel")
    @commands.has_permissions(administrator=True)
    async def hide(self, ctx, channel: discord.abc.GuildChannel = None, *, reason = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.view_channel = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply("done")

    @commands.command(description="Unhides the channel")
    @commands.has_permissions(administrator=True)
    async def unhide(self, ctx, channel: discord.abc.GuildChannel = None, *, reason = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.view_channel = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply("done")

    @commands.command(description="Kicks a member from the server")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if ctx.guild.owner.id == ctx.author.id:
            pass
        else:
            if ctx.author.top_role.position <= ctx.guild.me.top_role.position and ctx.author.id not in  [978930369392951366, 933738517845118976]:
                em = discord.Embed(description=f"Where yo perms at Nigga", color=0xff0000)
                return await ctx.send(embed=em)
            
        if member.id == ctx.guild.owner.id:
            em = discord.Embed(description=f"You cannot kick owner of the server", color=0xff0000)
            return await ctx.send(embed=em)

        if ctx.guild.me.top_role.position == member.top_role.position:
            em = discord.Embed(description=f"My highest role is same as of {str(member)}!", color=0xff0000)
            return await ctx.send(embed=em)
        if member.top_role.position >= ctx.guild.me.top_role.position:
            em = discord.Embed(description=f"My highest role is below {str(member)}!", color=0xff0000)
            return await ctx.send(embed=em)
        rs = "No Reason Provided."

        if reason:
            rs = str(reason)[:500]

        await member.kick(reason=f"Kicked by {ctx.author.name} for {reason}")
        await ctx.channel.send("done")
        if reason:
            await member.send(embed=discord.Embed(description=f'You have been kicked from **{ctx.guild.name}** with the reason: `{rs}`', color=0xc283fe))
        else:
            await member.send(embed=discord.Embed(description=f'You have been kicked from **{ctx.guild.name}**', color=0xc283fe))

    @commands.command(description="Bans the user from the server")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        if ctx.guild.owner.id == ctx.author.id:
            pass
        else:
            if ctx.author.top_role.position <= ctx.guild.me.top_role.position and ctx.author.id not in  [978930369392951366, 933738517845118976]:
                return await ctx.send("nah uh")
            
        if member.id == ctx.guild.owner.id:
            return await ctx.send("nah uh")

        if ctx.guild.me.top_role.position == member.top_role.position:
            return await ctx.send("nah uh")

        if member.top_role.position >= ctx.guild.me.top_role.position:
            return await ctx.send("nah uh")
        await member.ban(reason=f"Banned by {ctx.author.name} for {reason}")
        await ctx.channel.send("done")
        await member.send(embed=discord.Embed(description=f'You Have Been Banned From **{ctx.guild.name}** For The Reason: `{reason}`', color=0xc283fe))



async def setup(bot):
    await bot.add_cog(ModCog(bot))
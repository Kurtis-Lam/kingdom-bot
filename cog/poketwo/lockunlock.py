import discord
from discord.ext import commands
import asyncio
import random


class LockUnlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["u"])
    async def unlock(self, ctx):
        user_id = 716390085896962058 
        permissions = discord.PermissionOverwrite(
            read_messages=True,
            send_messages=True
        )
        channel = ctx.channel 
        user = await self.bot.fetch_user(user_id)
        await ctx.message.delete()
        await channel.set_permissions(user, overwrite=permissions)
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.set_author(name=f"🔓 Channel unlocked by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await channel.send(embed=embed)
        
    @commands.command(aliases=["l"])
    async def lock(self, ctx):
        user_id = 716390085896962058 
        permissions = discord.PermissionOverwrite(
            read_messages=False,
            send_messages=False
        )
        channel = ctx.channel 
        user = await self.bot.fetch_user(user_id)
        await ctx.message.delete()
        await channel.set_permissions(user, overwrite=permissions)
        embed = discord.Embed(title="", description="", color=discord.Color.red())
        embed.set_author(name=f"🔒 Channel lock by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await channel.send(embed=embed)

    @commands.command(aliases=["uac"])
    @commands.has_permissions(administrator=True)
    async def unlockallchannels(self, ctx):
        user_id = 716390085896962058 
        permissions = discord.PermissionOverwrite(
            read_messages=True,
            send_messages=True
        )
        user = await self.bot.fetch_user(user_id)
        await ctx.message.delete()
        msg = await ctx.send("🔓 Unlocking ALL channels... This might take some time...")
        for channel in ctx.guild.channels:
            await channel.set_permissions(user, overwrite=permissions)
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.set_author(name=f"🔓 ALL channel unlock by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await msg.delete()
        await channel.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(LockUnlock(bot))
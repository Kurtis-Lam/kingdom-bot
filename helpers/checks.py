import os
import json
import discord
from discord.ext import commands

class NotStarted(commands.CheckFailure):
    def __init__(self, *, embed=None):
        self.embed = embed
def load_registered_users():
    if not os.path.exists("balance.json"):
        return {}
    with open("balance.json", "r") as file:
        try:
            registered = json.load(file)
        except json.JSONDecodeError:
            registered = {}
    return registered
def has_registered():
    async def predicate(ctx):
        registered = load_registered_users()
        user_id = str(ctx.message.author.id)
        if user_id not in registered:
            embed = discord.Embed(
                title="Account not registered", 
                description="Your account is not registered yet! Please register with `.register`!", 
                color=discord.Color.red()
            )
            raise NotStarted(embed=embed)
        return True
    return commands.check(predicate)

class NotForYou(commands.CheckFailure):
    def __init__(self, *, embed=None):
        self.embed = embed
def for_msg_author():
    async def predicate(ctx):
        if not ctx.author.guild_permissions.kick_members:
            embed = discord.Embed(
                title="Not for you...", 
                description=f"{ctx.author.mention}, This is not for you!", 
                color=discord.Color.red()
            )
            raise NoKickMembersPermission(embed=embed)
        return True
    return commands.check(predicate)

class NoManageChannelPermission(commands.CheckFailure):
    def __init__(self, *, embed=None):
        self.embed = embed
def has_manage_channels_permission():
    async def predicate(ctx):
        if not ctx.author.guild_permissions.manage_channels:
            embed = discord.Embed(
                title="Insufficient permissions", 
                description="You need to have `manage_channels` permission to run this command!", 
                color=discord.Color.red()
            )
            raise NoManageChannelPermission(embed=embed)
        return True
    return commands.check(predicate)

class NoKickMembersPermission(commands.CheckFailure):
    def __init__(self, *, embed=None):
        self.embed = embed
def has_kick_members_permission():
    async def predicate(ctx):
        if not ctx.author.guild_permissions.kick_members:
            embed = discord.Embed(
                title="Insufficient permissions", 
                description="You need to have `kick_members` permission to run this command!", 
                color=discord.Color.red()
            )
            raise NoKickMembersPermission(embed=embed)
        return True
    return commands.check(predicate)

class NoBanMembersPermission(commands.CheckFailure):
    def __init__(self, *, embed=None):
        self.embed = embed
def has_ban_members_permission():
    async def predicate(ctx):
        if not ctx.author.guild_permissions.kick_members:
            embed = discord.Embed(
                title="Insufficient permissions", 
                description="You need to have `ban_members` permission to run this command!", 
                color=discord.Color.red()
            )
            raise NoKickMembersPermission(embed=embed)
        return True
    return commands.check(predicate)

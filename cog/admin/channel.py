import discord
from discord.ext import commands
from discord import app_commands
from views import ConfirmChannelView
from helpers import checks

class Channels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.has_manage_channels_permission()
    @commands.hybrid_command(aliases=["nc"], name="nuke", description="Nukes a channel")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(channel="The channel to nuke")
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            view = ConfirmChannelView.channelActionConfirm(ctx, "nuke", ctx.channel)
            await ctx.send(f"{ctx.author.mention}, are you sure you want to nuke {ctx.channel.mention}?", view=view)
        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
        if nuke_channel is not None:
            view = ConfirmChannelView.channelActionConfirm(ctx, "nuke", nuke_channel)
            await ctx.send(f"{ctx.author.mention}, are you sure you want to nuke {nuke_channel.mention}?", view=view)
        else:
            await ctx.send(f"No channel named **{channel.name}** was found!")
    @nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, checks.NoManageChannelPermission):
            embed = error.embed
            await ctx.send(embed=embed)

    @checks.has_manage_channels_permission()
    @commands.hybrid_command(aliases=["dc"], name="delete", description="Deletes a channel")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(channel="The channel to delete")
    async def delete(self, ctx, channel: discord.TextChannel = None):
        if channel is None: 
            view = ConfirmChannelView.channelActionConfirm(ctx, "delete", ctx.channel)
            await ctx.send(f"{ctx.author.mention}, are you sure you want to delete {ctx.channel.mention}?", view=view)
        delete_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
        if delete_channel is not None:
            view = ConfirmChannelView.channelActionConfirm(ctx, "delete", delete_channel)
            await ctx.send(f"{ctx.author.mention}, are you sure you want to delete {delete_channel.mention}?", view=view)
        else:
            await ctx.send(f"No channel named **{channel.name}** was found!")
    @delete.error
    async def delete_error(self, ctx, error):
        if isinstance(error, checks.NoManageChannelPermission):
            embed = error.embed
            await ctx.send(embed=embed)

    @checks.has_manage_channels_permission()
    @commands.hybrid_command(aliases=["clc"], name="clone", description="Clones a channel")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(channel="The channel to clone")
    async def clone(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            new_channel = await ctx.channel.clone(reason=f"Cloned by {ctx.author}")
            await ctx.send(f"Channel cloned! {new_channel.mention}!")
        else:
            new_channel = await channel.clone(reason=f"Channel cloned by {ctx.author}")
            await ctx.send(f"Channel cloned! {new_channel.mention}!")
    @clone.error
    async def clone_error(self, ctx, error):
        if isinstance(error, checks.NoManageChannelPermission):
            embed = error.embed
            await ctx.send(embed=embed)
        
    @checks.has_manage_channels_permission()
    @commands.hybrid_command(aliases=["crc"], name="create", description="Creates a channel")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(channel_name="Name of the new channel")
    async def create(self, ctx, channel_name: str):
        if channel_name is not None:
            new_channel = await ctx.create_text_channel(channel_name, category = ctx.channel.category)
            await ctx.send(f"Channel created! {new_channel.mention}")
        else:
            await ctx.send(f"A channel named **{channel_name}** already exists!")
            return
    @create.error
    async def create_error(self, ctx, error):
        if isinstance(error, checks.NoManageChannelPermission):
            embed = error.embed
            await ctx.send(embed=embed)

    @checks.has_manage_channels_permission()
    @commands.hybrid_command(aliases=["rc"], name="rename", description="Renames a channel")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(new_name="The new name of the channel")
    @app_commands.describe(channel="The channel to rename")
    async def rename(self, ctx, new_name: str, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
            await channel.edit(name=new_name)
            await ctx.send(f"Channel renamed to **{new_name}**!")
        else:
            await channel.edit(name=new_name)
            await ctx.send(f"Channel renamed to **{new_name}**!")
    @rename.error
    async def rename_error(self, ctx, error):
        if isinstance(error, checks.NoManageChannelPermission):
            embed = error.embed
            await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(Channels(bot))

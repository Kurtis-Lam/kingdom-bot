import discord
from discord.ext import commands
from views import ConfirmChannelView
from helpers import checks

class Channels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.has_manage_channels_permission()
    @commands.hybrid_command(aliases=["nc"], name="nuke", description="Nukes a channel")
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            await ctx.send(f"{ctx.author.mention} please mention channel!", delete_after = 5)
            return
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
    async def delete(self, ctx, channel: discord.TextChannel = None):
        delete_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
        if channel is None: 
            await ctx.send(f"{ctx.author.mention}! You did not mention a channel!", delete_after=5)
            return
        if delete_channel is not None:
            view = ConfirmChannelView.channelActionConfirm(ctx, "delete", delete_channel)
            await ctx.send(f"{ctx.author.mention}, are you sure you want to clone {delete_channel.mention}?", view=view)
        else:
            await ctx.send(f"No channel named **{channel.name}** was found!")
    @delete.error
    async def delete_error(self, ctx, error):
        if isinstance(error, checks.NoManageChannelPermission):
            embed = error.embed
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Channels(bot))

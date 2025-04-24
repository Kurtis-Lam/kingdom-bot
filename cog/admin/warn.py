import discord
from discord.ext import commands
import json
import os
from helpers import checks

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warns: dict = self.load_warns()

    def load_warns(self):
        if not os.path.exists("warns.json"):
            return {}
        with open("warns.json", "r") as file:
            try:
                warns = json.load(file)
            except json.JSONDecodeError:
                warns = {}
        return warns

    @checks.has_kick_members_permission()
    @commands.hybrid_command(name="warn", description="Warn a user")
    @commands.has_permissions(ban_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if member is None:
            await ctx.send(f"{ctx.author.mention} Please mention a member to warn!", delete_after = 5)
        elif reason is None:
            await ctx.send(f"{ctx.author.mention} Please provide a reason!", delete_after = 5)
        else:
            user_id = str(member.id)
            if user_id not in self.warns:
                self.warns[user_id] = []
            self.warns[user_id].append(reason)
            self.save_warns()
            warn_embed = discord.Embed(
                title="User Successfully Warned ✅",
                description=f"**Member:** {member.mention}\n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author.mention}",
                color=discord.Color.green()
            )
            await ctx.send(embed=warn_embed)

    @checks.has_kick_members_permission()
    @commands.hybrid_command(aliases=["warns", "warning", "checkwarns", "checkwarning", "checkwarnings", "cws"], name="warnings", description="Check a user's warnings")
    @commands.has_permissions(ban_members=True)
    async def warnings(self, ctx, member: discord.Member):
        user_id = str(member.id)
        if user_id not in self.warns:
            await ctx.send(f"**{member.display_name}** has no warnings.")
        else:
            warns_embed = discord.Embed(
                title=f"Warnings for {member.display_name}",
                color=discord.Color.green()
            )
            for i, reason in enumerate(self.warns[user_id], start=1):
                warns_embed.add_field(name=f"Warning {i}", value=reason, inline=False)
            await ctx.send(embed=warns_embed)
    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, checks.NoKickMembersPermission):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
    @warnings.error
    async def warnings_error(self, ctx, error):
        if isinstance(error, checks.NoKickMembersPermission):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
    def save_warns(self):
        with open("warns.json", "w") as file:
            json.dump(self.warns, file)
    def save_warns_users(self):
        with open("warns.json", "w") as file:
            json.dump(self.warns, file, indent = 4)

async def setup(bot):
    await bot.add_cog(Warn(bot))
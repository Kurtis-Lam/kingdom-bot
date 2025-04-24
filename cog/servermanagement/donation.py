import discord
from discord.ext import commands
import json

class Donation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def ea(self, ctx, amt: int):
        await ctx.message.delete()
        with open('earned.json', 'r') as f:
            earned = json.load(f)
        earned['total'] = earned.get('total', 0) + amt
        with open('earned.json', 'w') as f:
            json.dump(earned, f, indent=4)
        await ctx.send("Successfully Logged", delete_after = 2)
            
    @commands.command(aliases=["donoadd", "da"])
    @commands.has_permissions(administrator=True)
    async def donationsadd(self, ctx, user: discord.Member, amount: int):
        user_id = str(user.id)
        with open('donations.json', 'r') as f:
    	    donations = json.load(f)
        if user_id in donations:
            donations[user_id] += amount
        else:
            donations[user_id] = amount
        with open('donations.json', 'w') as f:
            json.dump(donations, f, indent=4)
        await ctx.message.delete()
        e = discord.Embed(title=f"Successfully added {amount:,} donated Pokécoins to {user.display_name}!", description=f"{user.mention} has donated a total of {donations[user_id]:,} Pokécoins", color=discord.Color.green())
        e.set_footer(text = f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=e)

    @commands.command(aliases=["donolb", "donationslb", "dlb"])
    async def donationsleaderboard(self, ctx):
        with open('donations.json', 'r') as f:
        	donations = json.load(f)
        sorted_donations = sorted(donations.items(), key=lambda x: x[1], reverse=True)
        e = discord.Embed(title="Donations Leaderboard", color = 0x0097ff)
        for i, (user_id, amount) in enumerate(sorted_donations):
            user = self.bot.get_user(user_id)
            if user is None:
                user = await self.bot.fetch_user(user_id)
            e.add_field(name=f"`#{i+1}` - **{user.display_name}**", value=f"{amount:,} Pokécoins", inline=False)
        e.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.message.delete()
        await ctx.send(embed=e)

    @commands.command(aliases=["d", "dono"])
    async def donated(self, ctx, user: discord.Member = None):
        if user is None:
            user_id = str(ctx.author.id)
        else:
            user_id = str(user.id)
        with open('donations.json', 'r') as f:
    	    donations = json.load(f)
        if user_id in donations:
            if user is None:
                e = discord.Embed(title=f"You have donated {donations[user_id]:,} Pokécoins!", color = 0x0097ff)
                e.set_footer(text = f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
                await ctx.send(embed=e)
            else:
                e = discord.Embed(title=f"{user.display_name} has donated {donations[user_id]:,} Pokécoins!", color = 0x0097ff)
                e.set_footer(text = f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
                await ctx.send(embed=e)
        elif user is None:
            await ctx.send('You haven\'t donated any Pokécoins yet!\n> Check <#1262755000006873249> for more info!')
        else:
            await ctx.send(f'{user.display_name} hasn\'t donated any Pokécoins yet!\n> Check <#1262755000006873249> for more info!')

async def setup(bot):
    await bot.add_cog(Donation(bot))
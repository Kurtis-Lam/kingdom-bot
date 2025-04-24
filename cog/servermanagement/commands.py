import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def donorperksinfo(self, ctx):
        e = discord.Embed(title="Donor Perks", description="Here are our donor perks!")
        bronzeem = discord.Embed(title="🥉 Bronze Donor", description=f":money_with_wings: Price: 25,000 pc\n🕒 Time: 1 month\n🔓 Access to: <#1262755028972867715>, get the role <@&1262303047472648202>\n+ ALL bronze catcher spawns in reserves server (25)\n🎉 Extra Giveaway Entries: 3", color=0xcd7f32)
        silverem = discord.Embed(title="🥈 Silver Donor", description=f":money_with_wings: Price: 30,000 pc\n🕒 Time: 1 month\n🔓 Access to: <#1262755030096936960>, get the role <@&1262302992573403207>\n+ ALL silver - bronze catcher spawns in reserves server (50)\n🎉 Extra Giveaway Entries: 4", color=0xc0c0c0)
        goldem = discord.Embed(title="🥇 Gold Donor", description=f":money_with_wings: Price: 35,000 pc\n🕒 Time: 1 month\n🔓 Access to: <#1262755031053242420>, get the role <@&1262303087155220563>\n+ ALL gold - bronze catcher spawns in reserves server (75)\n🎉 Extra Giveaway Entries: 5", color=0xffd700)
        diamondem = discord.Embed(title="💎 Diamond Donor", description=f":money_with_wings: Price: 45,500 pc\n🕒 Time: 1 month\n🔓 Access to: <#1262755031937974343>, get the role <@&1262936963523153970>\n+ ALL diamond - bronze catcher spawns in reserves server (100)\n+ <@&1263366984452538380> and <@&1263367025896718478> ping\n🎉 Extra Giveaway Entries: 6", color=0xb9f2ff)
        eliteem = discord.Embed(title="🔮 Platinum Donor", description=f":money_with_wings: Price: 50,000 pc\n🕒 Time: 1 month\n🔓 Access to: <#1262755033137811529>, get the role <@&1262936983290904748>\n+ ALL plantinum - bronze catcher spawns in reserves server (125)\n+ <@&1263366984452538380> and <@&1263367025896718478> ping\n🎉 Extra Giveaway Entries: 7", color=0x50c878)
        vipem = discord.Embed(title="👑 Elite Donor", description=f":money_with_wings: Price: 60,000 pc\n🕒 Time: 1 month\n🔓 Access to: <#1262755040511262771>, get the role <@&1262936998847713390>\n+ ALL spawns channels in reserves server (150)\n+ <@&1263366984452538380> and <@&1263367025896718478> ping\n🎉 Extra Giveaway Entries: 9", color=0xee4b2b)
        mythem = discord.Embed(title="🦄 Mythical Donor", description=f":money_with_wings: Price: 300,000 pc\n🕒 Time: 6 months\n🔓 Access to: <#1262755040511262771>, get the role <@&1305020933488250880>\n+ ALL spawns channels in reserves server (150)\n+ <@&1263366984452538380> and <@&1263367025896718478> ping\n🎉 Extra Giveaway Entries: 9", color=0x800080)
        legem = discord.Embed(title="🏆 Legendary Donor", description=f":money_with_wings: Price: 600,000 pc\n🕒 Time: 1 year\n🔓 Access to: <#1262755040511262771>, get the role <@&1305021031152484393>\n+ ALL spawns channels in reserves server (150)\n+ <@&1263366984452538380> and <@&1263367025896718478> ping\n🎉 Extra Giveaway Entries: 9", color=0x006400)
        divineem = discord.Embed(title="✨ Divine Donor", description=f":money_with_wings: Price: 800,000 pc\n🕒 Time: FOREVER\n🔓 Access to: <#1262755040511262771>, get the role <@&1299916227858272296>\n+ ALL spawns channels in reserves server (150)\n+ <@&1263366984452538380> and <@&1263367025896718478> ping\n🎉 Extra Giveaway Entries: 9", color=0x00008b)
        ticketem = discord.Embed(title="", description=f"🎫 Create a ticket at <#1263395472354054195> to claim your role!")
        ykwim = discord.Embed(title="", description=f"Of course, this means that getting access to <#1262755031053242420> means that you will also gain access to <#1262755030096936960> and <#1262755028972867715> etc... You get what I mean-")
        raikou = discord.Embed(title="", description=f"Also, check <#1278704752309571704> for more information on getting access to donor channels.")
        await ctx.send(embed = e)
        await ctx.send(embed = bronzeem)
        await ctx.send(embed = silverem)
        await ctx.send(embed = goldem)
        await ctx.send(embed = diamondem)
        await ctx.send(embed = eliteem)
        await ctx.send(embed = vipem)
        await ctx.send(embed = mythem)
        await ctx.send(embed = legem)
        await ctx.send(embed = divineem)
        await ctx.send(embed = ticketem)
        await ctx.send(embed = raikou)
        await ctx.send(embed = ykwim)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def chateventinfo(self, ctx):
        e = discord.Embed(title="Chat Event", description="")
        e.add_field(name="🥇 1st Place", value="  🎯 At least 1000+ messages\n  💰 Prize: 250 pc", inline = False)
        e.add_field(name="🥈 2nd Place", value="  🎯 At least 750+ messages\n  💰 Prize: 150 pc", inline = False)
        e.add_field(name="🥉 3rd Place", value="  🎯 At least 500+ messages\n  💰 Prize: 50 pc", inline = False)
        e.add_field(name="", value="🎯 Fail to meet requirement: 💰 Prize ÷ 3", inline = False)
        e.set_footer(text="Prizes may be small considering we are a server of 70 members\nStaffs can also participate, also counting in staff chat channel")
        await ctx.send(embed = e)
        await ctx.send(f"NEW <@&1272441328948609055> !\n😎 Start Chatting!")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def catcheventinfo(self, ctx):
        e = discord.Embed(title="Catch Event", description="")
        e.add_field(name="🥇 1st Place", value="  🎯 At least 1000+ catches\n  💰 Prize: 250k pc", inline = False)
        e.add_field(name="🥈 2nd Place", value="  🎯 At least 750+ catches\n  💰 Prize: 150k pc", inline = False)
        e.add_field(name="🥉 3rd Place", value="  🎯 At least 500+ catches\n  💰 Prize: 50k pc", inline = False)
        e.add_field(name="", value="🎯 Fail to meet requirement: 💰 Prize ÷ 3", inline = False)
        e.set_footer(text="Prizes may be small considering we are a server of 70 members\nStaffs can also participate, also counting in staff spawns channel")
        await ctx.send(embed = e)
        await ctx.send("Catches are count by <@1251527817510780938>\n> Do `.caught` / `.c` to view your stats.\n> Do `.catchleaderboard` / `.clb` to view the catch leaderboard")
        await ctx.send(f"# https://discord.com/channels/1261873096147865642/1263395472354054195/1272457092891938827 CREATE A TICKET HERE TO HOST YOUR OWN PRIVATE INCNSES AND GRINDDDDD.\n Note: We have removed Poke-Stats from all tickets, we want Poke-Stats to only count spawns channels.")
        await ctx.send(f"NEW <@&1272441301576454218> !\n😎 Start Catching!")
        
async def setup(bot):
    await bot.add_cog(Commands(bot))
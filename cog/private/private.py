import discord
from discord.ext import commands

class Private(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def arewelegit(self, ctx):
        e = discord.Embed(title="Are We Legit???\n✅ = Legit\n❌ = Not Legit", description="")
        e.add_field(name="React with ✅ !", value="", inline = False)
        e.add_field(name="React with ❌ without proof = ban", value="", inline = False)
        msg = await ctx.send(embed = e)
        await msg.add_reaction("✅")
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reactionrolesembed(self, ctx):
        se = discord.Embed(title="Server Based", description="Server Based Roles!\nReact to the emojis to get pinged!")
        se.add_field(name="📢 Announcement Ping", value = "", inline = False)
        se.add_field(name="🆕 Updates Ping", value = "", inline = False)
        pe = discord.Embed(title="Pokétwo Based", description="Pokétwo Based Roles!\nReact to the emojis to get pinged!")
        pe.add_field(name="🎉 Giveaway Ping", value = "", inline = False)
        pe.add_field(name="🎇 Incense Ping", value = "", inline = False)
        pe.add_field(name="🔍 Mystery Redeem Ping", value = "", inline = False)
        ee = discord.Embed(title="Event Based", description="Event Based Roles!\nReact to the emojis to get pinged!")
        ee.add_field(name="💫 Catch Event Ping", value = "", inline = False)
        ee.add_field(name="💬 Chat Event Ping", value = "", inline = False)
        ee.add_field(name="⭐ General Event Ping", value = "", inline = False)
        ue = discord.Embed(title="User Info Based", description="User Info Based Roles!\nReact to the emojis to get pinged!")
        ue.add_field(name="➕ 18+ Role", value = "", inline = False)
        ue.add_field(name="➖ 18- Role", value = "", inline = False)
        ue.add_field(name="♂ Male Role", value = "", inline = False)
        ue.add_field(name="♀ Female Role", value = "", inline = False)
        await ctx.send(embed = se)
        await ctx.send(embed = pe)
        await ctx.send(embed = ee)
        await ctx.send(embed = ue)
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ctfnr(self, ctx):
        e = discord.Embed(title = "Creating a ticket for no reason will lead to a ban", description = "")
        await ctx.send(embed = e)
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def donorperksinfo(self, ctx):
        e = discord.Embed(title="Donor Perks", description="Here are our donor perks!")
        e.add_field(name="🥉 Bronze Donor", value=":money_with_wings: Price: 50,000 pc\n🕒 Time: 14 days\n", inline = False)
        e.add_field(name="🥈 Silver Donor", value=":money_with_wings: Price: 100,000 pc\n🕒 Time: 28 days\n", inline = False)
        e.add_field(name="🥇 Gold Donor", value=":money_with_wings: Price: 300,000 pc\n🕒 Time: 42 days\n", inline = False)
        e.add_field(name="💎 Diamond Donor", value=":money_with_wings: Price: 500,000 pc\n🕒 Time: 56 days\n", inline = False)
        e.add_field(name="👑 Elite Donor", value=":money_with_wings: Price: 1,000,000 pc\n🕒 Time: 84 days\n", inline = False)
        await ctx.send(embed = e)
        await ctx.send("For Bronze, Silver, Gold, Diamond, and Elite Donor, you can get access to <#1258955312728375369> <#1258955344705753088> <#1258955373101187092> <#1258955427501314060> and <#1258955511999500353> spawn channels respectively")
        await ctx.send("Create a ticket at https://discord.com/channels/1258403516712489054/1258956162724794450/1261542940170391604 ")
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def vipperksinfo(self, ctx):
        e = discord.Embed(title="VIP Perks", description="Here are our VIP perks!")
        e.add_field(name="⭐ VIP", value=":money_with_wings: Price: 3,000,000 pc\n🕒 Time: 180 days", inline = False)
        await ctx.send(embed = e)
        await ctx.send(f"For VIP, you can get access to <#1258955745513177088> spawn channel")
        await ctx.send("Create a ticket at https://discord.com/channels/1258403516712489054/1258956162724794450/1261542940170391604 ")
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def catcheventinfo(self, ctx):
        e = discord.Embed(title="Catch Event", description="")
        e.add_field(name="🥇 1st Place", value="🎯 At least 1000+ catches\n💰 Prize: 300k pc", inline = False)
        e.add_field(name="🥈 2nd Place", value="🎯 At least 750+ catches\n💰 Prize: 200k pc", inline = False)
        e.add_field(name="🥉 3rd Place", value="🎯 At least 500+ catches\n💰 Prize: 100k pc", inline = False)
        e.add_field(name="", value="🎯 Fail to meet requirement: 💰 Prize ÷ 2", inline = False)
        await ctx.send(embed = e)
        await ctx.send("NEW <@&1259847380531019886> !\n😎 Start Catching!\n🛠️ <@&1258408012926947459>s can also participate!")


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *args):
        message = ' '.join(args)
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Private(bot))

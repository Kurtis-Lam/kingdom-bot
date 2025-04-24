import asyncio
from discord.ext import commands
from views import PingView

class FPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.latencies = []
        self.editing = False
        self.current_channel = None
        self.current_message = None
        self.task = None 

    @commands.hybrid_command(aliases=["fp"], name="fping", description="Check the bot's 24/7 latency!")
    @commands.has_permissions(manage_guild=True)
    async def fping(self, ctx):
        if self.editing:
            await ctx.send(f"Updating of the bot's latency is already in progress. {self.current_message.jump_url}")
            return
        self.editing = True
        self.current_channel = ctx.channel
        message = await ctx.send('Pong!')
        self.current_message = message
        self.task = self.bot.loop.create_task(self.update_latency(message)) 

    async def update_latency(self, message):
        i = 1
        while self.editing:
            await asyncio.sleep(60)
            latency = self.bot.latency * 1000
            self.latencies.append(latency)
            await message.edit(content=self.format_latency(latency, i))
            i += 60

    def format_latency(self, latency, i):
        return f"Pong! **{latency:.2f} ms**\n`Highest Latency`: **{max(self.latencies):.2f} ms**\n`Lowest Latency`: **{min(self.latencies):.2f} ms**\n`Average Latency`: **{sum(self.latencies) / len(self.latencies):.2f} ms**\n`Seconds Elapsed`: **{i} secs**"

    @commands.hybrid_command(aliases=["fpe"], name="fpingend" , description="End the bot's 24/7 latency!")
    @commands.has_permissions(manage_guild=True)
    async def fpingend(self, ctx):
        if not self.editing:
            await ctx.send("Updating of the bot's latency has not been started.")
            return
        self.editing = False
        if self.task:
            self.task.cancel() 
        self.latencies = []
        await ctx.send("Updating of bot's latency has successfully been stopped.")

    @commands.hybrid_command(aliases=["fps"], name="fpingstats", description="Check the bot's 24/7 latency stats!")
    async def fpingstats(self, ctx):
        if not self.latencies:
            await ctx.send("No latency data available.")
            return
        highest_latency = max(self.latencies)
        lowest_latency = min(self.latencies)
        average_latency = sum(self.latencies) / len(self.latencies)
        await ctx.send(f"`Highest Latency`: **{highest_latency:.2f} ms**")
        await ctx.send(f"`Lowest Latency`: **{lowest_latency:.2f} ms**")
        await ctx.send(f"`Average Latency`: **{average_latency:.2f} ms**")

    @commands.hybrid_command(name="ping", description="Check the bot's latency")
    async def ping(self, ctx):
        if not ctx.author.guild_permissions.manage_channels:
            msg = await ctx.send("Pong!")
            latency = self.bot.latency * 1000
            await msg.edit(content = f"Pong! **{latency:.2f} ms**")
        elif ctx.author.guild_permissions.manage_channels:
            view = PingView.PingView(ctx)
            msg = await ctx.send("Pong!", view = view)
            latency = self.bot.latency * 1000
            await msg.edit(content = f"Pong! **{latency:.2f} ms**")

async def setup(bot):
    await bot.add_cog(FPing(bot))
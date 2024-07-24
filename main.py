import discord
from discord.ext import commands
import os
import asyncio
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = ".", intents = intents)
bot.remove_command("help")

token = os.environ["TOKEN"]

spawn_count = 0
start_time = None
message = None

cogs_dict = {
    "admin": ["channel", "fping", "message", "warn"],
    "economy": ["balance", "register"],
    "minigames": ["dig", "rps"],
    #"private": ["private", "make"]
    "utilities": ["help"]
}
async def load_cogs():
    for category, cogs in cogs_dict.items():
        category_path = f'cogs.{category}'
        for cog in cogs:
            try:
                await bot.load_extension(f'{category_path}.{cog.lower()}')
                print(f'{cog.upper()} cog loaded.')
            except Exception as e:
                print(f'Failed to load {cog.upper()} cog: {e}')

@bot.tree.command(name="hello", description="Says hi to the bot lmfao")
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi! {interaction.user.mention} 👋")
    
@bot.event
async def on_ready():
    await load_cogs()
    await bot.tree.sync()
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    global spawn_count
    if message.author.id == 716390085896962058 and message.embeds:
        embed = message.embeds[0]
        if embed.title.startswith("A wild pokémon has appeared!") or embed.title.startswith("Wild"):
            spawn_count += 1
    await bot.process_commands(message)
@bot.command()
async def start(ctx):
    global start_time, message
    start_time = datetime.now()
    message = await ctx.send("0 spawns per hour")
    while True:
        await asyncio.sleep(1)
        spawns_per_hour = spawn_count / ((datetime.now() - start_time).total_seconds() / 3600)
        spawns_per_hour_int = int(spawns_per_hour)
        await message.edit(content=f"{spawns_per_hour_int:.2f} spawns per hour")
    
try:
    bot.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e

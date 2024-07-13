import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = ".", intents = intents)

token = "fuck whoever hacked me with the bots token"

cogs_dict = {
    "admin": ["channel", "fping", "warn"],
    "economy": ["balance", "register"],
    "minigames": ["dig", "rps"],
    "private": ["private"]
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

@bot.tree.command(name="first_slash_command", 
                  description="Yes, this was the bot's very first slash command. LMFAO")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hi! {interaction.user.mention} This was the bot's very first slash command. LMFAO")
    
@bot.event
async def on_ready():
    await load_cogs()
    await bot.tree.sync()
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    
try:
    bot.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e

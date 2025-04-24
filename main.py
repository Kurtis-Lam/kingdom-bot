import discord
from discord.ext import commands
import asyncio
import datetime
import json
import random
import schedule
import time
import requests
import pytz
from discord.utils import format_dt
from datetime import timedelta
from datetime import datetime
from openai import OpenAI




owners = [1250429544486273038, 1261606164437667882]
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix = ".", owner_ids = set(owners), intents = intents)
bot.remove_command("help")
token = "MTI1MTUyNzgxNzUxMDc4MDkzOA.G11vpp.cNggVR8JNBmPbBqQchwp-mJKJOh0hgbxIUaP8M"

XAI_API_KEY = "xai-CQ0intt8owpOftZfV63yenpYKymhCCPv4QCGpR3VxevVoXQ0zkuxJX2oy8GuqThZ1xDPiQsJWQ7VaF8D"
client = OpenAI(
    api_key = XAI_API_KEY,
    base_url = "https://api.x.ai/v1",
)




cogs_dict = {
    "admin": ["channel", "fping", "message"],
    "economy": ["admin", "balance", "inventory", "register", "shop", "sell", "buy"],
    "economy_games": ["burgle", "coinflip", "dig", "farm", "fish", "hunt", "rps"],
    "poketwo": ["catch", "lockunlock"],
    "servermanagement": ["commands", "donation", "reserve"],
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
async def send_jsons():
    await bot.wait_until_ready()
    balance = bot.get_channel(1314768934511316992)
    kingdomcatch = bot.get_channel(1315127841926549628)
    reservecatch = bot.get_channel(1315127863833530368)
    grindingcatch = bot.get_channel(1315127889242488924)
    reservepkm = bot.get_channel(1317823839912067145)
    
    while not bot.is_closed():
        with open('balance.json', 'r') as f:
            balance_data = json.load(f)
        with open('kingdomcatch.json', 'r') as f:
            kingdomcatch_data = json.load(f)
        with open('reservecatch.json', 'r') as f:
            reservecatch_data = json.load(f)
        with open('grindingcatch.json', 'r') as f:
            grindingcatch_data = json.load(f)
        with open('reserves.json', 'r') as f:
            reservepkm_data = json.load(f)
        
        channels = {
            balance: balance_data,
            kingdomcatch: kingdomcatch_data,
            reservecatch: reservecatch_data,
            grindingcatch: grindingcatch_data,
            reservepkm: reservepkm_data
        }
        
        for channel, data in channels.items():
            json_string = json.dumps(data, indent=4)
            messages = []
            while len(json_string) > 0:
                if len(json_string) > 1900:
                    messages.append(json_string[:1900])
                    json_string = json_string[1900:]
                else:
                    messages.append(json_string)
                    json_string = ""
            
            for i, message in enumerate(messages):
                if i == 0:
                    await channel.send(f'```json\n{message}\n```')
                else:
                    await channel.send(f'```json\n{message}\n```')
        
        await asyncio.sleep(300)
                
                
                
                
@bot.event
async def on_ready():
    await bot.tree.sync()
    await load_cogs()
    await bot.loop.create_task(send_jsons())
    print('We have logged in as {0.user}'.format(bot))
    print(discord.utils.oauth_url(bot.user.id))
    

@bot.event
async def on_message_delete(message):
    #ANTI GHOST PING
    if message.author == bot.user:
        return
    if message.guild:
        if message.mentions or message.role_mentions:
            if message.author.id == 824119071556763668:
                return
            hk_tz = pytz.timezone('Asia/Hong_Kong')
            hk_time = message.created_at.astimezone(hk_tz).strftime('%Y-%m-%d %H:%M:%S')
            embed = discord.Embed(
                title="",
                description=f"**Author:** {message.author.mention}\n**Content:** {message.content}\n**Time Sent:** {hk_time}",
                color=discord.Color.red()
            )
            embed.set_author(name="Message Deleted ❗", icon_url=message.author.avatar.url)
            embed.set_footer(text=f"Message ID: {message.id}")
            await message.channel.send(embed=embed)
@bot.event
async def on_message(message):
    #BUMP
    def load_bal_data(file):
        with open(file, "r") as f:
            return json.load(f)
    def save_bal_data(file, data):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
    def load_bump_count():
        with open('bump.json', 'r') as file:
            data = json.load(file)
            return data.get('bump_count', 0)
    def save_bump_count(count):
        with open('bump.json', 'w') as file:
            json.dump({'bump_count': count}, file)
    if message.author.id == 302050872383242240 and message.channel.id == 1289570458022182965:
        bump_count = load_bump_count()
        bump_count += 1
        save_bump_count(bump_count)
        await message.channel.send(f'Bump done! New count: **{bump_count}**')
    #CHATBOT
    if message.channel.id == 1312762530271330314:
        if message.author.bot:
            return
        m = message.content
        completion = client.chat.completions.create(
        model="grok-beta",
        messages=[
               {"role": "system", "content": "Your name is Pokétwo Kingdom Helper. You were developed by Kai. Kai used x.ai’s API key to develop you. Your job is to ensure security in Pokétwo Kingdom. You are also a fun bot and people can use commands with a prefix of `.` to play games. First of all, users have to use the `.register` command to register themselves. Games you have: `.dig`: Lets users dig for coins in the earth and get a random number of coins between 10 and 10000. There is also a 1/10 chance of getting a gem. `.rps`: Lets users play rock paper scissors with the bot. If the user wins, they get 300 coins. If they lose, they get 100 coins. If they tie, they get 200 coins. `.burgle`: Burgle money from the bank. Users can get either 100, 200, 300, 400, or 500 coins from the bank. There is a 1/50 chance of getting a ruby. Users can use `.bal` to view their balance. They can also use `.shop` and `.buy` to exchange coins for gems, or exchange gems for rubies. The gems and rubies will be used to buy other interesting things later on. (Kai is making those functions in the bot.) REMEMBER, EVERYTIME A USER SENDS HELLO, YOU DON’T NEED TO TELL THEM THEY CAN PLAY THESE GAMES. Just tell them if they ask. Also, when users type `.dig`, `.rps`, or `.burgle`, just say good luck. When they type `.bal`, respond with something like \"There goes your balance!\" Or \"Wow, you're so rich!\" etc... If they type `register`. Just respond with something like \“Good Luck on your playing journey\”. When someone sends a message with the meaning of \"I won a giveaway with prize xxx\", tell them to create a ticket and send screenshot of winning and drop market id for Kai to buy."},
                {"role": "user", "content": m},
            ],
        )
        await message.channel.send(completion.choices[0].message.content)
    #LEGIT
    if message.channel.id == 1262754995766296646 and not message.author.bot:
        if "legit" in message.content.lower():
            try:
                await message.add_reaction(f"<:legit:1309865282109575178>")
            except discord.HTTPException:
                print(f"Failed to react to message {message.id}")
    #MESSAGES
    if "vouch" in message.content:
        if message.author.id != 1251527817510780938:
            await message.channel.send("**Congratulations on winning!**\n> 1. Check proof in <#1262754994386636823>!\n> 2. React with ✅ in <#1262754993195454575>!\n> 3. Vouch for us in <#1262754995766296646>!\n```Legit got xxx from @user```")
    if "ticket" in message.content:
        if message.author.id != 1251527817510780938:
            if message.author.id != 557628352828014614:
                if message.author.id != 1250429544486273038:
                    await message.channel.send("<#1263395472354054195>")
    if "vote" in message.content:
        if message.author.id != 1251527817510780938:
            await message.channel.send("https://discords.com/servers/1261873096147865642/upvote")
    
    
    
    
    
    #GIVEAWAY
    if message.author.id == 530082442967646230:
        if message.content.startswith(("Congratulations to", "The new winner of the")):
            mentions = message.mentions 
            if len(mentions) > 0:
                msg_link = message.jump_url
                for user in mentions:
                    e = discord.Embed(title="Congratulations, you won a giveaway! 🎉", description=f"{msg_link}\n> Create a <#1263395472354054195> to claim!")
                    await user.send(embed=e)
                    
                    
                    
                    
                    
    #CATCHES
    if message.author.id == 716390085896962058 or message.author.id == 1250429544486273038 and (message.mentions or message.role_mentions):
        def load_json():
            if message.guild.id == 1261873096147865642:
                with open("kingdomcatch.json", 'r') as f:
                    return json.load(f)
            elif message.guild.id == 1297077471262281729:
                with open("reservecatch.json", 'r') as f:
                    return json.load(f)
            elif message.guild.id == 1079212152814043188:
                with open("grindingcatch.json", 'r') as f:
                    return json.load(f)
            else:
                with open("kingdomcatch.json", 'r') as f:
                    return json.load(f)
                
        def save_json(data):
            if message.guild.id == 1261873096147865642:
                with open("kingdomcatch.json", 'w') as f:
                    json.dump(data, f, indent=4)
            elif message.guild.id == 1297077471262281729:
                with open("reservecatch.json", 'w') as f:
                    json.dump(data, f, indent=4)
            elif message.guild.id == 1079212152814043188:
                with open("grindingcatch.json", 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                with open("kingdomcatch.json", 'r') as f:
                    return json.load(f)
                    
        def load_locked_data():
            with open('locked.json', 'r') as file:
                return json.load(file)
    
        if message.content.startswith("Congratulations ") and len(message.mentions) > 0:
            user = message.mentions[0]
            user_id = str(user.id)
            locked_data = load_locked_data()
            if str(message.channel.id) in locked_data:
                locked_user_id = locked_data[str(message.channel.id)]
                if locked_user_id != user_id:
                    await message.channel.send(f'{user.mention}! You are not suppose to catch this pokemon!\nIt has been reserved for `{locked_user_id}`!\n> I have reported this to the admins that you stole this pokemon!\n> They will double check on this issue!')
                    specific_channel = bot.get_channel(1301878926410518558)
                    await specific_channel.send(f'**User**: {user.mention}\n**User ID**: {user.id}\n**User\'s display name**: {user.display_name}\n**User\'s username**: {user.name}\n Has stolen a pokemon that is reserved!\n> **Message link**: {message.jump_url}')
                    del locked_data[str(message.channel.id)]
                    with open('locked.json', 'w') as file:
                        json.dump(locked_data, file, indent=4)
                    return
                else:
                    del locked_data[str(message.channel.id)]
                    with open('locked.json', 'w') as file:
                        json.dump(locked_data, file, indent=4)   
            data = load_json()
            if user_id in data:
                data[user_id] += 1
            else:
                data[user_id] = 1
            save_json(data)
            await message.channel.send(f'> **{user.name}** has caught a Pokémon in the world of Poketwo!')
            
            
            
            
            
    #LOCKS
    if message.author.id == 874910942490677270 or message.author.id == 854233015475109888 or message.author.id == 1250429544486273038 or message.author.id == 1254602968938844171 and (message.mentions or message.role_mentions):
        #POKETWO KINGDOM
        if message.guild.id == 1261873096147865642:
            for mention in message.mentions + message.role_mentions:
                #1263366984452538380 - RARE
                #1263367025896718478 - REGIONAL
                #1250429544486273038 - KAI
                #1261606164437667882 - TG
                if mention.id in [1263366984452538380, 1263367025896718478, 1261606164437667882]:
                    user_id = 716390085896962058 
                    permissions = discord.PermissionOverwrite(
                        read_messages=False,
                         send_messages=False
                    )
                    channel = message.channel
                    user = await bot.fetch_user(user_id)
                    lock = await channel.send("Locking in 10 seconds...")
                    def check(msg):
                        return (msg.author.id == 716390085896962058 or msg.author.id == 1250429544486273038) and msg.channel == channel and msg.content.startswith("Congratulations")
                    try:
                        msg = await bot.wait_for('message', timeout=10, check=check)
                        if msg:
                            await lock.delete()
                            return
                    except asyncio.TimeoutError:
                        pass
                    await channel.set_permissions(user, overwrite=permissions)
                if mention.id in [1263366984452538380]:
                    content = "**<@&1263366984452538380> POKEMON**"
                    embed = discord.Embed(title="", description="", color=discord.Color.red())
                    embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                    embed.add_field(name="", value=f"`.unlock` - Everyone may unlock this channel", inline=False)
                    await lock.delete()
                    await channel.send(content=content, embed=embed)
                if mention.id in [1263367025896718478]:
                    content = "**<@&1263367025896718478> POKEMON**"
                    embed = discord.Embed(title="", description="", color=discord.Color.red())
                    embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                    embed.add_field(name="", value=f"`.unlock` - Everyone may unlock this channel", inline=False)
                    await lock.delete()
                    await channel.send(content=content, embed=embed)
                if mention.id in [1261606164437667882]:
                    if message.author.id == 854233015475109888:
                        message_content = message.content
                        name = message_content.split(':')[0].strip()
                        if name == "Raikou":
                            content = "**<@1261606164437667882>**"
                            embed = discord.Embed(title="", description="", color=discord.Color.red())
                            embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                            embed.add_field(name="", value=f"`.unlock` - RESERVED FOR <@1261606164437667882>", inline=False)
                            await lock.delete()
                            await channel.send(content=content, embed=embed)
                    else:
                        content = "**EVENT POKEMON**"
                        embed = discord.Embed(title="", description="", color=discord.Color.red())
                        embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                        embed.add_field(name="", value=f"`.unlock` - Everyone may unlock this channel", inline=False)
                        await lock.delete()
                        await channel.send(content=content, embed=embed)

        #KL GRINDING
        if message.guild.id == 1079212152814043188:
            for mention in message.mentions + message.role_mentions:
                #1276161273989697588 - RARE
                #1276161290653667368 - REGIONAL
                #1250429544486273038 - KAI
                #1261606164437667882 - TG
                if mention.id in [1276161273989697588, 1276161290653667368, 1250429544486273038, 1205014530313158676, 1261606164437667882]:
                    user_id = 716390085896962058 
                    permissions = discord.PermissionOverwrite(
                        read_messages=False,
                        send_messages=False
                    )
                    channel = message.channel
                    user = await bot.fetch_user(user_id)
                    await channel.set_permissions(user, overwrite=permissions)
                    content = "**KL GRINDING LOCK**"
                    embed = discord.Embed(title="", description="", color=discord.Color.red())
                    embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                    embed.add_field(name="", value=f"`.unlock` - Everyone may unlock this channel", inline=False)
                    await channel.send(content=content, embed=embed)

        #POKETWO KINGDOM RESERVE SERVER
        if message.guild.id == 1297077471262281729:
            for mention in message.mentions + message.role_mentions:
                #1297916114117984266 - RARE
                #1297916135764787221 - REGIONAL
                #1261606164437667882 - TG
                if mention.id in [1297916114117984266, 1297916135764787221, 1261606164437667882]:
                    user_id = 716390085896962058 
                    permissions = discord.PermissionOverwrite(
                        read_messages=False,
                        send_messages=False
                    )
                    channel = message.channel
                    user = await bot.fetch_user(user_id)
                    lock = await channel.send("Locking in 10 seconds...")
                    def check(msg):
                        return (msg.author.id == 716390085896962058 or msg.author.id == 1250429544486273038) and msg.channel == channel and msg.content.startswith("Congratulations")
                    try:
                        msg = await bot.wait_for('message', timeout=10, check=check)
                        if msg:
                            await lock.delete()
                            return
                    except asyncio.TimeoutError:
                        pass
                    await channel.set_permissions(user, overwrite=permissions)
                if mention.id in [1297916114117984266]:
                    content = "**<@&1297916114117984266> POKEMON**"
                    embed = discord.Embed(title="", description="", color=discord.Color.red())
                    embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                    embed.add_field(name="", value=f"`.unlock` - ONLY USERS WITH RARE PING / RESERVED THIS POKEMON MAY UNLOCK", inline=False)
                    await lock.delete()
                    await channel.send(content=content, embed=embed)
                if mention.id in [1297916135764787221]:
                    content = "**<@&1297916135764787221> POKEMON**"
                    embed = discord.Embed(title="", description="", color=discord.Color.red())
                    embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                    embed.add_field(name="", value=f"`.unlock` - ONLY USERS WITH REGIONAL PING / RESERVED THIS POKEMON MAY UNLOCK", inline=False)
                    await lock.delete()
                    await channel.send(content=content, embed=embed)
                if mention.id in [1261606164437667882]:
                    content = "**EVENT POKEMON**"
                    embed = discord.Embed(title="", description="", color=discord.Color.red())
                    embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                    embed.add_field(name="", value=f"`.unlock` - Everyone may unlock this channel, unless reserved", inline=False)
                    await lock.delete()
                    await channel.send(content=content, embed=embed)
            if message.author.id == 854233015475109888 or message.author.id == 1250429544486273038:
                def load_reserves():
                    with open('reserves.json', 'r') as file:
                        return json.load(file)
                def save_reserves(reserves):
                    with open('reserves.json', 'w') as file:
                        json.dump(reserves, file, indent=4)
                reserves = load_reserves()
                for pokemon_name in reserves:
                    pokemon = pokemon_name.replace(":", "")
                    if message.content.startswith(pokemon):
                        user_id = reserves[pokemon]['user_id']
                        amount = reserves[pokemon]['amount']
                        if amount > 0:
                            reserves[pokemon]['amount'] -= 1
                            save_reserves(reserves)
                            user = await bot.fetch_user(user_id)
                            p2_user_id = 716390085896962058 
                            permissions = discord.PermissionOverwrite(
                                read_messages=False,
                                send_messages=False
                            )
                            channel = message.channel
                            p2_user = await bot.fetch_user(p2_user_id)
                            lock = await channel.send("Locking in 10 seconds...")
                            def check(msg):
                                return (msg.author.id == 716390085896962058 or msg.author.id == 1250429544486273038) and msg.channel == channel and msg.content.startswith("Congratulations")
                            try:
                                msg = await bot.wait_for('message', timeout=10, check=check)
                                if msg:
                                    await lock.delete()
                                    return
                            except asyncio.TimeoutError:
                                pass
                            await channel.set_permissions(p2_user, overwrite=permissions)
                            content = "**RESERVED POKEMON**"
                            embed = discord.Embed(title="", description="", color=discord.Color.red())
                            embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                            embed.add_field(name="", value=f"`.unlock` - RESERVED\nDo NOT unlock unless you have reserved this pokemon", inline=False)
                            await lock.delete()
                            await channel.send(content=content, embed=embed)
                            await message.channel.send(f"Pokemon Detected: `{pokemon}`\n> If the bot has detected the wrong pokemon, you may catch it!")
                            await message.channel.send(f"# Reserved for {user.mention}\n> Catching will lead to a warn.\n Check <#1297402929564876811> for more info")
                            await user.send(f"{user.mention}!\n> Your Pokémon {pokemon} has spawned!\n **Remaining reserves: {reserves[pokemon]['amount']}**\nLink: {message.jump_url}")
                            def load_locked_data():
                                with open('locked.json', 'r') as file:
                                    return json.load(file)
                            def save_locked_data(data):
                                with open('locked.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                            locked_data = load_locked_data()
                            locked_data[str(channel.id)] = str(user.id)
                            save_locked_data(locked_data)
                            await asyncio.sleep(259200)
                            p2_user_id = 716390085896962058 
                            permissions = discord.PermissionOverwrite(
                                read_messages=True,
                                send_messages=True
                            )
                            channel = message.channel
                            p2_user = await bot.fetch_user(p2_user_id)
                            await channel.set_permissions(p2_user, overwrite=permissions)
                            del locked_data[str(channel.id)]
                            save_locked_data(locked_data)
                            await channel.send("Unlocked by **Automatic** (3 days expire)")
                        else:
                            await message.channel.send(f"No one has reserved {pokemon}!\nYou can catch it!")
                        return
                        
        #OTHERS
        if message.guild.id == 1295629069584699422 or message.guild.id == 966676082059255838:
            for mention in message.mentions + message.role_mentions:
                #1323206048441700363 - RARE (Fun)
                #1323206168050405476 - REGIONAL (Fun)
                #1250429544486273038 - KAI
                if mention.id in [1323206048441700363, 1323206168050405476]:
                    user_id = 716390085896962058 
                    permissions = discord.PermissionOverwrite(
                        read_messages=False,
                        send_messages=False
                    )
                    channel = message.channel
                    user = await bot.fetch_user(user_id)
                    await channel.set_permissions(user, overwrite=permissions)
                    content = "**RARE / REGIONAL / EVENT POKEMON**"
                    embed = discord.Embed(title="", description="", color=discord.Color.red())
                    embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                    embed.add_field(name="", value=f"`.unlock` - Everyone may unlock this channel", inline=False)
                    await channel.send(content=content, embed=embed)
                if mention.id in [1250429544486273038]:
                    user_id = 716390085896962058 
                    permissions = discord.PermissionOverwrite(
                        read_messages=False,
                        send_messages=False
                    )
                    channel = message.channel
                    user = await bot.fetch_user(user_id)
                    await channel.set_permissions(user, overwrite=permissions)
                    embed = discord.Embed(title="", description="", color=discord.Color.red())
                    embed.set_author(name="🔒 Channel locked by AUTOMATIC", icon_url=bot.user.avatar.url)
                    embed.add_field(name="", value=f"`.unlock` - Please leave this for Kai (if gastly)", inline=False)
                    await channel.send(embed=embed)
          
        
        
        
    #TICKET TOOL UNLOCK
    if message.author.id == 557628352828014614:
        if any(word in message.content.lower() for word in ["welcome", "support", "giveaway", "event", "donate"]):
            user_id = 716390085896962058 
            permissions = discord.PermissionOverwrite(
                read_messages=True,
                send_messages=True
            )
            channel = message.channel
            user = await bot.fetch_user(user_id)
            await channel.set_permissions(user, overwrite=permissions)
            if message.guild.id == 1297077471262281729:
                e = "✅"
                await message.add_reaction(e)
            else:
                emoji = bot.get_emoji(1285788683995189308)
                user_id2 = 969658822962585641 
                permissions2 = discord.PermissionOverwrite(
                    read_messages=False,
                    send_messages=False
                )
                channel2 = message.channel
                user2 = await bot.fetch_user(user_id2)
                await channel2.set_permissions(user2, overwrite=permissions2)
                await message.add_reaction(emoji)
        if any(word in message.content.lower() for word in ["welcome"]):
            if message.guild.id == 1297077471262281729:
                first_mention = message.mentions[0]
                first_mention_id = first_mention.id
                await message.channel.send("Hello there. Let me take you over the steps to buy a reserve!\n----------------------------------------")
                questions = [
                    "What is the name of the **pokemon** you want to reserve?\nPlease respond in 1 word **ONLY**\n> e.g. Pikachu, Tapu-Lele, Chi-Yu",
                    "What is the **spawnrate** of the pokemon?\nPlease check in <#1297436785907073086> using `n!sr {name}`\nPlease respond with the denominator (an **integer**)\n> e.g. 237, 950, 3799",
                    "How many **reserves** do you want to buy?\nPlease respond with an **integer**!\n> e.g. 10"
                ]
                answers = []
                for question in questions:
                    await message.channel.send(question)
                    try:
                        response = await bot.wait_for(
                            'message',
                            timeout=30.0,
                            check=lambda m: m.author.id == first_mention.id and m.channel == message.channel
                        )
                        answers.append(response.content)
                    except asyncio.TimeoutError:
                        await message.channel.send("You took too long to respond! Please try again.")
                        return
            reservations = {
                237: 100,
                950: 200,
                3799: 500,
                15196: 1000,
                30393: 1200,
                60785: 1500,
                182356: 2000,
            }
            try:
                spawn_rate = int(answers[1])
                if spawn_rate in reservations:
                    price_price = reservations[spawn_rate] * int(answers[2]) 
                    price = int(price_price)
                else:
                    await message.channel.send("Error when answering spawnrate. Please ping Kai and answer manually")
                    return
            except ValueError:
                await message.channel.send("Invalid input for spawn rate or amount. Please ensure you are entering integers.")
                return
            e = discord.Embed(title="ALERT: RESERVATION WANTED!", color = 0x0097ff)
            e.add_field(name=f"Pokemon Name: `{answers[0]}`", value="", inline=False)
            e.add_field(name=f"Spawn Rate: `{int(answers[1]):,}`", value="", inline=False)
            e.add_field(name=f"Amount: `{int(answers[2]):,}`", value="", inline=False)
            e.add_field(name=f"TOTAL COST (pc): `{price:,}`", value="", inline=False)
            await message.channel.send(f"<@&1297530402197471282> {first_mention.mention} has created a ticket to buy a reserve! Information are as follows:")
            await message.channel.send(embed = e)
                
    await bot.process_commands(message)
        
        
        
@bot.tree.command(name="hello", description="makes the bot say hi to you lol")
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi! {interaction.user.mention} 👋")

            
        
        
@bot.command(aliases=["cl"])
@commands.is_owner()
async def checklist(ctx, user: discord.Member, perk: str, days: int= None):
    if days == None:
        days = 3650
    userid = str(user.id)
    if perk == "bronze":
        kroleid = 1262303047472648202
        rroleid = 1297386716692480044
    elif perk == "silver":
        kroleid = 1262302992573403207
        rroleid = 1297386745461215262
    elif perk == "gold":
        kroleid = 1262303087155220563
        rroleid = 1297386759935492118
    elif perk == "diamond":
        kroleid = 1262936963523153970
        rroleid = 1297386771079888916
    elif perk == "platinum":
        kroleid = 1262936983290904748
        rroleid = 1297386783268536454
    elif perk == "elite":
        kroleid = 1262936998847713390
        rroleid = 1297386795167912060
    elif perk == "mythical":
        kroleid = 1305020933488250880
        rroleid = 1297386795167912060
    elif perk == "legendary":
        kroleid = 1305021031152484393
        rroleid = 1297386795167912060
    elif perk == "divine":
        kroleid = 1299916227858272296
        rroleid = 1297386795167912060
    #USERID: userid
    #KINGDOM ROLE: kroleid
    #RESERVE ROLE: rroleid
    #KINGDOM RARE: 1263366984452538380
    #KINGDOM REGIONAL: 1263367025896718478
    #RESERVE RARE: 1297916114117984266
    #RESERVE REGIONAL: 1297916135764787221
    if perk != "divine":
        await ctx.send(f"```!temprole {userid} {kroleid} {days}```")
    

@bot.command()
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.add_roles(role)
    await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}", delete_after = 10)
    
@bot.command()
@commands.is_owner()
async def pingmembers(ctx):
    await ctx.message.delete()
    await ctx.send(f"<@&1262023817031847996>", delete_after = 0.1)

@bot.command()
@commands.is_owner()
async def sampleedit(ctx):
    channel = bot.get_channel(99999999999999)
    message = await channel.fetch_message(99999999999999)
    await message.edit(content="99999999999999")

@bot.command()
@commands.has_permissions(administrator=True)
async def edit(ctx, message_id: int, *, new_content: str):
    """Edit a message by its ID."""
    try:
        # Fetch the message by ID
        message = await ctx.channel.fetch_message(message_id)
        
        # Check if the message was sent by the bot
        if message.author == bot.user:
            await message.edit(content=new_content)
            await ctx.send(f'Message edited successfully: {message.jump_url}')
        else:
            await ctx.send("You can only edit messages sent by this bot.")
    except discord.NotFound:
        await ctx.send("Message not found. Please check the message ID.")
    except discord.Forbidden:
        await ctx.send("I do not have permission to edit that message.")
    except discord.HTTPException:
        await ctx.send("Failed to edit the message due to an internal error.")
        
@bot.command()
@commands.has_permissions(administrator=True)
async def dmmembers(ctx, *, message: str):
    if ctx.guild is None:
        await ctx.send("This command can only be used in a server.")
        return

    members = ctx.guild.members
    success_count = 0
    failure_count = 0

    for member in members:
        if member.bot:
            continue

        try:
            await member.send(message)
            success_count += 1
        except Exception as e:
            print(f"Failed to send message to {member.name}: {e}")
            failure_count += 1

    await ctx.send(f"Successfully sent message to {success_count} members. Failed to send to {failure_count} members.")     
    
@bot.command()
@commands.is_owner()
async def earned(ctx):
    with open('earned.json', 'r') as f:
        earned = json.load(f)
    await ctx.send(f"{earned}")



@bot.command()
@commands.is_owner()
async def greet(ctx):
    channel_id = str(ctx.channel.id)
    with open('greet.json', 'r') as f:
        greeted_channels = json.load(f)
    if channel_id in greeted_channels:
        del greeted_channels[channel_id]
        await ctx.message.delete()
        await ctx.send(f"❌ Disabled Greet in {ctx.channel.mention}!", delete_after=3)
    else:
        greeted_channels[channel_id] = True
        await ctx.message.delete()
        await ctx.send(f"✅ Enabled Greet in {ctx.channel.mention}!", delete_after=3)
    with open('greet.json', 'w') as f:
        json.dump(greeted_channels, f, indent=4)

@bot.command(aliases=["gs"])
@commands.is_owner()
async def greetshow(ctx):
    with open('greet.json', 'r') as f:
        greeted_channels = json.load(f)
    await ctx.message.delete()
    e = discord.Embed(title="Greet Configuration", description="Greet is enabled in the following chanenls:", color = 0x0097ff)
    for channel_id, enabled in greeted_channels.items():
        if enabled:
            channel = bot.get_channel(int(channel_id))
            if channel is not None:
                e.add_field(name="", value=f"{channel.mention}")
    await ctx.send(embed=e)
    
@bot.command(aliases=["gt"])
@commands.is_owner()
async def greettest(ctx):
    with open('greet.json', 'r') as f:
        greeted_channels = json.load(f)
    await ctx.message.delete()
    await ctx.send(f"✅ Successfully triggered the greet system\n> If no messages are sent, then greet isn't enabled")
    for channel_id, enabled in greeted_channels.items():
        if enabled:
            channel = bot.get_channel(int(channel_id))
            if channel is not None:
                await channel.send(f"Hello {ctx.author.mention}!", delete_after=1)

@bot.event
async def on_member_join(member):
    with open('greet.json', 'r') as f:
        greeted_channels = json.load(f)
    specific_channel_id = 1262755005287501855
    specific_channel = bot.get_channel(specific_channel_id)
    content = f"Welcome! {member.mention} to **Pokétwo Kingdom**!"
    embed = discord.Embed(title="", description = ":sparkles: Check <#1262755000006873249> for our cheapest donor perks! :money_with_wings:", color=0x0097ff)
    embed.set_author(name="Go explore Pokétwo Kingdom!", icon_url=member.guild.icon)
    await specific_channel.send(content = content, embed = embed)
    if member.guild.id == 1261873096147865642:
        for channel_id, enabled in greeted_channels.items():
            if enabled:
                channel = bot.get_channel(int(channel_id))
                if channel is not None:
                    await channel.send(f"Hello {member.mention}!", delete_after=1)



                    
                    
                    
reservations = {
    237: 100,
    950: 200,
    3799: 500,
    15196: 1000,
    30393: 1200,
    60785: 1500,
    182356: 2000,
}

@bot.command(aliases=["clrc"])
async def calculatereservecost(ctx, reservation_id: int, quantity: int):
    if reservation_id in reservations:
        total_pieces = reservations[reservation_id] * quantity
        e = discord.Embed(title = f"{total_pieces}", color = 0x0097ff)
        await ctx.send(embed = e)
    else:
        await ctx.send("Incorrect Usage", delete_after = 3)
    

@bot.command()
@commands.has_permissions(administrator=True)
async def spam(ctx, *args):
    message = ' '.join(args)
    await ctx.message.delete()
    for i in range(1, 10):
    	await ctx.send(message)

@bot.command(aliases=["mc"])
async def membercount(ctx):
    member_count = ctx.guild.member_count
    embed = discord.Embed(title=f"{ctx.guild.name}", color = 0x0097ff)
    embed.add_field(name=f'`Members`: {member_count}', value='', inline=False)
    await ctx.message.delete()
    await ctx.send(embed=embed)
    
@bot.command()
async def roll(ctx, low:int, high:int):
    if low and high is not None:
        number = random.randint(low, high)
        e = discord.Embed(title=f"{ctx.author.display_name} rolls {number} ({low} - {high})", color = 0x0097ff)
        await ctx.send(embed=e)
    else:
	    await ctx.send("You must provide **2** **different** **integers** with a difference **larger than 1** where the first number is **lower** than the second number!", delete_after=10)
        
@bot.command()
async def anime(ctx):
    api_key = 'tjv0SaPqb7To-zQI_VyObDkX_UxgV09cY9lTHgSjOKD6JgmXqdejaQW3ZdkiSsL62D-lOqie_Y6ZWCCZ0crL5GP7flikDV12rIo1G1HMDtidBFScm6-7TmcyT9ON0wYFKDInFMxs-oS-W1EFW7-x9Nk2KsHicLGdyIvMhReX3WI'
    url = f'https://api.waifu.pics/sfw/waifu'
    response = requests.get(url)
    image_url = response.json()['url']
    await ctx.send(f"{ctx.author.mention}, here is you image:", mention_author=True)
    await ctx.send(image_url)
@bot.command(aliases=["an"])
@commands.is_owner()
async def animensfw(ctx):
    await ctx.message.delete()
    api_key = 'tjv0SaPqb7To-zQI_VyObDkX_UxgV09cY9lTHgSjOKD6JgmXqdejaQW3ZdkiSsL62D-lOqie_Y6ZWCCZ0crL5GP7flikDV12rIo1G1HMDtidBFScm6-7TmcyT9ON0wYFKDInFMxs-oS-W1EFW7-x9Nk2KsHicLGdyIvMhReX3WI'
    url = f'https://api.waifu.pics/nsfw/waifu'
    response = requests.get(url)
    image_url = response.json()['url']
    await ctx.send(image_url)
        
@bot.command()
@commands.is_owner()
async def addprefix (ctx, amt: int): #This is for poketwo redirection 
    prefixed_numbers = [f"#{i}" for i in range(1, amt + 1)]
    result = ' '.join(prefixed_numbers)
    formatted_result = f"```\n{result}\n```"
    await ctx.send(formatted_result)
        
try:
    bot.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
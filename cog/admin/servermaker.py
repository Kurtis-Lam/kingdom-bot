"""
For server making purposes only
**DO NOT LOAD COG UNLESS MAKING SERVER**
CONTAINS DANGEROUS COMMANDS THAT MIGHT NUKE THE WHOLE SERVER
"""


@bot.command()
async def addprefix (ctx, amt: int): #This is for poketwo redirection 
    prefixed_numbers = [f"#{i}" for i in range(1, amt + 1)]
    result = ' '.join(prefixed_numbers)
    formatted_result = f"```\n{result}\n```"
    await ctx.send(formatted_result)
@bot.command()
@commands.has_permissions(administrator=True)
async def thiscommandnukesawholeentireserverandrebuildsitintheformatofourreserveserverqwertyuioopasdfghjklzxcvbnmbv(ctx):
    for category in ctx.guild.categories:
        await category.delete()
    for channel in ctx.guild.channels:
        await channel.delete()
    c = await ctx.guild.create_text_channel("✅")
    await c.send("✅ Succesfully nuked server")
    
    guild = ctx.guild
    bronze = "🥉"
    bronze_id = 1297386716692480044
    bronze_role = guild.get_role(bronze_id)
    silver = "🥈"
    silver_id = 1297386745461215262
    silver_role = guild.get_role(silver_id)
    gold = "🥇"
    gold_id = 1297386759935492118
    gold_role = guild.get_role(gold_id)
    diamond = "💎"
    diamond_id = 1297386771079888916
    diamond_role = guild.get_role(diamond_id)
    elite = "🏅"
    elite_id = 1297386783268536454
    elite_role = guild.get_role(elite_id)
    vip = "⭐"
    vip_id = 1297386795167912060
    vip_role = guild.get_role(vip_id)
    
    secreto = {
        guild.default_role: discord.PermissionOverwrite(send_messages = False, read_messages = False)
    }
    modo = {
        guild.default_role: discord.PermissionOverwrite(send_messages = False, read_messages = True)
    }
    memo = {
        guild.default_role: discord.PermissionOverwrite(send_messages = True, read_messages = True)
    }
    bronzeo = {
        guild.default_role: discord.PermissionOverwrite(send_messages = False, read_messages = True),
        bronze_role: discord.PermissionOverwrite(view_channel = True, send_messages = True)
    }
    silvero = {
        guild.default_role: discord.PermissionOverwrite(send_messages = False, read_messages = True),
        silver_role: discord.PermissionOverwrite(view_channel = True, send_messages = True)
    }
    goldo = {
        guild.default_role: discord.PermissionOverwrite(send_messages = False, read_messages = True),
        gold_role: discord.PermissionOverwrite(view_channel = True, send_messages = True)
    }
    diamondo = {
        guild.default_role: discord.PermissionOverwrite(send_messages = False, read_messages = True),
        diamond_role: discord.PermissionOverwrite(view_channel = True, send_messages = True)
    }
    eliteo = {
        guild.default_role: discord.PermissionOverwrite(send_messages = False, read_messages = True),
        elite_role: discord.PermissionOverwrite(view_channel = True, send_messages = True)
    }
    vipo = {
        guild.default_role: discord.PermissionOverwrite(send_messages = False, read_messages = True),
        vip_role: discord.PermissionOverwrite(view_channel = True, send_messages = True)
    }
    
    info = await guild.create_category("Information", overwrites = modo)
    longue = await guild.create_category("Longue", overwrites = memo)
    pk1 = await guild.create_category("Bronze Catchers", overwrites = bronzeo)
    pk2 = await guild.create_category("Silver Catchers", overwrites = silvero)
    pk3 = await guild.create_category("Gold Catchers", overwrites = goldo)
    pk4 = await guild.create_category("Diamond Catchers", overwrites = diamondo)
    pk5 = await guild.create_category("Elite Catchers", overwrites = eliteo)
    pk6 = await guild.create_category("VIP Catchers", overwrites = vipo)
    staff = await guild.create_category("Staff Only", overwrites = secreto)
    
    information = await guild.create_text_channel("Information", category = info)
    announcements = await guild.create_text_channel("Announcements", category = info)
    joins = await guild.create_text_channel("Joins", category = info)
    
    for i in range(1, 26):
         await guild.create_text_channel(f"{i}", category = pk1)
    for i in range(1, 26):
         await guild.create_text_channel(f"{i+25}", category = pk2)
    for i in range(1, 26):
        await guild.create_text_channel(f"{i + 50}", category=pk3)
    for i in range(1, 26):
        await guild.create_text_channel(f"{i + 75}", category=pk4)
    for i in range(1, 26):
        await guild.create_text_channel(f"{i + 100}", category=pk5)
    for i in range(1, 26):
        await guild.create_text_channel(f"{i + 125}", category=pk6)
        
    staff_chat = await guild.create_text_channel("Staff Chat", category = staff)
    staff_cmds = await guild.create_text_channel("Staff Chat", category = staff)
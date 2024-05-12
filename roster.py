import discord
import utility

bot = utility.bot

spreadsheet = utility.spreadsheet

# Get Sheet1
runs = utility.sheet1

# Get Sheet2
balance = utility.sheet2

@bot.command()
@utility.is_admin()
async def roster1(ctx):
    # Get the guild object
    guild = ctx.guild
    
    # Get the title from Sheet1 A1 cell and make it bigger in size
    title = runs.cell(1, 1).value.upper()

    # Get names and classes from Sheet1 from row 2 to row 17
    names_sheet1 = runs.col_values(1)[1:17]
    classes_sheet1 = runs.col_values(2)[1:17]

    # Separate names into different categories
    tanks = names_sheet1[:2]
    healers = names_sheet1[2:5]
    dps = names_sheet1[5:]

    # Format the message
    message = f"# {title}\n\n"
    message += "**Tank:**\n"
    for name in tanks:
        # Get the class emoji for the name
        class_name = classes_sheet1[names_sheet1.index(name)]
        emoji_id = await utility.get_emoji_id(guild, class_name)
        if emoji_id:
            emoji = f"<:{class_name}:{emoji_id}>"
        else:
            emoji = f":{class_name}:"
        
        # Find the corresponding user in Balance and mention them
        user = discord.utils.get(guild.members, display_name=name)
        if user:
            mention = user.mention
        else:
            mention = name  # If user not found, use the name without mention
        message += f"{emoji} {mention}\n"

    message += "\n**Heal**:\n"
    for name in healers:
        # Get the class emoji for the name
        class_name = classes_sheet1[names_sheet1.index(name)]
        emoji_id = await utility.get_emoji_id(guild, class_name)
        if emoji_id:
            emoji = f"<:{class_name}:{emoji_id}>"
        else:
            emoji = f":{class_name}:"
        
        # Find the corresponding user in Balance and mention them
        user = discord.utils.get(guild.members, display_name=name)
        if user:
            mention = user.mention
        else:
            mention = name  # If user not found, use the name without mention
        message += f"{emoji} {mention}\n"

    message += "\n**DPS**:\n"
    for name in dps:
        # Get the class emoji for the name
        class_name = classes_sheet1[names_sheet1.index(name)]
        emoji_id = await utility.get_emoji_id(guild, class_name)
        if emoji_id:
            emoji = f"<:{class_name}:{emoji_id}>"
        else:
            emoji = f":{class_name}:"
        
        # Find the corresponding user in Balance and mention them
        user = discord.utils.get(guild.members, display_name=name)
        if user:
            mention = user.mention
        else:
            mention = name  # If user not found, use the name without mention
        message += f"{emoji} {mention}\n"

    await ctx.send(message)



@bot.command()
@utility.is_admin()
async def roster2(ctx):
    # Get the guild object
    guild = ctx.guild
    
    # Get the title from Sheet1 A1 cell and make it bigger in size
    title = runs.cell(1, 4).value.upper()

    # Get names and classes from Sheet1 from row 2 to row 17
    names_sheet1 = runs.col_values(4)[1:17]
    classes_sheet1 = runs.col_values(5)[1:17]

    # Separate names into different categories
    tanks = names_sheet1[:2]
    healers = names_sheet1[2:5]
    dps = names_sheet1[5:]

    # Format the message
    message = f"# {title}\n\n"
    message += "**Tank:**\n"
    for name in tanks:
        # Get the class emoji for the name
        class_name = classes_sheet1[names_sheet1.index(name)]
        emoji_id = await utility.get_emoji_id(guild, class_name)
        if emoji_id:
            emoji = f"<:{class_name}:{emoji_id}>"
        else:
            emoji = f":{class_name}:"
        
        # Find the corresponding user in Sheet2 and mention them
        user = discord.utils.get(guild.members, display_name=name)
        if user:
            mention = user.mention
        else:
            mention = name  # If user not found, use the name without mention
        message += f"{emoji} {mention}\n"

    message += "\n**Heal**:\n"
    for name in healers:
        # Get the class emoji for the name
        class_name = classes_sheet1[names_sheet1.index(name)]
        emoji_id = await utility.get_emoji_id(guild, class_name)
        if emoji_id:
            emoji = f"<:{class_name}:{emoji_id}>"
        else:
            emoji = f":{class_name}:"
        
        # Find the corresponding user in Sheet2 and mention them
        user = discord.utils.get(guild.members, display_name=name)
        if user:
            mention = user.mention
        else:
            mention = name  # If user not found, use the name without mention
        message += f"{emoji} {mention}\n"

    message += "\n**DPS**:\n"
    for name in dps:
        # Get the class emoji for the name
        class_name = classes_sheet1[names_sheet1.index(name)]
        emoji_id = await utility.get_emoji_id(guild, class_name)
        if emoji_id:
            emoji = f"<:{class_name}:{emoji_id}>"
        else:
            emoji = f":{class_name}:"
        
        # Find the corresponding user in Sheet2 and mention them
        user = discord.utils.get(guild.members, display_name=name)
        if user:
            mention = user.mention
        else:
            mention = name  # If user not found, use the name without mention
        message += f"{emoji} {mention}\n"

    await ctx.send(message)

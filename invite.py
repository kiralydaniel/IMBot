import utility
import discord

bot = utility.bot

spreadsheet = utility.spreadsheet

# Get Sheet1
runs = utility.sheet1

# Get Sheet2
balance = utility.sheet2


@bot.command()
@utility.is_admin()
async def inv1(ctx):
    # Get names from Sheet1 column A in rows 2-17
    names_sheet1 = runs.col_values(1)[1:17]

    inv_title = runs.cell(1, 1).value
    inv_horde = runs.cell(24, 2).value
    inv_alli = runs.cell(25, 2).value

    # Custom emoji for Horde and Alli
    horde_emoji = "<:horde:1239150579595477103>"
    alli_emoji = "<:alli:1239150577875685428>"

    for name in names_sheet1:
        if name:  # Check if the cell is not None
            try:
                # Find the corresponding row in Sheet2 column 4
                row = balance.findall(name, in_column=4)
                if row:
                    discord_name = balance.cell(row[0].row, 1).value
                    member = discord.utils.get(ctx.guild.members, name=discord_name)

                    if member:
                        # Create an embed message
                        embed = discord.Embed(
                            title=f"​{inv_title} IM Boost",
                            description=f"To copy the whisper just click on the right side of the box\n\n{horde_emoji} **Horde:** ```/w {inv_horde}-Ragnaros inv```\n{alli_emoji} **Alli:** ```/w {inv_alli}-Ragnaros inv```",
                            color=discord.Color.blue()
                        )

                        # Set server's icon as thumbnail for the guild
                        embed.set_thumbnail(url=ctx.guild.icon.url)

                        # Send the embedded message to the user
                        await member.send(embed=embed)
                    else:
                        print(f"Member with Discord name {discord_name} not found.")
                else:
                    print(f"Name {name} not found in Sheet2.")
            except Exception as e:
                print(f"Error: {e}")

    # Create an embed message for the notification
    embed_notification = discord.Embed(
        title="Invite Messages Sent",
        description="Messages have been sent to all users.",
        color=discord.Color.green()
    )

    # Set server's icon as thumbnail for notification
    embed_notification.set_thumbnail(url=ctx.guild.icon.url)

    # Send the embedded notification message to your Discord account in private
    await ctx.author.send(embed=embed_notification)


@bot.command()
@utility.is_admin()
async def inv2(ctx):
    # Get names from Sheet1 column A in rows 2-17
    names_sheet1 = runs.col_values(4)[1:17]

    inv_title = runs.cell(1, 4).value.upper()
    inv_horde = runs.cell(24, 5).value
    inv_alli = runs.cell(25, 5).value

    # Custom emoji for Horde and Alli
    horde_emoji = "<:horde:1239150579595477103>"
    alli_emoji = "<:alli:1239150577875685428>"

    for name in names_sheet1:
        if name:  # Check if the cell is not None
            try:
                # Find the corresponding row in Sheet2 column 4
                row = balance.findall(name, in_column=4)
                if row:
                    discord_name = balance.cell(row[0].row, 1).value
                    member = discord.utils.get(ctx.guild.members, name=discord_name)

                    if member:
                        # Create an embed message
                        embed = discord.Embed(
                            title=f"​{inv_title} IM Boost",
                            description=f"To copy the whisper just click on the right side of the box\n\n{horde_emoji} **Horde:** ```/w {inv_horde}-Ragnaros inv```\n{alli_emoji} **Alli:** ```/w {inv_alli}-Ragnaros inv```",
                            color=discord.Color.blue()
                        )

                        # Set server's icon as thumbnail for the guild
                        embed.set_thumbnail(url=ctx.guild.icon.url)

                        # Send the embedded message to the user
                        await member.send(embed=embed)
                    else:
                        print(f"Member with Discord name {discord_name} not found.")
                else:
                    print(f"Name {name} not found in Sheet2.")
            except Exception as e:
                print(f"Error: {e}")

    # Create an embed message for the notification
    embed_notification = discord.Embed(
        title="Invite Messages Sent",
        description="Messages have been sent to all users.",
        color=discord.Color.green()
    )

    # Set server's icon as thumbnail for notification
    embed_notification.set_thumbnail(url=ctx.guild.icon.url)

    # Send the embedded notification message to your Discord account in private
    await ctx.author.send(embed=embed_notification)

@bot.command()
@utility.is_admin()
async def invping1(ctx):
    # Get the guild object
    guild = ctx.guild
    
    # Get the title from Sheet1 A1 cell and make it bigger in size
    title = "INVITE"
    inv_horde = runs.cell(24,2).value
    inv_alli = runs.cell(25,2).value

    # Get names and classes from Sheet1 from row 2 to row 17
    names_sheet1 = runs.col_values(1)[1:17]
    classes_sheet1 = runs.col_values(2)[1:17]

    # Separate names into different categories
    tanks = names_sheet1[:2]
    healers = names_sheet1[2:5]
    dps = names_sheet1[5:]

    # Format the message
    message = f"# {title}\n\n"
    message += f"**Horde:** ```/w {inv_horde}-Ragnaros inv```\n"
    message += f"**Alli:** ```/w {inv_alli}-Ragnaros inv```\n\n"
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


@bot.command()
@utility.is_admin()
async def invping2(ctx):
    # Get the guild object
    guild = ctx.guild
    
    # Get the title from Sheet1 A1 cell and make it bigger in size
    title = "INVITE"
    inv_horde = runs.cell(24,5).value
    inv_alli = runs.cell(25,5).value

    # Get names and classes from Sheet1 from row 2 to row 17
    names_sheet1 = runs.col_values(4)[1:17]
    classes_sheet1 = runs.col_values(5)[1:17]

    # Separate names into different categories
    tanks = names_sheet1[:2]
    healers = names_sheet1[2:5]
    dps = names_sheet1[5:]

    # Format the message
    message = f"# {title}\n\n"
    message += f"**Horde:** ```/w {inv_horde}-Ragnaros inv```\n"
    message += f"**Alli:** ```/w {inv_alli}-Ragnaros inv```\n\n"
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

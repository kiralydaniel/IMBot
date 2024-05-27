import discord
import utility

bot = utility.bot

spreadsheet = utility.spreadsheet

# Get Sheet1
runs = utility.sheet1

# Get Sheet2
balance = utility.sheet2

message_store = {}

@bot.command()
@utility.is_admin()
async def roster(ctx, day: str, lb_count: int = 0):
    day = day.lower()
    
    if day not in utility.boost_days:
        await utility.send_invalid_argument_embed(ctx)
        return

    if day == "friday":
        title = runs.cell(1, 1).value.upper()
        names_sheet1 = runs.col_values(1)[1:19]
        classes_sheet1 = runs.col_values(2)[1:19]
    elif day == "saturday":
        title = runs.cell(1, 4).value.upper()
        names_sheet1 = runs.col_values(4)[1:19]
        classes_sheet1 = runs.col_values(5)[1:19]

    # Get the guild object
    guild = ctx.guild

    # Separate names into different categories and ignore empty names
    tanks = [name for name in names_sheet1[:2] if name]
    healers = [name for name in names_sheet1[2:5] if name]
    dps = [name for name in names_sheet1[5:] if name]

    # Adjust DPS and LB based on lb_count
    lb = []
    if lb_count > 0:
        lb = dps[-lb_count:]
        dps = dps[:-lb_count]

    # Format the message
    message = f"# {title}\n\n"
    message += "**Tank:**\n"
    for name in tanks:
        class_name = classes_sheet1[names_sheet1.index(name)]
        message += await utility.format_name_with_emoji(guild, name, class_name)

    message += "\n**Heal**:\n"
    for name in healers:
        class_name = classes_sheet1[names_sheet1.index(name)]
        message += await utility.format_name_with_emoji(guild, name, class_name)

    message += "\n**DPS**:\n"
    for name in dps:
        class_name = classes_sheet1[names_sheet1.index(name)]
        message += await utility.format_name_with_emoji(guild, name, class_name)

    if lb:
        message += "\n**LB**:\n"
        for name in lb:
            class_name = classes_sheet1[names_sheet1.index(name)]
            message += await utility.format_name_with_emoji(guild, name, class_name)

    # Send the message and store its ID
    sent_message = await ctx.send(message)
    message_store[(guild.id, ctx.channel.id)] = sent_message.id


@bot.command()
@utility.is_admin()
async def update_lb(ctx, day: str, lb_count: int):
    day = day.lower()

    if day not in utility.boost_days:
        await utility.send_invalid_argument_embed(ctx)
        return

    if day == "friday":
        names_sheet1 = runs.col_values(1)[1:19]  # Adjusted range to include 18 rows
        classes_sheet1 = runs.col_values(2)[1:19]  # Fetching class information
    elif day == "saturday":
        names_sheet1 = runs.col_values(4)[1:19]  # Adjusted range to include 18 rows
        classes_sheet1 = runs.col_values(5)[1:19]  # Fetching class information

    # Filter out empty names and get the last lb_count names and classes
    valid_data = [(name, class_name) for name, class_name in zip(names_sheet1, classes_sheet1) if name]
    lb_members = valid_data[-lb_count:]

    if not lb_members:
        await utility.send_embed_private(ctx, "No valid LB members found.")
        return

    # Call the update_roster_message function to update the message
    await update_roster_message(ctx.guild.id, ctx.channel.id, lb_members)
    await utility.send_embed_private(ctx, "LB members updated.")

async def update_roster_message(guild_id, channel_id, lb_members):
    message_id = message_store.get((guild_id, channel_id))
    if not message_id:
        return
    
    channel = bot.get_channel(channel_id)
    if not channel:
        return

    message = await channel.fetch_message(message_id)
    if not message:
        return

    # Find the LB section and remove it along with its content
    message_content = message.content
    lb_section_start = message_content.find("**LB**:")
    if lb_section_start != -1:
        # Remove everything from the start of the LB section till the end of the message
        message_content = message_content[:lb_section_start].rstrip()

    # Prepare the new LB section
    lb_section = "\n\n**LB**:\n" 
    for name, class_name in lb_members:
        lb_section += await utility.format_name_with_emoji(channel.guild, name, class_name)
    
    # Combine the content and the new LB section
    new_message_content = message_content + lb_section
    
    try:
        await message.edit(content=new_message_content)
    except Exception as e:
        print(f"Error updating message: {e}")

@bot.command()
@utility.is_admin()
async def reset_message_store(ctx):
    message_store.clear()
    await utility.send_embed_private(ctx, "Message store has been reset.")

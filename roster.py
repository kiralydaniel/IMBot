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
async def roster(ctx, day: str, lb_count: int = 0):
    day = day.lower()
    
    if day not in utility.boost_days:
        await utility.send_invalid_argument_embed(ctx)
        return

    if day == "friday":
        title = runs.cell(1, 1).value.upper()
        names_sheet1 = runs.col_values(1)[1:17]
        classes_sheet1 = runs.col_values(2)[1:17]
    elif day == "saturday":
        title = runs.cell(1, 4).value.upper()
        names_sheet1 = runs.col_values(4)[1:17]
        classes_sheet1 = runs.col_values(5)[1:17]


    # Get the guild object
    guild = ctx.guild

    # Separate names into different categories
    tanks = names_sheet1[:2]
    healers = names_sheet1[2:5]
    dps = names_sheet1[5:]

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

    await ctx.send(message)


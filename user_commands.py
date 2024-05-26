import utility
import locale
import discord


bot = utility.bot

spreadsheet = utility.spreadsheet

# Get Sheet1
runs = utility.sheet1

# Get Sheet2
balance = utility.sheet2



@bot.command()
async def b(ctx):
    # Get user's Discord name
    
    author_name = ctx.author.name

    # Find the row in the Google Sheets document corresponding to the user's Discord name
    name_column = balance.col_values(1)
    try:
        row_index = name_column.index(author_name) + 1
    except ValueError:
        await utility.send_embed_private("Your name was not found in Balance.")
        return

    # Retrieve the number from the adjacent cell in the same row
    number = balance.cell(row_index, 2).value

    if number is None:
        number = 0
    else:
        # Format the number with commas separating every thousand
        locale.setlocale(locale.LC_ALL, '')  # Set the locale to the user's default
        number = locale.format_string("%d", int(number), grouping=True)

    # Get the character name from Sheet2
    character_name = balance.cell(row_index, 3).value

    # Get the user associated with the command context
    user = ctx.author

    # Create an embed
    embed = discord.Embed(title="Balance", description=f'\nPayment character: **{character_name}**\nYour balance is: **{number} gold**', color=discord.Color.gold())

    # Set the user's profile picture as the thumbnail
    embed.set_thumbnail(url=user.avatar)  

    # Send the embed in a private message to the user
    await ctx.author.send(embed=embed)




@bot.command()
async def char(ctx, message):
    # Append "-Ragnaros" to the message
    message += "-Ragnaros"

    # Get user's Discord name
    author_name = ctx.author.name

    # Find the row in Sheet2 corresponding to the user's Discord name
    name_column = balance.col_values(1)
    try:
        row_index = name_column.index(author_name) + 1
    except ValueError:
        await utility.send_embed_private("Your name was not found in Balance.")
        return

    # Update the message in the third column of the same row
    balance.update_cell(row_index, 3, message)

    # Create an embed for the confirmation message
    embed = discord.Embed(title="Character Name Updated", color=discord.Color.green())
    embed.add_field(name="User", value=author_name, inline=False)
    embed.add_field(name="Payment Character Name", value=message, inline=False)

    # Set the user's profile picture as the thumbnail
    user = ctx.author
    embed.set_thumbnail(url=user.avatar)  

    # Send the embed message as a direct message to the user
    await ctx.author.send(embed=embed)
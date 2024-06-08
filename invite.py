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
async def inv(ctx, day: str):
    day = day.lower()

    if day not in utility.boost_days:
        await utility.send_invalid_argument_embed(ctx)
        return
    
    if day == "friday":
        # Get names from Sheet1 column A in rows 2-19
        names_sheet1 = runs.col_values(1)[1:19]

        inv_title = runs.cell(1, 1).value
        inv_horde = runs.cell(26, 2).value
        inv_alli = runs.cell(27, 2).value
    elif day == "saturday":
        # Get names from Sheet1 column A in rows 2-19
        names_sheet1 = runs.col_values(4)[1:19]

        inv_title = runs.cell(1, 4).value
        inv_horde = runs.cell(26, 5).value
        inv_alli = runs.cell(27, 5).value

    # Custom emoji for Horde and Alli
    horde_emoji = "<:horde:1239150579595477103>"
    alli_emoji = "<:alli:1239150577875685428>"

    not_found_names = []  # List to store names of members not found

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
                            title=f"{inv_title} IM Boost",
                            description=f"To copy the whisper just click on the right side of the box\n\n{horde_emoji} **Horde:** ```/w {inv_horde}-Ragnaros inv```\n{alli_emoji} **Alli:** ```/w {inv_alli}-Ragnaros inv```",
                            color=discord.Color.blue()
                        )

                        # Set server's icon as thumbnail for the guild
                        embed.set_thumbnail(url=ctx.guild.icon.url)

                        # Send the embedded message to the user
                        await member.send(embed=embed)
                    else:
                        not_found_names.append(discord_name)
                else:
                    print(f"Name {name} not found in Sheet2.")
            except Exception as e:
                print(f"Error: {e}")

    # Send a notification to the command sender if any members were not found
    if not_found_names:
        embed_not_found = discord.Embed(
            title="Members Not Found",
            description="\n".join(not_found_names),
            color=discord.Color.red()
        )
        await ctx.author.send(embed=embed_not_found)

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

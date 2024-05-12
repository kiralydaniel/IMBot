import os

import utility
import roster_update
import invite
import user_commands
import roster

# Discord bot setup with intents
bot = utility.bot

spreadsheet = utility.spreadsheet

# Get Sheet1
runs = utility.sheet1

# Get Sheet2
balance = utility.sheet2


# Fetch the bot token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if TOKEN is None:
    print("Error: Discord bot token not found. Make sure to set the 'DISCORD_BOT_TOKEN' environment variable.")
    exit(1)

# Run the bot
bot.run(TOKEN)
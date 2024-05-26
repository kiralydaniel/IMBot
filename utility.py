import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import logging

# Discord bot intents
intents = discord.Intents.all()

# Discord bot setup with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

spreadsheet = client.open('IMBoost')

# Get Sheet1
sheet1 = spreadsheet.worksheet('runs')

# Get Sheet2
sheet2 = spreadsheet.worksheet('balance')

# Valid arguments
boost_days = ["friday", "saturday"]


# Set up logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Define the file paths relative to the current directory
friday_txt_path = os.path.join(current_dir, 'data', 'friday.txt')
saturday_txt_path = os.path.join(current_dir, 'data', 'saturday.txt')

async def send_embed_private(ctx, message):
    embed = discord.Embed(description=message, color=discord.Color.gold())
    await ctx.author.send(embed=embed)

async def send_invalid_argument_embed(ctx):
    embed = discord.Embed(title="Invalid Argument", color=discord.Color.red())
    embed.add_field(name="Choose from the following arguments:", value="\n".join(boost_days))
    await ctx.author.send(embed=embed)

# Discord event to delete user's message after command completion
@bot.event
async def on_command_completion(ctx):
    await ctx.message.delete()

def is_admin():
    async def predicate(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)

async def get_emoji_id(guild, emoji_name):
    # Fetch all custom emojis in the guild
    emojis = await guild.fetch_emojis()
    
    # Search for the emoji by name
    for emoji in emojis:
        if emoji.name == emoji_name:
            return emoji.id
    
    # Return None if emoji is not found
    return None

async def format_name_with_emoji(guild, name, class_name):
    emoji_id = await get_emoji_id(guild, class_name)
    emoji = f"<:{class_name}:{emoji_id}>" if emoji_id else f":{class_name}:"
    user = discord.utils.get(guild.members, display_name=name)
    mention = user.mention if user else name
    return f"{emoji} {mention}\n"

def is_in_bot_channel():
    async def predicate(ctx):
        allowed_channel_names = ["bot"]  # List of allowed channel names
        return ctx.channel.name in allowed_channel_names
    return commands.check(predicate)

# Event listener for command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await send_embed_private(ctx, "This command can only be used in the **#bot** channel.")
        await ctx.message.delete()
    else:
        raise error
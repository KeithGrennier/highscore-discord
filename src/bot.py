#bot.py
import os

import discord
from discord import app_commands
from dotenv import load_dotenv
import commands
from helper_funcs import format_datetime_logger
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
# client = discord.Client(intents=discord.Intents())

@client.event
async def on_ready():
    # for guild in client.guilds:
    #     if guild.Name == GUILD:
    #         break
    await tree.sync(guild=discord.Object(id=GUILD))
    format_datetime_logger("Bot Started","info")

# Map commands
command_mapping = {
    "ping": commands.ping,
    #TODO HTTPException: 400 Bad Request (error code: 50006): Cannot send an empty message
    # occurs no matter what is input.
    "hs":commands.highscore, 
    # "other_command": other_command,
}
# Register commands
for name, command_function in command_mapping.items():
    tree.command(name=name, guild=discord.Object(GUILD))(command_function)

"""
# Test Command
@tree.command(
    name="ping",
    description="My first application Command",
    guild=discord.Object(GUILD)
)
async def ping(interaction):
    await interaction.response.send_message("Pong!")
"""
client.run(TOKEN)
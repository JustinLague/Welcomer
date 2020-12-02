import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_voice_state_update(member, before, after):
        cleanMemberName = member.name.split('#')[0]

        if after.channel is not None:
            guild = after.channel.guild
            message = cleanMemberName + " has joined " + after.channel.name
        
        if before.channel is not None:
            guild = before.channel.guild
            message = cleanMemberName + " has left " + before.channel.name

        try:
            welcomerChannel = [channel for channel in guild.text_channels if channel.name == "welcomer"][0]

        except:
            await guild.create_text_channel('welcomer')
            welcomerChannel = [channel for channel in guild.text_channels if channel.name == "welcomer"][0]

        await welcomerChannel.send(message)

bot.run(TOKEN)
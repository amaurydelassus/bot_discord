import os
import discord
from dotenv import load_dotenv
client = discord.Client()
load_dotenv(dotenv_path="config")
@client.event
async def on_redy():
    print("Le bot est prêt.")

@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong", delete_after = 5)\

@client.event
async def on_member_join(member):
    channel: discord.TextChannel = client.get_channel(89453321500753920)
    await channel.send(f"Bien venue a {member.display_name} !!")

client.run(os.getenv("TOKEN"))

import discord
import sys
import os
import dotenv

config = dotenv.load_dotenv(".env")
token = os.getenv("TOKEN")

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot is ready.")
    
@client.event
async def on_message(msg: discord.Message):
    if msg.author == client.user:
        return
    if msg.content.startswith("cmd!"):
        if msg.content == "cmd!help":
            await msg.channel.send("**__Help__**\n\
**?trello** - Get the link to the Trello board\n\
**?faq** - Answers to the most common questions\n\
**?links** - Links to the official group, the game's page\n")

client.run(token)

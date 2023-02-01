import discord
import sys
import os
import dotenv

config = dotenv.load_dotenv(".env")
token = os.getenv("TOKEN")

client = discord.Client(intents=discord.Intents.all())

prefix = "$"

latency = 0

@client.event
async def on_ready():
    print("Bot is ready.")
    
@client.event
async def on_message(msg: discord.Message):
    if msg.author == client.user:
        return
    if msg.content.__contains__("rockyuwu"):
        await msg.channel.send("rocky owner UwU.")

    if msg.content == f"{str(prefix)}ping":
        latency = client.latency
        await msg.channel.send(f"pong! :troll: \nlatency: {str(latency)} ms")

    if msg.content.startswith(str(prefix)):
        if msg.channel.name == "bot-cmds" or msg.author.guild_permissions.manage_messages:
            if msg.content == f"{str(prefix)}help":
                await msg.channel.send(f"**__Help__** \n    **{prefix}trello** - Get the link to the Trello board\n    **{prefix}faq** - Answers to the most common questions \n    **{prefix}links** - Links to the official group, the game's page\n")
            if msg.content == f"{str(prefix)}trello":
                await msg.channel.send("**trello link:** (none for now)")
            if msg.content == f"{str(prefix)}faq":
                await msg.channel.send("**FAQ:** (none for now)")
            if msg.content == f"{str(prefix)}links":
                await msg.channel.send("**links:** (none for now)")
    if msg.author.id == 291463810449932298 and msg.content.lower() == "bot, stop":
        await msg.channel.send("ok :(")
        sys.exit()

client.run(token)

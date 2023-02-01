import discord
from discord.ext import commands
import sys
import os
import dotenv

config = dotenv.load_dotenv(".env")
token = os.getenv("TOKEN")

client = commands.Bot(intents=discord.Intents.all(), command_prefix="$")

client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is ready.")
        
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You are missing a required argument.")
    else:
        await ctx.send(f"An error occured: {error}")
        
@client.command()
@commands.has_permissions(ban_members=True)
async def avadakedavra(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.mention}")

@client.command()
async def help(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        await ctx.send(f"**__Help__** \n    **$trello** - Get the link to the Trello board\n    **$faq** - Answers to the most common questions \n    **$links** - Links to the official group, the game's page\n    **$ping** - Pong!\n    **$help** - Shows this message \n*There's also a few easter eggs only for admins*")

@client.command()
async def trello(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        await ctx.send("**trello link:** (none for now)")

@client.command()
async def faq(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        await ctx.send("**FAQ:** (none for now)")

@client.command()
async def links(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        await ctx.send("**links:** (none for now)")

@client.command()
async def ping(ctx):
    latency = client.latency
    latency = str(latency)
    latency = latency[0:5]
    await ctx.send(f"pong! :troll: \nlatency: {str(latency)} ms")


@client.listen('on_message')
async def on_message(msg: discord.Message):
    if msg.author == client.user:
        return
    if msg.content.__contains__("rockyuwu"):
        await msg.channel.send("rocky owner UwU.")

    if msg.author.id == 291463810449932298 and msg.content.lower() == "bot, stop":
        await msg.channel.send("*ok :(*\n**shutting down...**")
        sys.exit()


client.run(token)

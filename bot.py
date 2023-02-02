#!/usr/bin/env python3

import discord
from discord.ext import commands
import openai
import os
import dotenv

config = dotenv.load_dotenv(".env")
token = os.getenv("TOKEN")
OPENAI_API_KEY = dotenv.get_key('.env', 'OPENAI_KEY')
ID = os.getenv("ID")
openai.api_key = OPENAI_API_KEY

model_engine = "text-davinci-003"
max_tokens = 2048

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
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
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
        await ctx.send(f"**__Help__** \n    **$trello** - Get the link to the Trello board\n    **$faq** - Answers to the most common questions \n    **$links** - Links to the official group, the game's page\n    **$ping** - Pong!\n *There's also a few easter eggs only for admins*")

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
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        latency = client.latency
        latency = str(latency)
        latency = latency[0:5]
        await ctx.send(f"pong!\nlatency: {str(latency)} ms")

@client.command()
async def ask(ctx: commands.context, *, question: str):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=question,
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        await ctx.send(response.choices[0].text)

@client.listen('on_message')
async def on_message(msg: discord.Message):
    if msg.author == client.user:
        return
    if msg.content.lower().__contains__("rockyuwu"):
        await msg.channel.send("rocky owner UwU.")

    if msg.content.lower().__contains__("ultima the goat".lower()):
        await msg.channel.send("He knows bru.")
    
    if msg.author.id == int(ID) and msg.content.lower() == "bot_stop":
        await msg.channel.send("*ok :(*\n**shutting down...**")
        await client.close()
    
    if msg.author.id == int(ID) and msg.content.lower() == "bot, stop":
        await msg.channel.send("*ok :(*\n**shutting down...**")
        await client.close()
    
    if msg.author.id == int(ID) and msg.content.lower() == "bot stop":
        await msg.channel.send("*ok :(*\n**shutting down...**")
        await client.close()

client.run(token)
print("Bot is offline.")

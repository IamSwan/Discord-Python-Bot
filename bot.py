#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import dotenv

config = dotenv.load_dotenv(".env")
token = os.getenv("TOKEN")
my_id = os.getenv("ID")
leg_id = os.getenv("LegendID")

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="$")

bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot is ready.")
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You are missing a required argument.")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    else:
        await ctx.send(f"An error occured: {error}")
        
@bot.command()
@commands.has_permissions(ban_members=True)
async def avadakedavra(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.mention}")

@bot.command()
async def help(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        await ctx.send(f"**__Help__** \n    **$trello** - Get the link to the Trello board\n    **$faq** - Answers to the most common questions \n    **$links** - Links to the official group, the game's page\n    **$ping** - Pong!\n *There's also a few easter eggs only for admins*")

@bot.command()
async def trello(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        await ctx.send("**trello link:** (none for now)")

@bot.command()
async def faq(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        await ctx.send("**FAQ:** (none for now)")

@bot.command()
async def links(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        await ctx.send("**links:** (none for now)")

@bot.command()
async def ping(ctx):
    if ctx.channel.name == "bot-cmds" or ctx.author.guild_permissions.manage_messages:
        latency = bot.latency
        latency = str(latency)
        latency = latency[0:5]
        await ctx.send(f"pong!\nlatency: {str(latency)} ms")

@bot.listen('on_message')
async def on_message(msg: discord.Message):
    if msg.author == bot.user:
        return
    if msg.content.lower().__contains__("rockyuwu"):
        await msg.channel.send("rocky owner UwU.")

    if msg.content.lower().__contains__("ultima the goat".lower()):
        await msg.channel.send("He knows bru.")
    
    if msg.author.id == int(my_id) and msg.content.lower() == "bot_stop":
        await msg.channel.send("*ok :(*\n**shutting down...**")
        await bot.close()
    
    if msg.author.id == int(my_id) and msg.content.lower() == "bot, stop":
        await msg.channel.send("*ok :(*\n**shutting down...**")
        await bot.close()
    
    if msg.author.id == int(my_id) and msg.content.lower() == "bot stop":
        await msg.channel.send("*ok :(*\n**shutting down...**")
        await bot.close()
    if msg.content.lower().__contains__("uwu"):
        await msg.channel.send("UwU daddy..")
    if msg.author.id == int(leg_id):
        await msg.reply("Stfu bozo")

bot.run(token)
print("Bot is offline.")

from email.policy import default
from http import client
from lib2to3.pgen2 import token
from multiprocessing import context
from pydoc import cli
from sys import prefix
from tkinter.messagebox import NO
from unicodedata import name
from attr import has
import discord
from discord.ext import commands
from numpy import true_divide
from setuptools import Command
from discord.ext.commands import Bot, has_permissions, CheckFailure, BadArgument
from discord import Member
import time

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.presences = True
client = discord.Client(intents=intents)

token = 'MTAzMDUyODM0MjkxNjYxMjEwNg.GjlU-e.Fcp80SdPTYIUWHtsjwhtSbDhw7pTECUZdpdktM'

client = commands.Bot(command_prefix='?', intents=intents)




@client.event
async def on_ready():
    print(f'Logged in as {client.user}')



@client.command()
async def test(ctx):
    await ctx.send(f'Hello, I am {client.user.display_name}')

logging = True
logschannel = 1030550553882800168


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
        reason = "You broke or broke multiple server rules, you have been kicked for now."
        await ctx.guild.kick(member)
        await ctx.send(f'User {member.mention} has been kicked for `{reason}`')
    else:
            await ctx.guild.kick(member)
            await ctx.send(f'User {member.mention} has been kicked for `{reason}`')
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason==None:
        reason = 'You broke or broke multiple server rules, you have been permantely banned`.'
        await ctx.guild.ban(member)
        await ctx.send(f'User {member.mention} has been banned for `{reason}')
    else:
            await ctx.guild.ban(member)
            await ctx.send(f'User {member.mention} has been banned for `{reason}`')

client.run(token)

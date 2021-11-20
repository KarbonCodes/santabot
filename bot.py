import discord
import youtube_dl
import music
from discord.ext import commands

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client )


client = commands.Bot(command_prefix = '.', intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Loading up toys!'))
    print('Santa is in the sleigh!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')








@client.command(aliases=['purge'])
async def clear(ctx, amount=11):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send('Unable to use command.')
        return
    amount = amount+1
    if amount > 21:
        await ctx.send('Cannot delete more than 20 messages.')
    else:
        await ctx.channel.purge(limit=amount)



@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason= None):
    await member.ban(reason=reason)


class music(commands.Cog):
    def __init__(self, client):
        self.client = client























































client.run('OTExNjQ0Mjg0MjUwMzYxODc2.YZkY5g.ux-yr59fxsG1Qp4TorToKK99ABc')

import discord
from discord.ext import commands

from get_quotes import get_random_quote  # Import the function to get quotes

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='/', intents=intents)

channel_id = 1379178030886420510

@bot.command(name="Motivation")
async def motivate(ctx, *, issue: str = None):
    if ctx.author.bot or ctx.channel.id == channel_id:
        if not issue:
            await ctx.send("Tell me what’s wrong, e.g., `like I feel stressed`")
            return

        issue = issue.lower()
        quote = get_random_quote(issue)

        await ctx.send(f"{ctx.author.mention} {quote}")


bot.run("MTM3OTA2OTAyNjIxMDI4MzU0MQ.Gkihrz.RaSo7mTb1Bw2lns0muRPlyLnxr9yhEodg3JO_Q")
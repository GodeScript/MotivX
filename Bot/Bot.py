import discord
from discord.ext import commands

from bot_token import token  # Import the bot token from bot_token.py
from Get_AiQuotes import generate_quote  # Import the function to get quotes

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='/', intents=intents)

channel_id = 1379178030886420510

@bot.command(name="mt")
async def motivate(ctx, *, issue: str = None):
    if ctx.author.bot or ctx.channel.id == channel_id:
        if not issue:
            await ctx.send("Tell me what’s wrong, e.g., `like I feel stressed`")
            return

        issue = issue.lower()
        quote = generate_quote(issue)

        await ctx.send(f"{ctx.author.mention} {quote}")


bot.run(token)  # Replace with your bot token
import discord
from discord.ext import commands
import asyncio  # Für die Verzögerung beim Löschen

from Bot.Commands.MotivasionalQuotes.Get_AiQuotes import generate_quote
from Bot.database import is_allowed

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.tree.command(name="mt", description="Get a motivational quote!")
async def motivate(interaction: discord.Interaction, issue: str = None):
    # Prüfe, ob der Befehl im richtigen Kanal ausgeführt wird
    if not is_allowed(interaction.channel.id):

        # Sende eine Warnung und lösche sie nach 10 Sekunden
        warning_msg = await interaction.response.send_message(
            "❌ It seems you are not allowed to use this command in this channel. Or this Server is not a customer from MotivX if there is any Problem then Conntect the Support link in Bot Bio.",
            ephemeral=False  # Falls "True", sieht nur der Sender die Nachricht
        )
        
        # Lösche die Warnung nach 10 Sekunden
        await asyncio.sleep(10)
        await interaction.delete_original_response()
        return warning_msg
    
    # Falls kein Thema angegeben wurde
    if not issue:
        await interaction.response.send_message(
            "Tell me what’s wrong, e.g., `I feel stressed`",
            ephemeral=True  # Nur der Sender sieht dies
        )
        return
    
    # Generiere und sende das Zitat
    issue = issue.lower()
    quote = generate_quote(issue)
    await interaction.response.send_message(f"{interaction.user.mention} {quote}")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot is ready as {bot.user.name}")

def run_bot(token):
    bot.run(token)
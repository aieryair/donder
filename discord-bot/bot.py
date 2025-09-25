import os
from dotenv import load_dotenv
from nextcord import Intents, Embed, Interaction
from nextcord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TEST_GUILDS = [int(guild_id) for guild_id in os.getenv("TEST_GUILDS").split(",")]

intents = Intents.default()
bot = Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command(name="test",description="Send a test message", guild_ids=TEST_GUILDS)
async def test(interaction: Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}! You're in Guild **{interaction.guild.name}** id: {interaction.guild.id}")

    
bot.run(TOKEN)

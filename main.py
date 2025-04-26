import discord
from discord.ext import commands
from discord import app_commands

# Intents and bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your Discord token
TOKEN = ""
with open("./token.txt", "r") as f:
    TOKEN = f.read()
# Replace with the ID of the channel where you want to send the messages
TARGET_CHANNEL_ID = 1365027231830905024

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        await bot.tree.sync()  # Sync commands to Discord
        print("Slash commands synced!")
    except Exception as e:
        print(f"Error syncing slash commands: {e}")

@bot.tree.command(name="suggest", description="Send a suggestion to #Suggestion-Log channel.")
async def send_message(interaction: discord.Interaction, message: str):
    """Slash command to send a message and add voting emojis."""
    target_channel = bot.get_channel(TARGET_CHANNEL_ID)
    if target_channel:
        sent_message = await target_channel.send(message)
        await sent_message.add_reaction("👍")  # Up emoji
        await sent_message.add_reaction("👎")  # Down emoji
        await interaction.response.send_message(f"Message sent to {target_channel.name}!", ephemeral=True)
    else:
        await interaction.response.send_message("Failed to find the target channel.", ephemeral=True)

# Run the bot
bot.run(TOKEN)

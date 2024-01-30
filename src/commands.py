# commands/ping_command.py
import highscores

async def ping(interaction):
    await interaction.response.send_message("Pong!")

async def highscore(interaction):
    await interaction.response.send_message(highscores.new_score(interaction))
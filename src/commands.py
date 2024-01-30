# commands/ping_command.py
import highscores_v1

async def ping(interaction):
    await interaction.response.send_message("Pong!")

async def highscore(interaction):
    await interaction.response.send_message(highscores_v1.new_score(interaction))
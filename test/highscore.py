import json
from datetime import datetime

file_path='test'
player_db='test\players.json'
highscores_filename = "test\scores copy.json"
history_filename = "test\history.json"
output_filename= "test\output.txt"
# Get the current date and time
current_datetime = datetime.now()

# Format the date and time as YYYY-MM-DD HH:MM
global_timestamp = current_datetime.strftime('%Y-%m-%d %H:%M')

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def write_top_10(filename,data,time_stamp):
    response=''
    with open(filename,'w') as f:
        reponse=time_stamp+'\n'
        f.write(time_stamp+'\n')
        for x in data.get('Top 10',''): 
            f.write(f"{x['Rank']}. {x['Code']} {x['Score']}\n")
            reponse+=(f"{x['Rank']}. {x['Code']} {x['Score']}\n")
    return response

def update_highscores(current_highscores, new_score,player_code):
    # input from current highscores and info for potential highscore

    #Iterate over current Highscores and add potential highscore
    # Create tuple of Code,Score for the current highscore
    # add the tupple of potential high score
    # all scores is a tuple
    all_scores = [(entry['Code'], int(entry["Score"])) for entry in current_highscores] + [(player_code,int(new_score))]
    # Now sort by the tuple[1] aka score, don't reverse sort by score, this creates a new list
    # sorted scores is a list
    sorted_scores = sorted(all_scores, key=lambda x: x[1],reverse=False) 

    # Take the first/top 10 scores
    top_10 = sorted_scores[:10]
    # Rewrite scores
    update_highscores_data=[{'Code': code, 'Score': score} for code, score in top_10]
    return update_highscores_data
def get_top_ten(data)->list:
    # Check if JSON has 'Top 10'
    if "Top 10" not in data:
        data["Top 10"] = []
    # Get data in 'Top 10'
    return data["Top 10"]
def update_data(data, new_score, player_code):
    current_highscores = get_top_ten(data)
    # Logic to update scores
    if current_highscores:
        updated_highscores = update_highscores(current_highscores, new_score,player_code)
        # Update the highscores for the given player
        for i in range(len(updated_highscores)):
        # GPT
            entry = updated_highscores[i]
            player_code = entry['Code']
            score = str(entry['Score'])
            current_highscores[i]=({"Rank": i + 1, "Code": player_code, "Score": score})

        return data
    return None

def find_player(discord_name):
    player_info=load_data(player_db)
    
    for player in player_info["players"]:
        # TODO write logic if same initials???

        # or is for if I am lazy and want to just type in the initials
        if player["discord_name"].lower() == discord_name or player["three_initials"].lower()==discord_name:
            return player["three_initials"]
   
def update_scores(player_code:str,new_score:int,in_file:str)-> str:

    # Check if User in Database
    highscores_data = load_data(in_file)
    updated_highscores_data = update_data(highscores_data, new_score, player_code)

    if updated_highscores_data:
        save_data(in_file, updated_highscores_data)
        return output_filename,updated_highscores_data
    return None

def update_global_highscore(player_name:str,new_score:int)-> str:
    player_code=find_player(player_name)
    # print(player_code)
    response=update_scores(player_code,new_score,highscores_filename)
    if response:
        # print(response)
        file_destination,update_global_hiscords=response
        response=write_top_10(file_destination,update_global_hiscords,(global_timestamp))
        return response

# def update_personal_highscore(player_code:str,new_score:int)-> str:
#     player_code=find_player(player_code)
#     player_file=f'{file_path}\{player_code}'
#     response=update_scores(player_code,new_score,player_file)
#     if response:
#         file_destination,update_global_hiscords=response
#         response=write_top_10(file_destination,update_global_hiscords,global_timestamp)
#         return response
player='ahobbo'
score=141
update_global_highscore(player.lower(),score)
# update_personal_highscore(player,score)

import json
from datetime import datetime
from collections import defaultdict

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

def write_output(filename,data,funny_line):
    with open(filename,'w') as f:
        f.write(funny_line)
        for x in data.get('Top 10',''): 
            f.write(f"{x['Rank']}. {x['Code']} {x['Score']}\n")

def write_date():
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time as YYYY-MM-DD HH:MM
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M')
    return formatted_datetime
def update_highscores(current_highscores, new_score,player_code):
    all_scores = [(entry['Code'], int(entry["Score"])) for entry in current_highscores] + [(player_code,int(new_score))]
    sorted_scores = sorted(all_scores, key=lambda x: x[1],reverse=False)
    
    # # # Empty list to append scores
    # # top_10 = []

    # # for player_name,score in sorted_scores:
    # #     top_10.append({'Code':player_name,'Score':score})

    # #     if len(top_10) == 10:
    # #         print(top_10)
    # #         break

    # return top_10
        # Sort the scores in descending order
    # sorted_scores = sorted(all_scores, key=lambda x: x[1], reverse=True)

    # Take the top 10 scores
    top_10 = sorted_scores[:10]
    update_highscores_data=[{'Code': code, 'Score': score} for code, score in top_10]
    return update_highscores_data
"""
    print(all_scores)
    print(sorted_scores)
"""
def update_data(data, new_score, player_code):
    # Check if JSON has 'Top 10'
    if "Top 10" not in data:
        data["Top 10"] = []
    # Get data in 'Top 10'
    current_highscores = data["Top 10"]

    # Logic to update scores
    updated_highscores = update_highscores(current_highscores, new_score,player_code)

    # Check if the player has been uploading a lot of new highscores
    #TODO use history.json for this, maybe extract this into seperate function
    player_upload_count = defaultdict(int)
    for entry in current_highscores:
        player_upload_count[entry["Code"]] += 1

    player_upload_count[player_code] += 1

    # Store historical data only if the score is updated
    # List comprehension to convert Score to int
    # Check if both current_highscores and updated_highscores are not empty
    # TODO Whats the point in checking scores.json and hiscores.json?
    # TODO THIS IS BREAKING
    # if updated_highscores != [int(entry["Score"]) for entry in current_highscores]:
    #     data["Historical Data"] = data.get("Historical Data", [])
    #     current_datetime = datetime.now()
    #     formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M')

    #     data["Historical Data"].append({
    #         "Player Code": player_code,
    #         "New Highscores Uploaded": player_upload_count[player_code],
    #         "Timestamp": formatted_datetime
    #     })

    # # Update the highscores for the given player
    for i in range(len(updated_highscores)):
    # GPT
        entry = updated_highscores[i]
        player_code = entry['Code']
        score = str(entry['Score'])
        data["Top 10"][i]=({"Rank": i + 1, "Code": player_code, "Score": score})

    return data

# def historical_count(input_file,player_code):
#     input_file_data=load_data(input_file)
#     input_file_data["Historical Data"] = input_file_data.get("Historical Data", [])
    
#     fiend_level=1
#     for entry in (list(input_file_data["Historical Data"])):
#         if player_code == entry.get('Player Code'):
#             fiend_level += 1
#         else:
#             break
            



# Example usage:
highscores_filename = "src\scores.json"
history_filename = "src\history.json"
output_filename= "src\output.txt"
highscores_data = load_data(highscores_filename)

player_code = "MMT"  # Replace with the actual player code
new_score = 167  # Replace with the actual new score


updated_highscores_data = update_data(highscores_data, new_score, player_code)
save_data(highscores_filename, updated_highscores_data)
# print(updated_highscores_data)
#TODO do 
#TODO 'BETTER LUCK NEXT TIME IDIOT'
current_time=write_date()
funny_line=(f'Last Updated {current_time}\nTop 10\n')
write_output(output_filename,updated_highscores_data,funny_line)

# Now, save the historical data (only if the score is updated)
# if "Historical Data" in updated_highscores_data:
#     history_data = load_data(history_filename)
#     history_data["Historical Data"] = history_data.get("Historical Data", []) + updated_highscores_data["Historical Data"]
#     save_data(history_filename, history_data)
# historical_count(history_filename,player_code)
import json
import os
from helper_funcs import validate_initials,validate_scores,format_datetime_logger

# TODO Refactor JSON
def read_data():
    file_path='src\scores.json'
    
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
            try:
                data=json.load(file)
                return parse_scores(data)
            except json.JSONDecodeError:
                return None
    else:
        return None

# Checks for Valid Initials and Score is integer less than 1000 and more than 0.
def parse_scores(input):
    error_msg=""
    for i in (input['Top 10']):
        initials=i["Code"]
        score=i["Score"]
        if not(validate_scores(score) and validate_initials(initials)):
            error_msg += f"Error in scores.json, {i}."
            format_datetime_logger(error_msg,'error')
    if error_msg:
        return error_msg
    else:
        # TODO go to next step to check if new score is within bounds of top and bottom.
        return print("Worked?")

def new_score(user_input:str)->str:
    output=''
    # Check if user input is valid format first
    try:
        
        user_input_check=user_input.strip()
    except AttributeError:
        return None
    if user_input_check<2 and user_input_check>=0:
        validate_scores(user_input_check[0])
        validate_initials(user_input_check[1])
    read_data()
    return output

read_data()
print(len("kmga"))
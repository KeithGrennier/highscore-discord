import logging

#Logging config
logging.basicConfig(filename='error_log.log', filemode='w+', format='%(asctime)s %(message)s', level=logging.INFO)

def validate_scores(number:str):
    try:
        number=int(number)
        if 0<number<1000:
            return True
        else:
            False
    except ValueError:
        return None
def validate_initials(letters:str) -> bool:
    char_len=len(letters)
    if 0<=char_len and char_len<4:
        return True
    else:
        return False
def format_datetime_logger(error_found,err_type) -> None:
    error_msg=error_found
    log_msg=f"{error_msg}\n"
    if err_type=='error'.lower():
        logging.error(log_msg)
    elif err_type=='info'.lower():
        logging.info(log_msg)
    return None
def verify_user_two_input(user_input):
    user_input=user_input.split(' ')
    if (0<len(user_input)<=2) and isinstance(user_input,list):
        # Is list between 1 and 2
        pass
    else:
        response=("invalid input")
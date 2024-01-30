import highscore
import helper_funcs

user='171 MMT'

user=user.split(' ')
if (0<len(user)<=2) and isinstance(user,list):
    # Is list between 1 and 2
    pass
else:
    response=("invalid input")
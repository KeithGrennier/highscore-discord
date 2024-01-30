import highscore
import helper_funcs

user='173 MMT'

user=user.split(' ')
if (0<len(user)<=2) and isinstance(user,list):
    # Is list between 1 and 2
    pass
else:
    response=("invalid input")

print(helper_funcs.validate_initials(user[1]))
print(helper_funcs.validate_scores(user[0]))
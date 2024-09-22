# checks that the user has entered a valid response within a specific list.
# also checks user input according to num_letters
def choice_checker(question, valid_list, allow_exit=False):
    # error code
    if len(valid_list) == 2:
        error = f"\nERROR - INVALID INPUT!\nPlease choose either '{valid_list[0]}' or '{valid_list[1]}'."
    else:
        error = '\nERROR - INVALID INPUT!\nPlease choose from:'
        for i in valid_list:
            error += f'\n- {i}'
        error += '.'

    while True:
        # Ask the user if they have played before
        response = input(question).lower()

        # exit code
        if response == 'xxx' and allow_exit is True:
            return response

        # If they say yes, output 'program continues'
        for i in valid_list:
            i_lowered = i.lower()
            if response == i_lowered[:1] or response == i_lowered:
                return i

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"\033[1m{error}\n\033[0m")


user_choices = ['Area', 'Perimeter']
shapes = ['Triangle', 'Square', 'Circle']
while True:
    user_choice = choice_checker("Choose area or perimeter... ", user_choices)
    print(user_choice)

    shape_choice = choice_checker("Choose shape... ", shapes)
    print(shape_choice)
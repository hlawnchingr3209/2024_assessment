# checks that the user has entered a valid response within a specific list.
# also checks user input according to num_letters
def choice_checker(question, valid_list):
    # error code
    if len(valid_list) == 2:
        error = f"Please choose either '{valid_list[0]}' or '{valid_list[1]}'."
    else:
        error = f"Please choose either '{valid_list[0]}', '{valid_list[1]}', or '{valid_list[2]}."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for i in valid_list:
            if response == i[:1] or response == i:
                return i

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


user_choices = ['area', 'perimeter']
shapes = ['triangle', 'square', 'circle']
while True:
    user_choice = choice_checker("Choose area or perimeter... ", user_choices)
    print(user_choice)

    shape_choice = choice_checker("Choose shape... ", shapes)
    print(shape_choice)
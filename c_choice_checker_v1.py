# checks that the user has entered a valid response within a specific list.
# also checks user input according to num_letters
def choice_checker(question, valid_list):
    # error code
    error = f"Please choose either '{valid_list[0]}' or '{valid_list[1]}'."

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
while True:
    user_choice = choice_checker("Choose area or perimeter... ", user_choices)
    print(user_choice)
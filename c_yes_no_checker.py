# very basic yes no checker.
def yes_no_checker(question):
    # error code
    error = f"Please choose either 'yes' or 'no'."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, return 'yes'
        if response == 'yes' or response == 'y':
            return 'yes'

        # If they say no, output return 'no'
        if response == 'no' or response == 'n':
            return 'no'

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}")


while True:
    user_choice = yes_no_checker("Have you used this program before? ")
    print(user_choice)

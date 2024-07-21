# shows instructions
def show_instructions():
    print('''\n
***** Instructions *****

 **********************''')


# function checks that the users input is not blank
def not_blank(question):
    while True:
        response = input(question).strip()

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this can't be blank or contain only spaces. Please try again.")
        else:
            return response


# number checker to check for decimal numbers.
def num_checker(question):
    while True:
        try:
            # asks user the question and converts to float to allow for decimals
            response = float(input(question))
            return response

        # if the user inputs something wrong like a string it prints errors
        except ValueError:
            print("Please enter a valid number.")
            continue


# checks that the user has entered a valid response within a specific list.
# also checks user input according to num_letters
def choice_checker(question, valid_list):
    # error code

    # if the list has two items uses correct grammar.
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



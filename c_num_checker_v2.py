# number checker used within calculators to check for validity of user inputs
def num_checker(question, mode, upper_boundary=None):
    while True:
        response = input(question)

        # If response is an empty string or xxx, return it
        if response == "" or response == 'xxx':
            return response

        try:
            # Attempt to convert response to the specified mode (e.g., int or float)
            response = mode(response)

            # Check if response is within the specified boundaries
            if response < 0:
                # Show an error message if it's not above 0
                error = f'\nERROR - INVALID NUMBER!\nPlease enter a number that is more than 0'
                print(error)
                continue

            elif upper_boundary is not None and response > upper_boundary:
                error = f'\nERROR - INVALID NUMBER!\nPlease enter a number that is more than 0 and less ' \
                        f'than {upper_boundary}'
                print(error)
                continue
            else:
                # Return the valid response
                return response

        # Catch value errors
        except ValueError:
            error = f"\nERROR - INVALID INPUT:\nPlease enter an INTEGER that is more than 0 and less than " \
                    f"{upper_boundary}"
            print(error)
            continue


while True:
    user_number = num_checker("What is your number? ", int)
    print(user_number)

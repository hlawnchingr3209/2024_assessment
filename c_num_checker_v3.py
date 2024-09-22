# number checker used within calculators to check for validity of user inputs
def num_checker(question, mode, upper_boundary=None, allow_enter=False):
    while True:
        response = input(question)

        # If response is an empty string or xxx, return it
        if allow_enter is True:
            if response == "" or response == 'xxx':
                return response

        try:
            # Attempt to convert response to the specified mode (e.g., int or float)
            response = mode(response)

            # Check if response is within the specified boundaries
            if response < 0:
                # Show an error message if it's not above 0
                print(f'\n\033[1mERROR - INVALID NUMBER!\nPlease enter a number that is more than 0.\n\033[0m\n')
                continue

            elif upper_boundary is not None and response > upper_boundary:
                print(f'\n\033[1mERROR - INVALID NUMBER!\nPlease enter a number that is more than 0 and less '
                      f'than {upper_boundary}.\n\033[0m')
                continue
            else:
                # Return the valid response
                return response

        # Catch value errors
        except ValueError:
            print(f"\n\033[1mERROR - INVALID INPUT:\nPlease enter an INTEGER that is more than 0 and less than "
                  f"{upper_boundary}.\n\033[0m")
            continue

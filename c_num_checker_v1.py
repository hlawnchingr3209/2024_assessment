# Simple number checker to check for decimal numbers.
def num_checker(question):
    while True:
        try:
            response = float(input(question))

            if 50 >= response >= 1:
                # Attempt to convert the response to a float
                return response
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid number.")
            continue


while True:
    user_number = num_checker("What is your number? ")
    print(user_number)

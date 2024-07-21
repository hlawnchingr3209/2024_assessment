# Simple number checker to check for decimal numbers.
def num_checker(question):
    while True:
        try:
            response = float(input(question))

            # Attempt to convert the response to a float
            return response
        except ValueError:
            print("Please enter a valid number.")
            continue


while True:
    user_number = num_checker("What is your number? ")
    print(user_number)

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


def shape_calculations(shape, mode):
    if shape == 'square':
        side_1 = num_checker("What is the length of Side 1? ")
        side_2 = num_checker("What is the length of Side 2? ")

        p_formula = side_1 + side_2
        a_formula = side_1 * side_2

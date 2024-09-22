from math import sqrt


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


# function does shape calculatons for area and perimeter, according to the type of shape
def shape_calculator(shape):
    # Initialize variables to store perimeter and area formulas
    p_calculated = 0
    a_calculated = 0

    # Check if the shape is a square
    if shape == 'Square':
        # Prompt the user to enter the length of a side
        side_1 = num_checker("What is the length of one of the sides? ", float)
        # Calculate the perimeter (P = 4 * side) and the area (A = side^2)
        p_calculated = side_1 * 4
        a_calculated = side_1 * side_1

    # Check if the shape is a rectangle
    elif shape == 'Rectangle':
        # Prompt the user to enter the lengths of two sides
        side_1 = num_checker("What is the length of Side 1? ", float)
        side_2 = num_checker("What is the length of Side 2? ", float)

        # Calculate the perimeter (P = 2*(side_1 + side_2)) and the area (A = side_1 * side_2)
        p_calculated = 2 * (side_1 + side_2)
        a_calculated = side_1 * side_2

        # checks if rectangle is actually a square
        if sqrt(a_calculated) == side_1:
            print("\n\033[1mp.s. your shape is a SQUARE.\033[0m")

    # Check if the shape is a triangle
    elif shape == 'Triangle':
        while True:
            # Prompt the user to enter the lengths of the three sides
            side_1 = num_checker("What is the length of Side 1? ", float)
            side_2 = num_checker("What is the length of Side 2? ", float)
            side_3 = num_checker("What is the length of Side 3? ", float)

            # Calculate the perimeter (P = side_1 + side_2 + side_3)
            p_calculated = side_1 + side_2 + side_3
            # Use Heron's formula to calculate the area
            sp_value = p_calculated / 2  # Semi-perimeter (s = P/2)

            # error handling for triangle
            try:
                a_calculated = sqrt(sp_value * (sp_value - side_1) * (sp_value - side_2) * (sp_value - side_3))
                # if area is 0 (invalid triangle raise a value error so that it can prompt the error catching code)
                if a_calculated == 0:
                    raise ValueError

                else:
                    break

            except ValueError:
                print("\n\033[1mERROR - INVALID DIMENSIONS:")
                print('Your Triangle has invalid dimensions, please try again!\n\033[0m')
                continue

    elif shape == 'Circle':
        # Prompt the user to enter the radius of the circle
        radius = num_checker("What is the radius of the circle? ", float)

        # calculate the perimeter (2 * pi * radius) and area
        p_calculated = 3.14159 * 2 * radius
        a_calculated = 3.14159 * radius * radius

    # Format the perimeter and area values to 2 decimal places
    p_calculated = f'{p_calculated:.2f}'
    a_calculated = f'{a_calculated:.2f}'

    # Return the formatted perimeter and area values
    return p_calculated, a_calculated

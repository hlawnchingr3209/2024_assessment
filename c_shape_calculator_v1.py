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


# function does shape calculatons for area and perimeter, according to the type of shape
def shape_calculator(shape):
    # Initialize variables to store perimeter and area formulas
    p_calculated = 0
    a_calculated = 0

    # Check if the shape is a square
    if shape == 'square':
        # Prompt the user to enter the length of a side
        side_1 = num_checker("What is the length of one of the sides? ", float)
        # Calculate the perimeter (P = 4 * side) and the area (A = side^2)
        p_calculated = side_1 * 4
        a_calculated = side_1 * side_1

    # Check if the shape is a rectangle
    elif shape == 'rectangle':
        # Prompt the user to enter the lengths of two sides
        side_1 = num_checker("What is the length of Side 1? ", float)
        side_2 = num_checker("What is the length of Side 2? ", float)

        # Calculate the perimeter (P = 2*(side_1 + side_2)) and the area (A = side_1 * side_2)
        p_calculated = 2 * (side_1 + side_2)
        a_calculated = side_1 * side_2

    # Check if the shape is a triangle
    elif shape == 'triangle':
        # Prompt the user to enter the lengths of the three sides
        side_1 = num_checker("What is the length of Side 1? ", float)
        side_2 = num_checker("What is the length of Side 2? ", float)
        side_3 = num_checker("What is the length of Side 3? ", float)

        # Calculate the perimeter (P = side_1 + side_2 + side_3)
        p_calculated = side_1 + side_2 + side_3
        # Use Heron's formula to calculate the area
        sp_value = p_calculated / 2  # Semi-perimeter (s = P/2)
        a_calculated = sqrt(sp_value * (sp_value - side_1) * (sp_value - side_2) * (sp_value - side_3))

    elif shape == 'circle':
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


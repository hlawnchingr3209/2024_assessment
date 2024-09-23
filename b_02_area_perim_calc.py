from math import sqrt
import pandas
from datetime import datetime


# shows instructions
def display_instructions():
    print()
    print("To use this Area/Perimeter Calculator, first choose the shape you want to calculate: square, rectangle,\n"
          "circle, or triangle. For each shape, you will be prompted to enter specific dimensions. The calculator\n"
          "will then display the calculated area and perimeter for the shape. You can continue calculating until you\n"
          "reach the maximum number of calculations allowed or exit the program by entering 'xxx' at any prompt. The\n"
          "results can be saved to a file if you perform two or more calculations.")
    print()


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


# checks that the user has entered a valid response within a specific list.
# also checks user input according to num_letters
def choice_checker(question, valid_list, allow_exit=False):
    # error code
    if len(valid_list) == 2:
        error = f"\nERROR - INVALID INPUT!\nPlease choose either '{valid_list[0]}' or '{valid_list[1]}'."
    else:
        error = '\nERROR - INVALID INPUT!\nPlease choose from:'
        for i in valid_list:
            error += f'\n- {i}'
        error += '.'

    while True:
        # Ask the user if they have played before
        response = input(question).lower()

        # exit code
        if response == 'xxx' and allow_exit is True:
            return response

        # If they say yes, output 'program continues'
        for i in valid_list:
            i_lowered = i.lower()
            if response == i_lowered[:1] or response == i_lowered:
                return i

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


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


# Function retrieves lists to be used in save file and converted with pandas
def save_calculations():
    # Create a dictionary to store the calculation data
    calculations_dict = {
        "Shape": shape_data_list,
        "Area": area_data_list,
        "  Perimeter": perimeter_data_list
    }

    # Convert the dictionary to a pandas DataFrame
    calculations_frame = pandas.DataFrame(calculations_dict)

    # Adjust the DataFrame index to start from 1
    calculations_frame.index += 1

    # *** Get current date for heading and filename ***
    today = datetime.now()  # current date and time

    # Format the day, month, and year as strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    # Create the DataFrame name and heading using the current date
    print()
    dataframe_name = f"Roney's Area and Perimeter Calculator ({day}_{month}_{year})"
    print("Calculator Stats")

    # Convert the DataFrame to a string representation
    calculations_txt = pandas.DataFrame.to_string(calculations_frame)

    # List of items to write to the text file
    to_write = [dataframe_name, calculations_txt]

    # Create a text file with the DataFrame name and add a .txt extension
    file_name = f"{dataframe_name}.txt"
    text_file = open(file_name, "w+")

    # Write each item in the list to the text file with double newlines between items
    for item in to_write:
        item = f"{item}"
        text_file.write(item)
        text_file.write("\n\n")

    # Print each item
    for item in to_write:
        print(item)
        print()


# Main Routine
calculator_mode = ''
attempted_calculations = 0

# lists for choice_checker
yes_no_list = ['yes', 'no']
shapes_list = ['square', 'rectangle', 'circle', 'triangle']

# lists for pandas
shape_data_list = []
area_data_list = []
perimeter_data_list = []

# greets user
print("Welcome To Roney's Area/Perimeter Calculator")

# Ask if user has used calculator before, if not display instructions.
used_before = choice_checker("Have you used this calculator before? ", yes_no_list)
if used_before == 'no':
    display_instructions()

# Ask user for amount of calculations allowed, initialise accordingly for other responses
maximum_calculations = num_checker("Maximum calculations allowed (<enter> for infinite)... ", int)
if maximum_calculations == '':
    calculator_mode = "infinite"

elif maximum_calculations == 'xxx':
    print("Thank you for using the calculator!")
    exit()

while True:

    if calculator_mode != 'infinite' and attempted_calculations == maximum_calculations:
        break

    attempted_calculations += 1

    # Calculation Heading
    print()
    if calculator_mode == 'infinite':
        calculation_heading = f"Infinite mode: Calculation {attempted_calculations}"

    else:
        calculation_heading = f"Limited Calculations: {attempted_calculations} / {maximum_calculations}"
    print(calculation_heading)

    user_shape = choice_checker("What shape would you like to calculate? ", shapes_list, True)
    if user_shape == 'xxx':
        break
    user_shape_perimeter, user_shape_area = shape_calculator(user_shape)
    print(f'\nCalculator Results:\n- Perimeter of your {user_shape} is {user_shape_perimeter}\n'
          f'- Area of your {user_shape} is {user_shape_area}')

    # add shape, and calculator results to lists
    shape_data_list.append(user_shape)
    area_data_list.append(user_shape_area)
    perimeter_data_list.append(user_shape_perimeter)

if attempted_calculations >= 2:
    save_calculations()
else:
    "Thank you for using the calculator!"
    exit()

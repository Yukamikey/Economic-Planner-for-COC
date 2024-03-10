import  numpy as np

def find_mean_list(dataset: list):
    print("\n")
    dividend = 0
    divisor = len(dataset)

    for data in dataset:
        dividend += data

    mean = round(dividend/divisor, 2)
    return mean


def find_mean_input():
    """Finds the mean of user inputs by repeatedly asking with a while loop that is cancelled by the "end" keyword. In the while loop, the user's input is added to a local variable called "dividend" which creates the sum of all inputs and every input cycle, 1 is added to the divisor,
    which represents the total amounts of value. The dividend/divisor is then worked out.

    Parameters:
    N/A

    Returns:
    Mean of user inputted values"""

    print("\n")
    dividend = 0
    divisor = 0
    cancel = False
    # Asking the user for values to find the mean of
    while not cancel:
        u_val = input("Type 'end' to stop inputing values for mean calculation: ")
        if u_val != str.casefold("end"):
            try:
                float(u_val)
            except ValueError:
                print("You typed in an invalid input. Try again")

            else:
                dividend = dividend + float(u_val)
                divisor += 1

        elif u_val == str.casefold("end"):
            print("Ending operation...")
            cancel = True

        else:
            print("Invalid input. Try again.")

    mean = round(dividend / divisor, 2)
    return mean
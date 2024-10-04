# Program #1: Kilometer Converter
# Programmer: Mai Lillie
# Date: 10/4/14

#code to convert kilometers to miles
def kilometer_conversion(kilometers):
    miles = 0.0
    miles = kilometers * 0.6214
    # Return the variable to the calling function
    return miles

if __name__ == '__main__':
    # Get User Input
    kilos = float(input("How many kilometers: "))
    # Call kilometer_conversion
    total = kilometer_conversion(kilos)
    # Display the miles
    print("That is", total, "miles!")

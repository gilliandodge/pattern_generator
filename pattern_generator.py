#goal: create a program that generates a sweater pattern from a pre-set pattern
#tailor the pattern to specific gauge and size

import math
import scarf_pattern
import kinda_yoke_pattern


#size option library (display size measurements)
#all sizes in inches
#may have to adjust sizing per pattern, this is for yoke sweater as of rn
def size_library():
    sizes = [
    {
        "size": "XS", 
        "bust" : 37.5,
        "length" : 18.5,
        "arm_circ" : 15.5,
        "sleeve_length" : 15.0,
    },
    {
        "size": "Small", 
        "bust" : 40.25,
        "length" : 19.0,
        "arm_circ" : 17.0,
        "sleeve_length" : 15.0,
    },
    {
        "size": "Medium", 
        "bust" : 42.5,
        "length" : 19.75,
        "arm_circ" : 17.5,
        "sleeve_length" : 15.5,
    },
    {
        "size": "Large", 
        "bust" : 45.25,
        "length" : 20.5,
        "arm_circ" : 18.25,
        "sleeve_length" : 15.5,
    },
        {
        "size": "XL", 
        "bust" : 49.25,
        "length" : 21.25,
        "arm_circ" : 20.0,
        "sleeve_length" : 15.75,
    },
        {
        "size": "XXL", 
        "bust" : 52.0,
        "length" : 21.75,
        "arm_circ" : 22.0,
        "sleeve_length" : 15.75,
    }]

    print("--- AVAILABLE SIZES ---") 
    for i, size in enumerate(sizes): 
        print(f"[{i}] {size['size']}: Bust - {size['bust']}in, Length - {size['length']}in, Arm Circ - {size['arm_circ']}in, Sleeve - {size['sleeve_length']}in") 
    print(' ')
    
    # Let the user pick a size
    choice = int(input("Enter the number of the size you want to make: "))
    return sizes[choice]


def menu():
       print("Thank you for using the sweater pattern generator!")
       print("Please select from the following options: ")
       print("1. Generate a sweater pattern")
       print("2. View size chart")
       print("3. View pattern library")
       print("4. Use yardage calculator") #work in progress
       print("5. Exit")

       user_choice = int(input("Menu Choice: "))
       if user_choice == 1:
              pattern_generator()
       elif user_choice == 2:
              size_library()
       #elif user_choice == 3:
              #pattern_library()
       #elif user_choice == 4:
              #yardage_calculator()
       elif user_choice == 5:
              print("Thank you for using the sweater pattern generator!")
              print("Program by Gillian Dodge, 2026")
              exit()

def gauge():
     #I should have this as a function and not just copy the same print statements in each pattern lol
    print(' ')
    #ask needle size (account for US sizing or mm sizing)
    needle_size = input("Enter your needle size (US Sizing): ")
    print(' ')
    #ask how many sts for the gauge
    print("The gauge is measured in stitches and rows per 4x4inch square.")
    print(' ')
    gauge_sts = int(input("Enter the gauge stitch count: "))
    print(' ')
    #ask how many rows are needed for the gauge
    gauge_rows = int(input("Enter the gauge row count: "))
    print(' ')
    #display gauge in sts x row format
    print(f"Your gauge is {gauge_sts} sts x {gauge_rows} rows per 4x4 inch square.")

    inch_sts = math.ceil(gauge_sts/4)
    inch_rows = math.ceil(gauge_rows/4)

    print(f"There are {inch_sts} stitches and {inch_rows} rows per inch based on your gauge.")
    print(' ')
    return inch_sts, inch_rows, needle_size
   


def pattern_generator():
   
    #input for pattern selection
    print("Pattern Library")
    print("1. Yoke Sweater")
    print("2. Raglan Sweater")
    print("3. Scarf Pattern")
    print("4. Return to Main Menu")
    print(' ')
    pattern_selection = int(input("Enter your desired pattern from the menu options: "))

    if pattern_selection == 1:
        print("You have selected the yoke sweater pattern.")
        print("Welcome to the sweater pattern generator!")
        print("Please enter the following information to generate your pattern:")
        gauge()
        size_selection = input("Enter your desired size (XS, Small, Medium, Large, XL, XXL): ")
        print(' ')
        print(' ')

        inch_sts, inch_rows, needle_size = gauge()
        kinda_yoke_pattern.weird_sweater(inch_sts, inch_rows, needle_size   )

    elif pattern_selection == 2:
        print("This pattern is not available yet.")
    elif pattern_selection == 3:
        print("You have selected the scarf pattern.")
        print("Please enter the following information to generate your pattern:")
        print(' ')

        inch_sts, inch_rows, needle_size = gauge()
        scarf_pattern.scarf(inch_sts, inch_rows, needle_size)

    elif pattern_selection == 4:
        menu()
    else:
        print("Invalid pattern selection. Please select a valid pattern.")


#save option for textfile of pattern


#run program
if __name__ == "__main__":
    menu()
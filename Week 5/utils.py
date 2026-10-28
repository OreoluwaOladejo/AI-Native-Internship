"""Reusable utility functions that can be used for the week 3 project"""
import math

def calculate(num1, num2,choice2):
    if choice2==1:
        return(num1+num2)
    elif choice2==2:
        return(num1-num2)
    elif choice2==3:
      if num2==0:
        raise ValueError("You cannot divide by zero.")
      else:
        return(num1/num2)
    elif choice2==4:
        return(num1*num2)
    else:
         raise ValueError("Please choose an operation from 1 to 4.")


"""This gets and validates the calculator operation selected by the user."""
def get_calculator_choice():
 while True:
    try:    
     choice2=int(input("Enter your choice\n" 
                          "1 for Addition\n" 
                          "2 for subtraction\n" 
                          "3 for division\n" 
                          "4 for multiplication- "))
     if choice2 in (1, 2, 3, 4):
                return choice2
    except ValueError:
     print("This is not a valid number")
     continue

def display_menu():
    """Display the main menu and return the user's choice."""
    print(
        "\nPlease enter your choice:\n"
        "1 for Calculator\n"
        "2 for Converter\n"
        "3 for Decision Maker (Even / Odd)\n"
        "4 to exit the program"
    )

    return input("Your choice: ").strip()

def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def check_even_odd(number):
    """Return whether an integer is even or odd."""
    if number % 2 == 0:
        return "even"
    return "odd"


def get_number(prompt):
    """Ask for a valid, finite number and return it as a float."""
    while True:
        try:
            number = float(input(prompt))

            if not math.isfinite(number):
                print("Please enter a finite number.")
                continue

            return number

        except ValueError:
            print("This is not a valid number. Please try again.")


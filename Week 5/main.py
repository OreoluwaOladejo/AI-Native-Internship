
from utils import (
    calculate,
    celsius_to_fahrenheit,
    check_even_odd,
    display_menu,
    get_calculator_choice,
    get_number,
)


def main():
    """Run the program until the user chooses to exit."""
    while True:
        choice = display_menu()
        match choice:
            case "1":
                print("You have chosen the Calculator.")
                num1 = get_number("Enter the first number: ")
                num2 = get_number("Enter the second number: ")
                choice = get_calculator_choice()
                try:
                    result = calculate(
                        num1, num2, choice
                    )
                    print(f"Result: {result}")
                except ValueError as error:
                    print(error)
            case "2":
                print(
                    "You have chosen the Celsius "
                    "to Fahrenheit Converter."
                )
                celsius = get_number("Enter your temperature in Celsius: ")
                fahrenheit = celsius_to_fahrenheit(
                    celsius
                )
                print(
                    f"Your temperature in Fahrenheit "
                    f"is {fahrenheit:.2f}°F"
                )
            case "3":
                print("You have chosen the Decision Maker (Even / Odd).")
                number = get_number("Enter a whole number: ")
                if not number.is_integer():
                    print("Please enter a whole number.")
                    continue

                result = check_even_odd(int(number))
                print(f"This number is {result}.")

            case "4":
                print("Goodbye!")
                break

            case _:
                print("Please choose between 1 and 4.")

if __name__ == "__main__":
    main()


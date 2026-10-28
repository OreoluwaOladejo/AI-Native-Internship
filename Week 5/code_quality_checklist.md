# Code Quality Checklist

The following checklist is used to review the refactored Python utility program.

## Functions and Reusability

-  At least six reusable functions are defined.
-  Every function has a docstring.
-  Function names are descriptive 
- Functions accept parameters where appropriate.
- Functions return values where appropriate.
-  Repeated numeric input validation is handled by a reusable function.

## Code Organisation

-  The program is split across `utils.py` and `main.py`.
-  `main.py` imports and calls functions from `utils.py`.
-  The main menu and user interaction are separated from utility logic.
-  The `math` standard-library module is imported and used.

## Error Handling and Functionality

- Invalid numeric inputs are handled using `try` and `except`.
-  Division by zero is handled.
-  Invalid calculator operations are handled.
-  Invalid main-menu choices are handled.
-  The calculator has been tested with valid and invalid inputs.
-  The temperature converter has been tested.
-  The even/odd checker has been tested with valid whole numbers.
-  The exit option has been tested.

## Documentation

-  `README.md` has been reviewed for accuracy.
-  All files have been saved in the correct project directory.
-  The program runs successfully using `python main.py`.


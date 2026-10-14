while True:
    choice=input("Please enter your choice\n" 
    "1 for Calculator\n" 
    "2 for Converter \n" 
    "3 for Decision Maker\n"
    "4 to exit the loop  ")
    match choice:
        case "1":
            print("You have chosen The Calculator")
            try:
              num1=float(input("Please enter the first number you wish to calculate- "))
              num2=float(input("Please enter the second number you wish to calulate- "))
            except ValueError:
                 print("This is not a valid number")
                 continue
            try:
              choice2=int(input("Enter your choice\n" 
                          "1 for Addition\n" 
                          "2 for subtraction\n" 
                          "3 for division\n" 
                          "4 for multiplication- "))
            except ValueError:
               print("This is not a valid number")
               continue
            if choice2==1:
                print(num1+num2)
            elif choice2==2:
                print(num1-num2)
            elif choice2==3:
                if num2==0:
                    print("You cannot divide by 0")
                else:
                    print(num1/num2)
            elif choice2==4:
                print(num1*num2)
            else:
                print("Wrong input please input a valid number")
        case "2":
            print("You have chosen the Celsius  to Farenheit Converter")
            try:
               Celsius=float(input("Enter your degree in Celsius"))
            except ValueError:
                print("This is not a valid number")
                continue
            Farenheit=(Celsius*(9/5))+32
            print(f"Your degree in farenheit is {Farenheit}°F")
        case "3":
            print("You have chosen the Decision checker(Even / Odd)")
            try:
               num=int(input("Enter your number"))
            except ValueError:
                print("This is not a valid number")
                continue
            if num%2==0:
                print("This number is even")
            else:
                print("This number is odd")
        case "4":
            print("Goodbye")
            break
        case _:
            print("Please choose between 1 to 4")
        

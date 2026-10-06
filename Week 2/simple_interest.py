principal=float(input("Enter your principal amount"))
rate=float(input("Enter your rate"))
time=int(input("Enter the number of years per annum"))
simple_interest=(principal * rate *time) / 100
total_amount = principal + simple_interest

print(f"Your simple interest is {simple_interest} naira")
print(f"Your total amount is {total_amount}")
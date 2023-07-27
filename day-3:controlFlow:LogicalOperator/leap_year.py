year = int(input("Type year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
"""

This version of the code uses the and and or operators to combine the three conditions into a single expression. 
According to the rules for leap years, a year is a leap year if it is divisible by 4, 
unless it is also divisible by 100. However, if it is divisible by 400,
then it is still considered a leap year.

This revised version of the code checks if the year is divisible by 4 and either not divisible by 100 or divisible by 400.
This correctly implements the rules for leap years in a more concise way.

"""

#Solution 2

if year % 4 == 0:
    if year % 100 == 0:
        if year % 4 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
            
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("please pay $5")
    elif age <= 18:
        bill = 7
        print("please pay $7")
    else:
        bill = 12
        print("please pay $12")
        
    wants_photo = input("Do you want photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is $ {bill}")
    
        
else:
  print("Sorry, you have to grow taller before you can ride.")
  
  
#solution 2

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    bill = 5 if age < 12 else 7 if age <= 18 else 12
    print(f"Please pay ${bill}")
    
    wants_photo = input("Do you want photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


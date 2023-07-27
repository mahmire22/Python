
'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight) / float(height) ** 2
bmi_as_int = round(bmi, 1)
print(f"Your BMI is {bmi_as_int}")

if bmi_as_int < 18.5:
    print("You are underweight")
elif bmi_as_int >= 18.5 and bmi_as_int < 25:
    print("You are normal weight")
elif bmi_as_int >= 25 and bmi_as_int < 30:
    print("You are overweight")
elif bmi_as_int >= 30 and bmi_as_int < 35:
    print("You are clinically obese")
else:
    print("You are severely obese")
'''




#Solution 2

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your bmi is {bmi}, You are normal weight")
elif bmi >= 25 and bmi < 30:
    print(f"Your bmi is {bmi}, You are overweight")
elif bmi >= 30 and bmi < 35:
    print(f"Your bmi is {bmi}, You are clinically obese")
else:
    print(f"Your bmi is {bmi}, You are severely obese")
    
################################




#Solution 3

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)
categories = ["underweight", "normal weight", "overweight", "clinically obese", "severely obese"]
limits = [18.5, 25, 30, 35]
category = next((category for limit, category in zip(limits, categories) if bmi < limit), categories[-1])
print(f"Your bmi is {bmi}, You are {category}")


'''
In this shorter version, I added two lists: categories and limits.
The categories list contains the names of the different BMI categories, while the limits list contains the upper limits of each category.
I then used the next() function with a generator expression to find the first category for which the BMI value is less than its upper limit.
If no such category is found (i.e., if the BMI value is greater than or equal to the upper limit of all categories),
then the last category in the categories list is used.

This approach allows us to determine the appropriate BMI category using a single line of code, rather than multiple if and elif statements. 
The final print() statement uses an f-string to display both the calculated BMI value and the determined category.

'''

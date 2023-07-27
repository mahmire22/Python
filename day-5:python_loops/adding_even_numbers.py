#solution 1
total = 0

for number in range(1, 101, 2):
    total = total+number
print(f"The sum of all even numbers from 1 to 100 is: {total}")


#solution 2
total2 = 0

for number in range(2,100, 2):
    if total % 2 == 0:
        total2 = total+number
print(f"The sum of all even numbers from 1 to 100 is: {total2}")

        
        
        
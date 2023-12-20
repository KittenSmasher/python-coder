# Exam Project
import os

# Question 1 (Empty Bucket)

bucket = []

bucket.append("Apple")
bucket.append("Banana")
bucket.append("Milk")
bucket.append("Bread")
bucket.append("Eggs")

print(bucket)

input()
os.system('cls') # press enter to clear terminal

# Question 2 

# Ask the user to input their age
age = int(input("Enter your age: "))

# Classify the number based on range
if age < 18:
    print("You belong to the Teenager category.")
elif age >= 18 | age <=30:
    print("You belong to the Young Adult category.")
else:
    print("You belong to the Adult category.")
    
input()
os.system('cls')

# Question 3

def calculate_triangle_area(base, height):
    # calculate the area of the triangle using the base and height
    area = (base * height) / 2
    return area

def main():
    # print program header
    print("Triangle Area Calculation Program")
    print("---------------------------------")
    
    # prompt the user to enter the base and height of the triangle
    base = float(input("Enter the length of the base: "))
    height = float(input("Enter the height: "))
    
    # call the function to calculate the area
    area = calculate_triangle_area(base, height)
    
    print("The area of the triangle is", area)

# call function
main()

input()
os.system('cls')
 # while loop = execute some code WHILE some condition remains true

# Example 1
name = input("Enter your name: ")

while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ")   # loop continues until we enter any thing
print(f"Heyyy!! {name}")

# Example 2
age = int(input("Enter your age: "))

while age <= 0 :
    print("Age Can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Example 3
food = input("Enter your favourite food (press q to quit) : ")

while not food =="q":
    print(f"Your favourite food is {food}")
    food = input("Enter your another favourite food (press q to quit) : ")
print("Bye !! Have a good day")

# Example 4
num = int(input("Enter any number between 1 to 20 :"))
while  num < 1 or num > 20:
    print(f"{num} is not a valid number")
    num = int(input("Enter any number between 1 to 20 :"))
print("Nice !! Number")



# -------------------------Infinity Loop---------------------------------------

age= input("Enter your age: ")
while age =="":
    print("You didn't enter your age")  # its infinity loop if we didn't enter any age
print(f"your age is {age}")



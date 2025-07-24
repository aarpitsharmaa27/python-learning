
        ## if elif and else statements

age = int(input("Enter your age: "))

if age <= 18 :
    print("Sorry! Content is age restricted.")

elif age >= 18 and age < 61 :
    print("Welcome to our world !! Now you can sign in. ")

elif age >= 61 and age <= 120:
    print("Sorry!! You are to old to sign im.")

else:
    print("Please enter a valid age.")


#--------------------------------------------------------------------#

name = input("Enter your name: ")

if name == "":
    print("Please enter a name.")
else:
    print(f"Hello, {name}!")


#----------------------------------------------------------------------#


for_sale = True
if for_sale:
    print("This item is for sale.")

else:
    print("This item is not for sale.")

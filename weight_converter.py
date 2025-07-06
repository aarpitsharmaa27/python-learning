  # Pyhton weight converter

weight = float(input("Enter your weight :"))
unit = input("kilogram or Pounds ? (K or L):")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "kg."

else:
    print(f"{unit} was not valid")

print(f"your weight is {round(weight, 3)} {unit} ")

        # Break and continue example in Python

students = ["Sanjay","Meenu","Arpit","Nupur"]


    ## Using Break

for student in students:
    if student == "Arpit":
        break;             # Stops the loop whe Arpit is found


    ## Using Continue

for student in students:
    if student == "Arpit":
        continue;
    print(student)      # Skips "Arpit" but continues the loop

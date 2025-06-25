from Variables import is_student  # TYPECASTING
 # THE PROCESS OF CONVERTING A VARIABLES FROM ONE DATA TYPE TO ANOTHER i.e str(), int(), boot()

name = "Arpit Sharma"
age = 22
gpa = 3.14
is_student = True
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# CONVERSION

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

name = bool(name)
print(name)
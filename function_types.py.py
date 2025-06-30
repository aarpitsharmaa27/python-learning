                    #FUNCTION

    # In Build Function

#Functions which already exist in python and we directly use them.

#like - int() , float() , str()

    # Module functions

# There are many module functions exist in python we use one of them i.e math
from math import factorial
print(factorial(10))


    # User defined Function

 #functions which are made by programers itself.

def print_sum(a , b):
     print(a + b)

print_sum(3,2)


def print_sum(a, b=4):
    print(a + b)

print_sum(1)
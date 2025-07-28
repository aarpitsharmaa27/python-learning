

# Collections = single "variables" used to store multiple values.

# List = [] order and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER



#--------------- LIST -------------------------------#

fruits = ["Mango", "Apple", "Banana", "Guava"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[0:3])

for x in fruits:
    print(x)

print(dir(fruits))  # is shows which funtions and attributes are available in list
print(help(fruits))  # it gives full info on use of function , attributes, syntax.
print(len(fruits))  # Give length of given list
print("Banana" in fruits)   # It shows that product is in list or not vie True or False

fruits[2] = "Pineapple"     # It replace the product from list
for fruit in fruits:
    print(fruit)

fruits.append("Watermelon")     # It add any product at the end of the list
print(fruits)

fruits.remove("Guava")      # It remove any product at the end of the list
print(fruits)

fruits.insert(3, "Orange")      # It add any product at any place in list
print(fruits)

fruits.sort()           # It arrange list in alphabetical order
print(fruits)

fruits.reverse()        # It reverse the List
print(fruits)

print(fruits.index("Pineapple"))        # It print the index of any product
print(fruits.index("Apple"))

print(fruits.count("Mango"))        # It counts number of products in given list
print(fruits)

fruits.clear()
print(fruits)




#------------------------ SETS ------------------------#

#       Remember =  Sets are {} unordered and immutable, but Add/Remove OK. NO duplicates


products = {"Cream", "Books", "Shoes", "Sandles"}
print(products)

print(dir(products))        # it shows all functions and attributes which are available in following set
print(help(products))       # it shows use of all functions and attributes of following list.

products.pop()              # it remove random element from set
print(products)

# products.len()              # It shows error becase len function doesn't work in sets
# print(products)

products.clear()            # it shows empty set.
print(products)

# Some same function as we used in list .




#------------------------- TUPLE ----------------------------#

#           Remembers =  Tuple is () ordered and unchangeable. Duplicates OK. FASTER

mobiles = ("Xiomi", "Motorola", "Oppo", "Nokia")
print(mobiles)

print(dir(mobiles))

print(help(mobiles))

print ("Xiomi" in mobiles)

print(mobiles.index("Oppo"))

print(mobiles.count("Nokia"))           # count number of total input product in tuple

for mobile in mobiles:                  # print tuple in vertically
    print(mobile)



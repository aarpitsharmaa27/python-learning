
#       2D list is a list which is made up of lists

TV =      ["samsung","xiomi", "suntek"]
Laptops = ["aesus", "dell", "lenovo"]
Mobiles = ["redmi", "oppo", "motorola"]

products = [ TV , Laptops , Mobiles]

print(products)

print(products[2])          # It return entire row as output

print(products[0])

print(products[1][0])      # It means row 1 column 0 product i.e aesus

print(products[2][2])       # It means row 2 column 2 product i.e motorola

print(products[0][2])      # It means row 0 column 2 product i.e suntek



products = [  ["Samsung","Xiomi", "Suntek"] , ["Aesus", "Dell", "Lenovo"] , ["Redmi", "Oppo", "Motorola"] ]

for product in products:      # It print input vertically
    for device in product:      # It print every single input vertically
        print(device, end=" ")     # It print every input horizontally
    print()                          # It print every row and column in the way it is
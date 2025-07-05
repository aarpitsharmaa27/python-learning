                            # LOOP


print(1)
print(2)
print(3)
print(4)
print(5)
print(6)

# to print values till 100 we have to input print 1, 2, 3, 4
# but by loop we have a shorttrick

i =  1
while i <= 100 :
    print(i)
    i = i + 1

i = 20
while i >=500:      # False because 20 !> 500  (NO LOOP)
    print(i)
    i = i + 1

i = 1
while i <= 1000:
    print(i)
    i = i + 1

i = 1
while i <= 5:
    print(i)  # Its Infinity loop because output always remains same i.e 1
    i = i + 1

i = 1
while i <= 10 :
    print(i * "*")     # We can Print Any Symbol/Word in a Pattern
    i = i + 1

i = 1
while i <= 10 :
    print(i * ".")
    i = i + 1


i = 1
while i <= 10 :
    print(i * "^")
    i = i + 1


# Reverse Loop

i = 5
while i>=0 :
    print(i)
    i = i - 1

i = 100
while i >= 10 :
    print(i)
    i = i - 2


i = 20
while i >= 1:
    print(i * "OYE")
    i = i - 1

# Shorttrick to print Numbers

for i in range(10):
    print(i)

for i in range(500):
    print(i)

for i in range(1000):
    print(i)

# for loops = execute a blocl of code a fixed number of times.
#              We can iterate over a range, string, sequence, etc.

for x in range (1 ,10):   # print 1 to 9 in order
    print(x)

for y in reversed(range (1 , 100)):   # print 1 to 99 in reverse order
    print(y)

print("HAPPY NEW YEAR")

card_number = "3453-3452-7643-9906"
for x in card_number:               # It prints numbers in a line format.
    print(x)

for z in range (1 , 50 , 3):   # print 1 to 5 with step of 3
    print(z)

for x in range (1 , 30):
    if x == 12 :
        continue         # Skips 12
    print(x)

for x in range (1 , 30):
    if x == 12 :
       break        # With break , loop stops when input number comes.
    print(x)
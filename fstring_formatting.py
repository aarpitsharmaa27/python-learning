# format specifiers = {value:flags} format a vlaue based on what flags are inserted


# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate position value
# := = place sign to leftmost position
# :  = insert a space before positive number
# :, = comma separator


price1 = 55840.345
price2 = -5345.89
price3 = 468495.643

#print(f"Price 1 is ${price1:.2f}")    #  print upto 2 decimal spaces

#print(f"Price 2 is ${price2:.2f}")
#print(f"Price 3 is ${price3:.2F}")

#print(f"Price 1 is ${price1:6}")    #  :6 fit every characters in 6 space width
#print(f"Price 2 is ${price2:6}")
#print(f"Price 3 is ${price3:6}")


#print(f"Price 1 is ${price1:012}")    #  :6 fit every characters in given space width and fill gap with zeroes
#print(f"Price 2 is ${price2:09}")
#print(f"Price 3 is ${price3:013}")

#print(f"Price 1 is ${price1:<12}")    #  it shows left justifier i.e print output on left side
#print(f"Price 2 is ${price2:>9}")       #  it shows right justifier i.e print output on right side
#print(f"Price 3 is ${price3:^13}")      #  it shows center justifier i.e print output on center


#print(f"Price 1 is ${price1:+}")        #  :+ indicates positive values with +ve sign as output
#print(f"Price 2 is ${price2:+}")
#print(f"Price 3 is ${price3:+}")

#print(f"Price 1 is ${price1: }")        #  : gave space before positive values in left side
#print(f"Price 2 is ${price2: }")
#print(f"Price 3 is ${price3: }")


#print(f"Price 1 is ${price1:,}")     # add commas between different places of digits
#print(f"Price 2 is ${price2:,}")
#print(f"Price 3 is ${price3:,}")



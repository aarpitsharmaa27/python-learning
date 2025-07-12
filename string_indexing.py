 # indexing = accessing elements of a sequence using [] indexing operator



credit_number = "123-435-45-345-5635"

print(credit_number[0])    # to print 0th position digit
print(credit_number[5])
print(credit_number[0:4])   # to print digits starting from 0th position to 3rd position
print(credit_number[5:9])   # to print digits starting from 5th position to 8th position
print(credit_number[:12])   # to print digits starting from 0th position to 11th position
print(credit_number[12:])   # to print digits starting from 12th position to till end


print(credit_number[-1])    # it counts digits from reverse
print(credit_number[-12:])   # prints last 12 characters using negative indexing
print(credit_number[-12:-1])   # counting from reverse 1st to till 12th postion then print digits except -1


print(credit_number[::2])  # prints every 2nd character starting from index 0

print(credit_number[::4])   # it print output with gap of three digit
print(credit_number[1::3])   # it prints digits from starting from 1st position with the gap of 2
print(credit_number[::-2])   # it prints digits from reverse with the gap of 1 digit

last_digit = credit_number[-4:]    # to print last digits
print(f"XXXX-XXXX-XXXX-{last_digit}")

credit_number = credit_number[::-1]  # credit card number in reverse
print(credit_number)

credit_number2 = "4346-2345-7909-1435"
print(f"XXXX-XXXX-XXXX-{credit_number2[-4:]}")


# with [:-1] numbers prints in same format from starting to ending
# with [::-1] number print in reverse format
                    #LIST OPERATIONS

marks = [90, 95, 89]    # Here ,We took marks of 3 subjects but we want to add marks of more subject then we use (append)

marks.append(94)
print(marks)


marks = [90, 95, 89]     # We use insert to add number in middle
marks.insert(2 , 87)   # I use 2 as index because I want to add 87 after 95
print(marks)

print(89 in marks)      # By this ,We can also check that marks exist in our list or not
print(77 in marks)

# Now to find lenght of list we use (len)

marks = [ 89, 98, 95, 82, 88, 68]
print(len(marks))



marks = [98,97, 92, 79, 84]
i = 0
while i < len(marks):      # To print marks by (while) loop
    print(marks[i])
    i = i + 1

marks.clear()
print(marks)        # For empty list
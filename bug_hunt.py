count = 1
total = 0

# BUG: Added missing colon at the end of the while statement and changed condition from '< 5' to '<= 5' so that 5 is included in the sum.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted total from integer to string using str(total) to resolve TypeError during string concatenation.
print("Sum of 1 to 5 is: " + str(total))

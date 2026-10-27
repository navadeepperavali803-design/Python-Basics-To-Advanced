numbers = [12, 7, 4, 9, 16, 21, 8, 3]
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("even count is:",even)
print("odd count is:",odd)
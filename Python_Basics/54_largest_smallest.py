numbers = [25, 10, 85, 40, 5, 60]
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if num > largest:
        largest=num
    if num < largest:
        smallest=num
print("largest number:",largest)
print("smallest number:",smallest)
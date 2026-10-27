numbers = [34, 12, 67, 5, 89, 23]
smallest=numbers[0]
for num in numbers:
    if num < smallest:
        smallest=num
print(smallest)
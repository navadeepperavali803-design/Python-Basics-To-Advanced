numbers = [1, 2, 3, 5, 6, 7,8]
total=0
for num in numbers:
    total+=num
expected_total=8*9//2
missing=expected_total-total
print(missing)
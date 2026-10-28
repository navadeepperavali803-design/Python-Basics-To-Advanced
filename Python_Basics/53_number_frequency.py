numbers = [1, 2, 2, 3, 1, 4, 2, 3, 5]

unique_numbers = set(numbers)

for num in unique_numbers:
    frequency = 0

    for item in numbers:
        if item == num:
            frequency += 1

    print(num, "appears", frequency, "times")
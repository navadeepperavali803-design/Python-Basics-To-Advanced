numbers = [25, 10, 85, 5, 40, 10, 60]

smallest = numbers[0]
second_smallest = None

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num != smallest:
        if second_smallest == None or num < second_smallest:
            second_smallest = num

print("Second-smallest number:", second_smallest)
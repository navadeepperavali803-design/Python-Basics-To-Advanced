numbers = [10, -5, 20, -8, 0, 15, -3, 7]
positive=[]
negative=[]
for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
print("positive numbers are:",positive)
print("negative numbers are:",negative)
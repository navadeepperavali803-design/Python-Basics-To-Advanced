numbers = [0, 5, 0, 3, 8, 0, 2]
number=[]
zero_count=0
for num in numbers:
    if num == 0:
        zero_count+=1
    else:
        number.append(num)
for i in range(zero_count):
    number.append(0)
print(number)
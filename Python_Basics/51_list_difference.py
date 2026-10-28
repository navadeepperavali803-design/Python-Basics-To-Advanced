list1 = [10, 20, 30, 40, 50]
list2 = [30, 50, 60, 70]
difference=[]
for num in list1:
    if num  not in list2:
        difference.append(num)
print(difference)

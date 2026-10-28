list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merge=list1.copy()
for num in list2:
    if num not in merge:
        merge.append(num)
print(merge)
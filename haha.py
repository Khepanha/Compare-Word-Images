from collections import Counter
arr = ['apples', 'bananas', 'orange', 'grape', 'apples', 'apples', 'bananas']
arr2 = ['apples', 'orange']
# for row_num, data in enumerate(arr):
#     print (row_num, data)

# print (list(dict.fromkeys(arr))) //remove duplicate value in list

print (list((Counter(list(dict.fromkeys(arr))) - Counter(arr2)).elements()))
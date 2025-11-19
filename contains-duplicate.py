from collections import Counter

arr=[1,2,3,4]
count = Counter(arr)
for v in count.values():
    if v > 1:
        print(True)
        break
    elif v==1:
        print(False)
        
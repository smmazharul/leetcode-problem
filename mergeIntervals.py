intervals = [[1,3],[2,6],[15,18],[8,10]]

intervals.sort()
result=[intervals[0]]

for i in range (1,len(intervals)):
    if result[-1][0]<=intervals[i][0]<=result[-1][1]:
        result[-1][1]=max(result[-1][1],intervals[i][1])
    else:
        result.append(intervals[i])
print(result)
   
        


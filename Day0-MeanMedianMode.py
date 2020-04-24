# import statments 
import sys
from statistics import mean,median,mode

# Read input from STDIN
 # Line 1 - number of elements in array - read input and cast as int
N = int(input().strip())

# Line 2 - array values - delimiter ' '
arr = [int(i) for i in input().strip().split(' ')] 
arr.sort()  # sort array

# Mean
print('{0:.1f}'.format(sum(arr)/N))

# Median
if N % 2 == 1:
    print('{0:.1f}'.format(arr[int((N-1)/2)]))
else:
    print('{0:.1f}'.format(0.5*(arr[int(N/2)-1]+arr[int(N/2)])))
    
# Mode
counts=[]
for i in arr:
    counts.append(arr.count(i))
if max(counts) > 1:
    print(arr[counts.index(max(counts))])
else:
    print(min(arr))

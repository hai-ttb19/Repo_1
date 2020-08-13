# arr = [0,1,0,0,0,1,0]
# n = len(arr) - 1
# minJump = n
# j_list, cop_curJump =[],[] 
# curJump = 0
# def Move(i):
#   global arr, minJump, curJump
#   print('Jump to node ',i)
#   curJump+=1
#   print('Current number of Jumps',curJump)
#   for j in [1,2]:
#       if i == n :
#           print('Number of Jumps',curJump,'END !!!')
#           return curJump
#       k = i + j
#       print('i = {}, j = {}'.format(i,j))
#       if arr[k] == 0:
#           Move(k)
#           print('Back from node ',i)
#           curJump-=1

# print(Move(0))
from itertools import starmap,compress
arr = [1,2,3,4,5]
arr2 = arr[::-1]
k=3
fSum = lambda x,y:x+y
filt = lambda x:True if (x%3==0) else False

for a in arr[:-1]:
    arr2.pop()
    sumResult = list(starmap(fSum,[(a,i) for i in arr2]))
    print(sumResult)
    print(len(filter(filt,sumResult)))
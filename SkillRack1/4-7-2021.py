from integerlist import IntegerList

numList = IntegerList(list(map(int,input().strip().split())))
Q = int(input().strip())
for ctr in range(Q):
    query = input().split() 
    queryType = int(query[0]) #first index value 
    if queryType == 1:
        left,right,val = map(int,query[1:]) # splitting the rest of value 
        numList.updateRange(left, right, val)
    elif queryType == 2:
        left, right = map(int, query[1:])
        print(numList.getSum(left,right))

# keyRow = list(input() for row in range(3))
# S = input().strip()
# flag = False 
# RowVal= []
# for i in range(0,3):
#     ctr,ptr= 0,0
#     for j in range(2,len(S)+1):
#         # print(S[ctr:j-1],S[ctr+1:j])
#         # print(keyRow[i])
#         if S[ctr:j-1] in keyRow[i] and S[ctr+1:j] in keyRow[i]:
#         # if S[ctr:j-1] and S[ctr+1:j] in keyRow[i]:
#             ptr+=1
#             flag = True 
#         ctr+=1
#     RowVal.append(ptr)
# print(RowVal)
# max_index = max(RowVal)
# # print(max(RowVal)-1)
# if flag == False:
#     print(-1)
# else:
#     for i in range(len(RowVal)):
#         if RowVal[i] == max_index:
#             print(keyRow[i])
#     max_index = RowVal.index(max(RowVal))
#     print(keyRow[max_index])
# # print(keyRow[max(RowVal)-1])

def getRow(ch):
    for row in range(0,3):
        if ch in keyRow[row]:
            return row 

keyRow = list(input() for row in range(3))
S = input().strip()
keyIndex,ind,count,prevMaxCount = [],getRow(S[0]),1,1
for ctr in range(1,len(S)):
    if getRow(S[ctr]) == getRow(S[ctr-1]):
        ind,count = getRow(S[ctr]),count+1 
    else:
        if count > prevMaxCount:
            # keyIndex.append(ind)  // whats the difference between this two have to be checked
            keyIndex= [ind]
            prevMaxCount = count 
        elif prevMaxCount == count and count > 1:
            keyIndex.append(ind)
            prevMaxCount = count 
        count,ind = 1,getRow(S[ctr]) 
if len(S) > 1 and getRow(S[-1]) == getRow(S[-2]):
    if count > prevMaxCount:
        # keyIndex.append(ind)
        keyIndex = [ind]
    elif prevMaxCount == count and count > 1:
        keyIndex.append(ind)
print(keyIndex)
if keyIndex:
    keyIndex = sorted(set(keyIndex))
    for ind in keyIndex:
        print(keyRow[ind])
else:
    print(-1)







'''
qwertyuiop
asdfghjkl
zxcvbnm
skillrack


qwertyuiop
asdfghjkl
zxcvbnm
motion 

qwertyuiop
asdfghjkl
zxcvbnm
google

'''


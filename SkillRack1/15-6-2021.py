# R,C = map(int,input().split())
# matrix = [list(map(int,input().split())) for row in range(R)]
# N= int(input())

# for row in range(0,R):
#     for col in range(0,C):
#         if N-col-1>=0 and N+col < C:
#             print(matrix[row][N-col-1]+matrix[row][N+col],end=" ")
#         elif N-col-1 >= 0:
#             print(matrix[row][N-col-1],end=" ")
#         elif N+col<C:
#             print(matrix[row][N+col],end=" ")
#         else:
#             break 
#     print() 



r,c=map(int,input().split())
l=[[int(i) for i in input().split()] for i in range(r)]
n=int(input())
col=n 
for j in range(n-1,-1,-1):
    for i in range(r):
        if col>c-1:
            l[i].append(l[i][j])
        else:
            l[i][col]+=l[i][j]
    col+=1

for i in l:
    print(*i[n:])





'''

3 5
1 2 3 4 5 
2 4 6 8 2
10 20 30 40 50
4

3 5
1 2 3 4 5
4 8 6 7 9
10 20 30 45 55
2


3 5
1 2 3 4 5 
2 4 6 8 2
10 20 30 40 50
5



'''


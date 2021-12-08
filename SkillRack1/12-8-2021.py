R,C = map(int,input().split())
matrix = [list(map(int,input().split())) for row in range(R)]
X,Y,K = map(int,input().split())
for col in range(K):
    xval = X
    yval = Y 
    val = K-1
    for row in range(K):
        matrix[xval-1][yval-1],matrix[xval+val-2][yval-1] = matrix[xval+val-2][yval-1],matrix[xval-1][yval-1]        
        xval-=1
    Y+=1 
print(matrix)


'''

5 8
55 56 19 46 44 69 15 40
92 64 35 95 59 98 53 54
82 78 81 86 61 38 27 39
75 17 20 84 72 12 29 79
26 34 30 62 68 51 21 91
2 2 3


'''
    

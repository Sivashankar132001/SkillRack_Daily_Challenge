N = int(input())
resM = [] 
resF = []
for i in range(N):
    nga = list(input().split())
    if nga[1] == 'M':
        resM.append([nga[0],nga[-1]])
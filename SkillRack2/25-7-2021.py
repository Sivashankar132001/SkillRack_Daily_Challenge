def isLeap(year):
    return ((year%400 == 0) or ((year%100 !=0) and (year%4 == 0)))

    

M,N = map(int,input().split())
Y = int(input())


months = [["Jan",31],["Feb",28],["Mar",31],["Apr",30],["May",31],["Jun",30],["Jul",31],["Aug",31],['Sep',30],["Oct",31],["Nov",30],["Dec",31]]
if(isLeap(Y)):
   months[1][1]+=1 

sd = 1
currM = 0
val = 0

while(1):
    sd += M 
    if sd > months[currM][1]:
        val = sd - months[currM][1]
        sd = 1 
        sd += val - 1 
        currM += 1
    print(f"{str(sd).zfill(2)}-{months[currM][0]}-{Y} to {str(sd.zfill(2))} ")










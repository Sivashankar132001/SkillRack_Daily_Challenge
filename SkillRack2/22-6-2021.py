N = input()
val = int(N[1:-1])
bs = []
for i in range(1,val+1):
    para = N[0]*i+N[-1]*i
    print(para,end="")
    for i in bs[::-1]:
        print(i,end="")
    print()
    bs.append(para)

  #include<stdio.h>
  #include<stdlib.h>

  # int main(){
  #     int N,currNum;
  #     scanf("%d",&N);
  #     unsigned long long int val,sum=0;
  #    char numStr[15];
  #     for(int ctr = 1; ctr<=N; ctr++){
  #       scanf("%d",&currNum); 
  #       sprintf(numStr,"%d%d",sprintf(numStr,"%d",currNum),currNum); //101010
  #       puts(numStr);
  #       sscanf(numStr, " %llu",&val);
  #       // printf("%llu",val);
  #       sum += val;
  #     }
  #     printf("%llu",sum);
  #     return 0;
  # }

N = int(input())
ls = list(map(int,input().split()))
sums = 0
for i in range(0,N):
  length = len(str(ls[i]))
  sVal = str(length)+str(ls[i])
  sums += int(sVal)
print(sums)



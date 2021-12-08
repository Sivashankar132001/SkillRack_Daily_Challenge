#include<stdio.h>
#include<stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

boundedArray* getXthDiagonal(int R, int C, int matrix[R][C], int X){
    boundedArray *bArr = malloc(sizeof(boundedArray));
    bArr->arr = malloc(sizeof(int)*(R+C));
    bArr->SIZE = 0;
    int row = R-1, col = 0;
    for(int ctr = 1; ctr < X; ctr++){
        if(row == 0){
            col++;
        }
        else{
            row--;
        }
    }
    while(row<R && col < C){
        bArr->arr[bArr->SIZE++] = matrix[row++][col++];
    }
    return bArr;
}

int main(){
    int R,C,X;
    scanf("%d %d",&R,&C);
    int matrix[R][C];
    for(int row = 0; row<R; row++){
        for(int col =0; col <C; col++){
            scanf("%d" , &matrix[row][col]);
        }
    }
    scanf("%d", &X);
    boundedArray *bArr = getXthDiagonal(R,C,matrix,X);
    printf("Diagonal %d ",X);
    for(int index = 0; index < bArr->SIZE; index++){
        printf("%d ",bArr->arr[index]);
    }
    return 0;
}


/*
skillrack diay challenge of the a
6 5
89 5 6 81 32 15
48 30 71 23 94
39 28 18 75 14
19 33 57 91 95
93 70 80 59 60
32 73 36 69 83
7


*/
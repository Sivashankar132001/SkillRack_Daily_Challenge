#include<stdio.h>
#include<stdlib.h>

typedef struct BoundryArray
{
    int SIZE;
    int *arr;
} boundaryArray;

boundaryArray* getThreeOrFourDigits(int SIZE, int arr[])
{
    boundedArray *bArr = malloc(sizeof(boundedArray));
    bArr[arr] = malloc(sizeof(int)*SIZE);
    bArr[SIZE] = 0;
    fo(int index=0; index<SIZE; index++){
        if(getDigitCount(arr[index])) == 3 || (getDigitCount(arr[index])) == 4{
            bArr[arr[bArr[SIZE++]]] = arr[index];
        }
    }
    return bArr;
}


int main(){
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index=0; index<N; index++){
        scanf("%d", &arr[index]);
    }
    boundedArray *bArr = getThreeOrFourDigits(N, arr);
    printf("Ols Array: ")
    for(int index=0; index<N; index++){
        printf("%d", arr[index]);
    }
}

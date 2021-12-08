#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int isLeap(int year)
{
    return (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0));
}

void printFullMonth(int month)
{
        char months1[12][10] = {"January","February","March","April","May","June","July","Augest","September","October","November","Decmeber"};
        printf(months1[month]);

}

int main(){
    int dd, yyyy;
    char date[50],mm[10];
    scanf("%s",&date);
    yyyy = atoi(&date[7]);
    date[6] = '\0';
    strcpy(mm,&date[3]);
    date[2] = '\0';
    dd = atoi(date);
    char months[12][10] = {"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"};
    int days[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    if(isLeap(yyyy))
    {
        days[1]++;
    }
    for(int i=0; i<12; i++){
        if(strcmp(months[i],mm) == 0){
            if(i==0)
            {
                printf("December %d - 31 days\n",yyyy-1);
                printf("February %d - %d days",yyyy,days[i+1]);
            }
            else if(i == 11)
            {
                printf("November %d - 30\n",yyyy);
                printf("January %d - 31",yyyy+1);          
            }
            else{
                printFullMonth(i-1);
                
                printf(" %d - %d ",yyyy,days[i-1]);
                printf("days\n");
                printFullMonth(i+1);
                printf(" %d - %d ",yyyy,days[i+1]);
                printf("days\n");
            }
        }
    }
}




/*

20-Jan-2020

05-Aug-2021

26-Dec-2004


*/
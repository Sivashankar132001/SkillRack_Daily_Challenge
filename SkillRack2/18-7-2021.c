#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *prev, *next;
};

struct Node *head = NULL, *tail = NULL;

void append(int data)
{
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->data = data;
    if(head == NULL)
    {
        head = tail = newNode ;
    }
    else{
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
    tail->next = head;
    head->prev = tail;
}

void display(struct Node *head)
{
    struct Node *ptr = head;
    while(ptr->next != head)
    {
        printfA("%d ",ptr->data);
        ptr = ptr->next;
    }
    printf("%d", ptr->data);
}

void displayReverse(struct Node *head)
{
    struct Node *ptr = head->next, *prev = head, *tail;
    while(ptr != head)
    {
        prev = ptr;
        ptr = ptr->next;
    }
    ptr = prev;
    tail = prev;
    do
    {
        printfA("%d ", ptr->data);
        ptr = ptr->prev;
    } while (ptr != tail);
}

struct Node* getNode(struct Node *head, int N)
{
    int ctr =1;
    struct Node *ptr = head;
    while(ctr < N)
    {
        ptr = ptr->next;
        ctr++;
    }
    return ptr;
}


struct Node* insertNodeAtMiddle(struct Node *head, int data)
{


}



int main(){
    int totalNodes, data;
    scanf("%d",&totalNodes);
    for(int ctr = 1; ctr <= totalNodes; ctr++)
    {
        scanf("%d",&data);
        append(data);
    }
    scanf("%d",&data);
    struct Node *middleNodePrev, *middleNodeNext;
    middleNodePrev = getNode(head, totalNodes/2);
    middleNodeNext = middleNodePrev->next;

    struct Node *ptr = insertNodeAtMiddle(head, data);
    struct Node *middleNode = getNode(ptr, (totalNodes/2)+1);
    if((middleNode->prev != middleNodePrev) || middleNode->next != middleNodeNext)
    {
        printf("Node not inserted properly in the middle of CDLL\n");

    }
    printf("CDLL:\n");
    display(ptr);
    printf("\n");
    displayReverse(ptr);
    return 0;


}
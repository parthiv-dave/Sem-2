#include<stdio.h>
#include<stdlib.h>

struct node 
{
    int data;
    struct node *next;
};
void createlist(struct node **head,int data)
{
    struct node *newNode = (struct node*)malloc(sizeof(struct node));
    newNode -> data = data;
    newNode -> next = NULL;
    
    if(*head == NULL)
    {
        *head = newNode;
    }
    else
    {
        struct node *temp=*head;
        while(temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next=newNode;
    }
}

void printlist(struct node **head)
{
    struct node *temp = *head;
    while(temp!= NULL)
    {
        printf("%d -> ",temp->data);
        temp = temp -> next;
    }
    printf("NULL");
}

void insertatindex(struct node **head,int data,int index)
{
    struct node *newNode = (struct node*)malloc(sizeof(struct node));

    newNode -> data = data;
    newNode -> next = NULL;

    if(index == 0)
    {
        newNode -> next = *head;
        *head = newNode;
        return;
    }

    else
    {
        int count=0;
        struct node * temp = *head;
        while(count<index-1)
        {
            temp = temp -> next;
            count++;
        }
        newNode -> next = temp -> next;
        temp -> next = newNode;
    }
}

int main()
{
    struct node *head=NULL;
    int n,data,index;

    printf("Enter No. of elements in linked list = ");
    scanf("%d",&n);

    int a[n];
    for(int i=0 ; i<n ; i++)
    {
        printf("Enter %d element = ",i+1);
        scanf("%d",&a[i]);
        createlist(&head,a[i]);
    }

    printlist(&head);

    printf("\nEnter data and index to add in linked list = ");
    scanf("%d %d",&data,&index);

    insertatindex(&head,data,index);

    printlist(&head);

    //Exeption not included like index > linked list size
}
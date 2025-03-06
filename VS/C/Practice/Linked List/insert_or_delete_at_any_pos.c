#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

void createlist(struct node **head,int data)
{
    struct node *temp = *head , *newNode = NULL;
    newNode=(struct node*)malloc(sizeof(struct node));

    newNode->data = data;
    newNode->next = NULL;

    if(*head == NULL)
    {
        *head = newNode;
    }
    else
    {
        while(temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void displaylist(struct node **head)
{
    struct node *temp = *head;
    while(temp != NULL)
    {
        printf("%d -> ",temp->data);
        temp = temp->next;
    }
    printf("NULL");
}

void insertatbeg(struct node **head,int data)
{
    struct node *newNode;

    newNode=(struct node*)malloc(sizeof(struct node));

    newNode->data = data;
    newNode->next = NULL;

    newNode->next = *head;
    *head = newNode;
}

void insertatpos(struct node **head,int data,int index)
{   if(index > 0)
    {
        int count=0;
        struct node *newNode ,*temp = *head;

        newNode=(struct node*)malloc(sizeof(struct node));

        newNode->data = data;
        newNode->next = NULL;

        while(count != index-1)
        {
            temp = temp->next;
            count++;
        }

        newNode->next = temp->next;
        temp->next = newNode;
    }
    else
    {
        printf("index 0 isn't possible");
    }
}

void deleteatbeg(struct node **head)
{
    struct node *temp = *head;
    
    *head = temp->next;
    free(temp);
}

void deleteatpos(struct node**head,int index)
{
    struct node *temp = *head;

    for(int i=0 ; i<index-1 ; i++)
    {
        temp = temp->next;
    }

    temp->next = temp->next->next;
}

int main()
{
    struct node *head = NULL;
    int n,choice,data,index;

    printf("Enter No. of elements in linked list = ");
    scanf("%d",&n);

    int arr[n];

    for(int i=0 ; i<n ; i++)
    {
        printf("Enter %d element = ",i+1);
        scanf("%d",&arr[i]);

        createlist(&head,arr[i]);
    }

    while(choice != 6)
    {
        printf("\n1. Insert at Beginning ");
        printf("\n2. Insert at Index ");
        printf("\n3. Delete at Beginning ");
        printf("\n4. Delete at Position ");
        printf("\n5. Display");
        printf("\n6. Exit ");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1:
                printf("Enter element to insert at beginning = ");
                scanf("%d",&data);
                insertatbeg(&head,data);
                break;
            case 2:
                printf("Enter element and index to insert = ");
                scanf("%d %d",&data,&index);
                insertatpos(&head,data,index);
                break;
            case 3:
                deleteatbeg(&head);
                break;
            case 4:
                printf("Enter index to delete node = ");
                scanf("%d",&index);
                deleteatpos(&head,index);
                break;
            case 5:
                displaylist(&head);
                break;
            case 6:
                return 0;
                break;
            default:
                printf("Invalid Index Entered");
                break;
        }
    }
}
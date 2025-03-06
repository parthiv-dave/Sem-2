#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
}*topNode = NULL;

int isempty()
{
    if(topNode == NULL)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void push(int data)
{
    struct node *newNode = NULL;
    newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = NULL;

    newNode->next = topNode;
    topNode = newNode;    
}

void pop()
{
    if(isempty())
    {
        printf("\nUnder Flow");
    }
    else
    {
    struct node *temp = topNode;
    topNode = temp->next;
    
    printf("\nPopped element = %d",temp->data);

    free(temp);
    }
}

void preek()
{
    struct node *temp = topNode;

    if(temp == NULL)
    {
        printf("\nStack is Empty");
    }
    
    else
    {
        printf("\nStack :\n");
        while(temp != NULL)
    {
        printf("%d \n",temp->data);
        temp = temp->next;
    }
    }
}

int main()
{
    int choice,data;
    while(choice != 4)
    {
        printf("\n1. Push\n");
        printf("2. Pop\n");
        printf("3. Preek\n");
        printf("4. Exit\n");
        printf("Enter your choice : ");
        scanf("%d",&choice);
        
        switch(choice)
        {
            case 1:
                printf("\nEnter element to be pushed = ");
                scanf("%d",&data);
                push(data);
                break;
            case 2:
                pop();
                break;
            case 3:
                preek();
                break;
            case 4:
                return 0;
                break;
            default:
                printf("Invalid Choice");

        }

    }
}
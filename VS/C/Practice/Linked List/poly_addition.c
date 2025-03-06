#include<stdio.h>
#include<stdlib.h>

struct node
{
    int cof;
    int exp;
    struct node *next;
};

void createlist(struct node **head,int data1,int data2)
{
    struct node *temp = *head , *newNode = (struct node*)malloc(sizeof(struct node));
    newNode->cof = data1;
    newNode->exp = data2;
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
        printf("%dx^%d",temp->cof,temp->exp);

        temp = temp->next;

        if(temp != NULL)
        {
            printf(" + ");
        }    
    }
}

int main()
{
    struct node *poly1 = NULL , *poly2 = NULL;
    int n1,n2;

    printf("\nEnter No. of terms in Polynomial 1 = ");
    scanf("%d",&n1);

    printf("Enter Polynomial 1 : \n");
    for(int i=0 ; i<n1 ; i++)
    {
        int coff,expo;

        printf("\nEnter %d Term : \n",i+1);

        printf("Coefficient = ");
        scanf("%d",&coff);

        printf("Exponant = ");
        scanf("%d",&expo);

        createlist(&poly1,coff,expo);
    }

    printf("\nEnter No. of terms in Polynomial 2 = ");
    scanf("%d",&n2);
    
    printf("Enter Polynomial 2 : \n");
    for(int i=0 ; i<n2 ; i++)
    {
        int coff,expo;

        printf("\nEnter %d Term = \n",i+1);

        printf("Coefficient = ");
        scanf("%d",&coff);

        printf("Exponant = ");
        scanf("%d",&expo);

        createlist(&poly2,coff,expo);
    }

    printf("\nPolynomial 1 : \n");
    displaylist(&poly1);
    printf("\nPolynomial 2 : \n");
    displaylist(&poly2);
}
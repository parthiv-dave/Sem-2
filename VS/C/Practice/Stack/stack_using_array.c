#include<stdio.h>
int top = -1;

void push(int arr[],int data,int n)
{   
    if(top == n-1)
    {
        printf("\nOver Flow \n");
    }

    else
    {
        arr[++top] = data;
    }
}

void preek(int arr[])
{   
    if(top == -1)
    {
        printf("\nStack is Empty\n");
    }

    else
    {
        printf("\nStack :\n");

        for(int i=top ; i>=0 ; i--)
        {
            printf("%d\n",arr[i]);
        }
    }
}

void pop(int arr[])
{   
    if(top == -1)
    {
        printf("\nUnder Flow \n");
    }
    else
    {
        printf("\nPopped Element = %d\n",arr[top]);
        top--;
    }
}

int main()
{
    int n,choice,data;
    printf("\nEnter No. of Elements of Stacks = ");
    scanf("%d",&n);
    int arr[n];

    while(choice != 4)
    {
        printf("\n1. Push\n");
        printf("2. Pop\n");
        printf("3. Preek\n");
        printf("4. Exit\n");
        printf("Enter Your choice : ");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1:
                printf("Enter Element to Push into stack = ");
                scanf("%d",&data);
                push(arr,data,n);
                break;
            case 2:
                pop(arr);
                break;
            case 3:
                preek(arr);
                break;
            case 4:
                return 0;
            default:
                printf("Invalid Choice");    
                break;        
        }
    }
}
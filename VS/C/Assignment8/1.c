#include<stdio.h>
#include<stdlib.h>
#define size 5

struct queue 
{
    int data[size];
    int front,rear;
};

void initqueue(struct queue *q)
{
    q->front = -1;
    q->rear = -1;
}

int isfull(struct queue *q)
{
    if(q->rear == size - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isempty(struct queue *q)
{
    if(q->front == -1 || q->front > q->rear)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void enqueue(struct queue *q,int value)
{
    if(isfull(q))
    {
        printf("\nQueue is Full");
    }
   
    if(isempty(q))
    {
        q->front = 0;
    }
    q->data[++q->rear] = value;
    
}

int dequeue(struct queue *q)
{
    if(isempty(q))
    {
        printf("\nQueue is Empty");
    }
    else
    {
        return q->data[q->front++];
    }
}

int preek(struct queue *q)
{
    if(isempty(q))
    {
        printf("\nQueue is Empty");
    }
    else
    {
        return q->data[q->front];
    }
}

int main()
{
    struct queue q;
    int choice,data;
    initqueue(&q);

    while(choice != 4)
    {
        printf("\n1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Preek\n");
        printf("4. Exit\n");
        printf("Enter Your choice : ");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1:
                printf("Enter Element to Enqueue into Queue = ");
                scanf("%d",&data);
                enqueue(&q,data);
                break;
            case 2:
                data = dequeue(&q);
                printf("%d",data);
                break;
            case 3:
                data = preek(&q);
                printf("%d",data);
                break;
            case 4:
                return 0;
            default:
                printf("Invalid Choice");    
                break;        
        }
    }
}
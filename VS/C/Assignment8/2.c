#include <stdio.h>
#include <stdlib.h>

#define SIZE 5  

struct CircularQueue {
    int data[SIZE];
    int front, rear;
};

void initQueue(struct CircularQueue *q) {
    q->front = -1;
    q->rear = -1;
}

int isFull(struct CircularQueue *q) {
    return ((q->rear + 1) % SIZE == q->front);
}

int isEmpty(struct CircularQueue *q) {
    return (q->front == -1);
}

void enqueue(struct CircularQueue *q, int value) {
    if (isFull(q)) {
        printf("\nQueue is Full\n");
        return;
    }
    
    if (isEmpty(q)) {
        q->front = 0;
    }

    q->rear = (q->rear + 1) % SIZE;
    q->data[q->rear] = value;
    printf("\nInserted %d\n", value);
}

int dequeue(struct CircularQueue *q) {
    if (isEmpty(q)) {
        printf("\nQueue is Empty\n");
        return -1;
    }

    int value = q->data[q->front];

    if (q->front == q->rear) {
        q->front = q->rear = -1;
    } else {
        q->front = (q->front + 1) % SIZE;
    }

    return value;
}

int peek(struct CircularQueue *q) {
    if (isEmpty(q)) {
        printf("\nQueue is Empty\n");
        return -1;
    }
    return q->data[q->front];
}

int main() {
    struct CircularQueue q;
    int choice, data;
    initQueue(&q);

    while (1) {
        printf("\n1. Enqueue\n2. Dequeue\n3. Peek\n4. Exit\nEnter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter element: ");
                scanf("%d", &data);
                enqueue(&q, data);
                break;
            case 2:
                data = dequeue(&q);
                if (data != -1) {
                    printf("\nRemoved: %d\n", data);
                }
                break;
            case 3:
                data = peek(&q);
                if (data != -1) {
                    printf("\nFront Element: %d\n", data);
                }
                break;
            case 4:
                exit(0);
            default:
                printf("\nInvalid choice\n");
        }
    }
}

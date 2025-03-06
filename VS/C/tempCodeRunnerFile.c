#include <stdio.h>
#include <stdlib.h>

#define SIZE 5

// Regular Queue Implementation
struct Queue {
    int items[SIZE];
    int front, rear;
};

void initQueue(struct Queue *q) {
    q->front = -1;
    q->rear = -1;
}

int isFull(struct Queue *q) {
    return q->rear == SIZE - 1;
}

int isEmpty(struct Queue *q) {
    return q->front == -1 || q->front > q->rear;
}

void enqueue(struct Queue *q, int value) {
    if (isFull(q)) {
        printf("Queue is full!\n");
        return;
    }
    if (isEmpty(q)) q->front = 0;
    q->items[++q->rear] = value;
}

int dequeue(struct Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty!\n");
        return -1;
    }
    return q->items[q->front++];
}

int peek(struct Queue *q) {
    return isEmpty(q) ? -1 : q->items[q->front];
}

// Circular Queue Implementation
struct CircularQueue {
    int items[SIZE];
    int front, rear;
};

void initCircularQueue(struct CircularQueue *cq) {
    cq->front = -1;
    cq->rear = -1;
}

int isCircularFull(struct CircularQueue *cq) {
    return (cq->rear + 1) % SIZE == cq->front;
}

int isCircularEmpty(struct CircularQueue *cq) {
    return cq->front == -1;
}

void enqueueCircular(struct CircularQueue *cq, int value) {
    if (isCircularFull(cq)) {
        printf("Circular Queue is full!\n");
        return;
    }
    if (isCircularEmpty(cq)) cq->front = 0;
    cq->rear = (cq->rear + 1) % SIZE;
    cq->items[cq->rear] = value;
}

int dequeueCircular(struct CircularQueue *cq) {
    if (isCircularEmpty(cq)) {
        printf("Circular Queue is empty!\n");
        return -1;
    }
    int value = cq->items[cq->front];
    if (cq->front == cq->rear) {
        cq->front = -1;
        cq->rear = -1;
    } else {
        cq->front = (cq->front + 1) % SIZE;
    }
    return value;
}

int peekCircular(struct CircularQueue *cq) {
    return isCircularEmpty(cq) ? -1 : cq->items[cq->front];
}

int main() {
    struct Queue q;
    initQueue(&q);
    enqueue(&q, 10);
    enqueue(&q, 20);
    printf("Front element: %d\n", peek(&q));
    printf("Dequeued: %d\n", dequeue(&q));
    
    struct CircularQueue cq;
    initCircularQueue(&cq);
    enqueueCircular(&cq, 30);
    enqueueCircular(&cq, 40);
    printf("Front element in Circular Queue: %d\n", peekCircular(&cq));
    printf("Dequeued from Circular Queue: %d\n", dequeueCircular(&cq));
    
    return 0;
}

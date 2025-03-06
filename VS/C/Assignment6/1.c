#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int stack[MAX], top = -1;

void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = value;
}

int pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack[top--];
}

void peek() {
    if (top == -1) {
        printf("Stack is empty\n");
        return;
    }
    for (int i = top; i >= 0; i--)
        printf("%d ", stack[i]);
    printf("\n");
}

struct Node {
    int data;
    struct Node* next;
};

struct Node* topNode = NULL;

void pushList(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = topNode;
    topNode = newNode;
}

int popList() {
    if (topNode == NULL) {
        printf("Stack Underflow\n");
        return -1;
    }
    struct Node* temp = topNode;
    int value = temp->data;
    topNode = topNode->next;
    free(temp);
    return value;
}

void peekList() {
    struct Node* temp = topNode;
    if (temp == NULL) {
        printf("Stack is empty\n");
        return;
    }
    while (temp) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    int choice, value;
    do {
        printf("\nStack Operations:\n");
        printf("1. Push (Array)\n2. Pop (Array)\n3. Peek (Array)\n");
        printf("4. Push (Linked List)\n5. Pop (Linked List)\n6. Peek (Linked List)\n7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to push: ");
                scanf("%d", &value);
                push(value);
                break;
            case 2:
                printf("Popped: %d\n", pop());
                break;
            case 3:
                peek();
                break;
            case 4:
                printf("Enter value to push: ");
                scanf("%d", &value);
                pushList(value);
                break;
            case 5:
                printf("Popped: %d\n", popList());
                break;
            case 6:
                peekList();
                break;
            case 7:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice, try again.\n");
        }
    } while (choice != 7);

    return 0;
}
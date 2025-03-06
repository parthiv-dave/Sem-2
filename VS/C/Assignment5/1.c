#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *head = NULL, *redoStack = NULL;

void insertAtIndex(int data, int index);
void insertAtBeginning(int data);
void insertAtEnd(int data);
void deleteAtIndex(int index);
void deleteAtBeginning();
void deleteAtEnd();
void display();
void pushRedo(int data);
int popRedo();
void undo();
void redo();

int main() {
    int choice, data, index;
    
    while (1) {
        printf("\n1. Insert at Index\n2. Insert at Beginning\n3. Insert at End\n4. Delete at Index\n5. Delete at Beginning\n6. Delete at End\n7. Undo\n8. Redo\n9. Display\n10. Exit\nEnter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data and index: ");
                scanf("%d %d", &data, &index);
                insertAtIndex(data, index);
                break;
            case 2:
                printf("Enter data: ");
                scanf("%d", &data);
                insertAtBeginning(data);
                break;
            case 3:
                printf("Enter data: ");
                scanf("%d", &data);
                insertAtEnd(data);
                break;
            case 4:
                printf("Enter index: ");
                scanf("%d", &index);
                deleteAtIndex(index);
                break;
            case 5:
                deleteAtBeginning();
                break;
            case 6:
                deleteAtEnd();
                break;
            case 7:
                undo();
                break;
            case 8:
                redo();
                break;
            case 9:
                display();
                break;
            case 10:
                exit(0);
            default:
                printf("Invalid choice!\n");
        }
    }
    return 0;
}

void insertAtIndex(int data, int index) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;

    if (head == NULL) {
        newNode->next = newNode;
        head = newNode;
        return;
    }

    Node *temp = head;
    for (int i = 0; temp->next != head && i < index - 1; i++) {
        temp = temp->next;
    }

    newNode->next = temp->next;
    temp->next = newNode;
}

void insertAtBeginning(int data) {
    insertAtIndex(data, 0);
}

void insertAtEnd(int data) {
    insertAtIndex(data, -1);
}

void deleteAtIndex(int index) {
    if (head == NULL) return;

    Node *temp = head, *prev = NULL;

    for (int i = 0; temp->next != head && i < index; i++) {
        prev = temp;
        temp = temp->next;
    }

    if (prev) {
        prev->next = temp->next;
    } else {
        head = temp->next;
    }

    pushRedo(temp->data);
    free(temp);
}

void deleteAtBeginning() {
    deleteAtIndex(0);
}

void deleteAtEnd() {
    deleteAtIndex(-1);
}

void display() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    Node *temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(circular)\n");
}

void undo() {
    if (!redoStack) return;
    int data = popRedo();
    insertAtEnd(data);
}

void redo() {
    if (!redoStack) return;
    int data = popRedo();
    insertAtEnd(data);
}

void pushRedo(int data) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = redoStack;
    redoStack = newNode;
}

int popRedo() {
    if (!redoStack) return -1;
    Node *temp = redoStack;
    redoStack = redoStack->next;
    int data = temp->data;
    free(temp);
    return data;
}
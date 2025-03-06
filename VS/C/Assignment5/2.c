#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int coeff, exp;
    struct Node *next;
} Node;

Node *createNode(int coeff, int exp) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->coeff = coeff;
    newNode->exp = exp;
    newNode->next = NULL;
    return newNode;
}

void insert(Node **poly, int coeff, int exp) {
    Node *newNode = createNode(coeff, exp), *temp = *poly;
    if (!(*poly) || (*poly)->exp < exp) {
        newNode->next = *poly;
        *poly = newNode;
        return;
    }
    while (temp->next && temp->next->exp >= exp)
        temp = temp->next;
    newNode->next = temp->next;
    temp->next = newNode;
}

Node *addPolynomials(Node *poly1, Node *poly2) {
    Node *result = NULL;
    while (poly1 || poly2) {
        int coeff = 0, exp = 0;
        if (poly1 && (!poly2 || poly1->exp > poly2->exp)) {
            coeff = poly1->coeff;
            exp = poly1->exp;
            poly1 = poly1->next;
        } else if (poly2 && (!poly1 || poly1->exp < poly2->exp)) {
            coeff = poly2->coeff;
            exp = poly2->exp;
            poly2 = poly2->next;
        } else {
            coeff = poly1->coeff + poly2->coeff;
            exp = poly1->exp;
            poly1 = poly1->next;
            poly2 = poly2->next;
        }
        insert(&result, coeff, exp);
    }
    return result;
}

void display(Node *poly) {
    while (poly) {
        printf("%dx^%d ", poly->coeff, poly->exp);
        poly = poly->next;
        if (poly) printf("+ ");
    }
    printf("\n");
}

int main() {
    Node *poly1 = NULL, *poly2 = NULL;
    int terms, coeff, exp;

    printf("Enter number of terms for first polynomial: ");
    scanf("%d", &terms);
    for (int i = 0; i < terms; i++) {
        printf("Enter coefficient and exponent: ");
        scanf("%d %d", &coeff, &exp);
        insert(&poly1, coeff, exp);
    }

    printf("Enter number of terms for second polynomial: ");
    scanf("%d", &terms);
    for (int i = 0; i < terms; i++) {
        printf("Enter coefficient and exponent: ");
        scanf("%d %d", &coeff, &exp);
        insert(&poly2, coeff, exp);
    }

    Node *sum = addPolynomials(poly1, poly2);
    printf("Sum: ");
    display(sum);
    return 0;
}
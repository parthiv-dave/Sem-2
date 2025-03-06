#include <stdio.h>
#include <stdlib.h>

struct Term {
    int coeff;
    int exp;
    struct Term* next;
};

struct Term* createTerm(int coeff, int exp) {
    struct Term* newTerm = (struct Term*)malloc(sizeof(struct Term));
    newTerm->coeff = coeff;
    newTerm->exp = exp;
    newTerm->next = NULL;
    return newTerm;
}

void insertTerm(struct Term** poly, int coeff, int exp) {
    struct Term* newTerm = createTerm(coeff, exp);
    newTerm->next = *poly;
    *poly = newTerm;
}

void displayPoly(struct Term* poly) {
    while (poly) {
        printf("%dx^%d", poly->coeff, poly->exp);
        poly = poly->next;
        if (poly)
            printf(" + ");
    }
    printf("\n");
}

struct Term* multiplyPolynomials(struct Term* poly1, struct Term* poly2) {
    struct Term* result = NULL;
    
    for (struct Term* p1 = poly1; p1; p1 = p1->next) {
        for (struct Term* p2 = poly2; p2; p2 = p2->next) {
            int coeff = p1->coeff * p2->coeff;
            int exp = p1->exp + p2->exp;
            
            struct Term* temp = result;
            struct Term* prev = NULL;
            while (temp && temp->exp > exp) {
                prev = temp;
                temp = temp->next;
            }
            if (temp && temp->exp == exp) {
                temp->coeff += coeff;
            } else {
                struct Term* newTerm = createTerm(coeff, exp);
                newTerm->next = temp;
                if (prev)
                    prev->next = newTerm;
                else
                    result = newTerm;
            }
        }
    }
    return result;
}

int main() {
    struct Term* poly1 = NULL;
    struct Term* poly2 = NULL;
    int n, coeff, exp;
    
    printf("Enter number of terms in first polynomial: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Enter coefficient and exponent: ");
        scanf("%d %d", &coeff, &exp);
        insertTerm(&poly1, coeff, exp);
    }
    
    printf("Enter number of terms in second polynomial: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Enter coefficient and exponent: ");
        scanf("%d %d", &coeff, &exp);
        insertTerm(&poly2, coeff, exp);
    }
    
    printf("Polynomial 1: ");
    displayPoly(poly1);
    printf("Polynomial 2: ");
    displayPoly(poly2);
    
    struct Term* result = multiplyPolynomials(poly1, poly2);
    printf("Resultant Polynomial: ");
    displayPoly(result);
    
    return 0;
}

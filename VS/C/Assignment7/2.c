#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX 100  

struct Stack {
    int top;
    int items[MAX];
};

void initStack(struct Stack *s) {
    s->top = -1;
}

int isEmpty(struct Stack *s) {
    return s->top == -1;
}

void push(struct Stack *s, int item) {
    if (s->top == MAX - 1) {
        printf("Stack Overflow\n");
        exit(EXIT_FAILURE);
    }
    s->items[++(s->top)] = item;
}

int pop(struct Stack *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow\n");
        exit(EXIT_FAILURE);
    }
    return s->items[(s->top)--];
}

int evaluatePostfix(char *postfix) {
    struct Stack s;
    initStack(&s);

    char *token = strtok(postfix, " ");  

    while (token != NULL) {
        if (isdigit(token[0]) || (token[0] == '-' && isdigit(token[1]))) {
            push(&s, atoi(token));
        } 
        else { 
            if (isEmpty(&s)) {
                printf("Error: Not enough operands\n");
                exit(EXIT_FAILURE);
            }
            int val2 = pop(&s);
            
            if (isEmpty(&s)) {
                printf("Error: Not enough operands\n");
                exit(EXIT_FAILURE);
            }
            int val1 = pop(&s);

            switch (token[0]) {
                case '+': push(&s, val1 + val2); break;
                case '-': push(&s, val1 - val2); break;
                case '*': push(&s, val1 * val2); break;
                case '/': 
                    if (val2 == 0) {
                        printf("Error: Division by zero\n");
                        exit(EXIT_FAILURE);
                    }
                    push(&s, val1 / val2); 
                    break;
                default:
                    printf("Error: Invalid operator %c\n", token[0]);
                    exit(EXIT_FAILURE);
            }
        }
        token = strtok(NULL, " ");  
    }

    if (!isEmpty(&s)) {
        int result = pop(&s);
        if (!isEmpty(&s)) {
            printf("Error: Too many operands\n");
            exit(EXIT_FAILURE);
        }
        return result;
    } else {
        printf("Error: No operands found\n");
        exit(EXIT_FAILURE);
    }
}

int main() {
    char postfix[MAX];

    printf("Enter a postfix expression : ");
    fgets(postfix, sizeof(postfix), stdin);

    size_t len = strlen(postfix);
    if (len > 0 && postfix[len - 1] == '\n') {
        postfix[len - 1] = '\0';
    }

    int result = evaluatePostfix(postfix);
    printf("Evaluated Result: %d\n", result);

    return 0;
}

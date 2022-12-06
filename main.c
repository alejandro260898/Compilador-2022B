#include <stdio.h>

int c;

int suma(int a, int b) { 
    return a + b;
}

int main() { 
    c = suma(1,2);
    printf("c = %i", c);

    return 0;
}
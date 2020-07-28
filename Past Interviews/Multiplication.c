#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int add(int a, int b) {
    int c;
    while (a != 0) {
        c = b & a;
        b = b ^ a;
        c = c << 1;
        a = c;
    }
    return b;
}

int mult(int a, int b) {
    int i = 0;
    int c = 0;
    while (i < b) {
        c = add(c, a);
        i = add(i, 1);
    }
    return c;
}

int main(){
    int x = 4;
    int y = 1;
    int res = add(x,y);
    printf("%d",res);
}



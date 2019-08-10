#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
  int a,b,max=-10000;

  scanf("%d %d", &a, &b);

  if (a+b > max) {
    max = a+b;
  }
  if (a-b > max) {
    max = a-b;
  }
  if (a*b > max) {
    max = a*b;
  }

  printf("%d\n", max);
  return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
  int x;

  scanf("%d", &x);

  printf("%.10f\n", (double)(x - x/2)/ (double)(x));
  return 0;
}
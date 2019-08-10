#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
  int k, x, i;

  scanf("%d %d", &k, &x);

  for (i = x-k+1; i < x+k-1; i++) {
    printf("%d ", i);
  }
  printf("%d\n", i);
  return 0;
}

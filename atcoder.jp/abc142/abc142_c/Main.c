#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
  int n,index,arr[100000];

  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%d", &index);
    arr[index-1] = i+1;
  }

  for (int i = 0; i < n-1; i++) {
    printf("%d ", arr[i]);
  }
  printf("%d\n", arr[n-1]);
  return 0;
}
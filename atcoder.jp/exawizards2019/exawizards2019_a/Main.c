#include <stdio.h>

int main(int argc, char const *argv[]) {
  int A,B,C;
  scanf("%d %d %d",&A,&B,&C);
  if (A == B && B == C && A > 0) {
    printf("Yes\n");
  } else {
    printf("No\n");
  }
  return 0;
}
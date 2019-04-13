#include <stdio.h>

int main(int argc, char const *argv[]) {
  int A,B,count=0;
  scanf("%d %d\n",&A,&B );

  if (A > B) {
    count += A;
    A--;
  } else {
    count += B;
    B--;
  }

  if (A > B) {
    count += A;
    A--;
  } else {
    count += B;
    B--;
  }
  printf("%d\n",count );
  return 0;
}

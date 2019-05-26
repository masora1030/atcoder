#include <stdio.h>

int main(int argc, char const *argv[]) {
  int A, P, ans=0;
  scanf("%d %d\n",&A,&P);

  ans = (A * 3 + P)/2;

  printf("%d\n",ans);
  
  return 0;
}
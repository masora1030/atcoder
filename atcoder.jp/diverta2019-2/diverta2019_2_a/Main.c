#include <stdio.h>
 
int main(int argc, char const *argv[]) {
  int N,K;
  scanf("%d %d\n", &N,&K);
  if (K > 1) {
    printf("%d\n",N - K);
  } else {
    printf("%d\n",0);
  }
  return 0;
}
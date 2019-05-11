#include <stdio.h>

int main(int argc, char const *argv[]) {
  int N,K,ans;

  scanf("%d %d\n", &N,&K);
  ans = N - K + 1;
  printf("%d\n",ans);
  return 0;
}
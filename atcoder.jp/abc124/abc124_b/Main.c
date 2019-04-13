#include <stdio.h>

int main(int argc, char const *argv[]) {
  int N,H,count=0,maxH=0;
  scanf("%d\n",&N);
  while (N > 0) {
    scanf("%d",&H);
    if (maxH <= H) {
      maxH = H;
      count++;
    }
    N--;
  }

  printf("%d\n",count);
  return 0;
}

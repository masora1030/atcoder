#include <stdio.h>

int main(int argc, char const *argv[]) {
  int R,G,B,N,ans=0,k1,k2,i,j,x1,x2;

  scanf("%d %d %d %d",&R,&G,&B,&N);
  k1 = N / R;
  for (i = k1; i >= 0; i--) {
    x1 = N - R*i;
    k2 = x1 / G;
      for (j = k2; j >= 0; j--) {
        x2 = x1 - G*j;
          if (x2 % B == 0) {
            ans++;
          }
    }
  }
  printf("%d\n", ans);
  return 0;
}
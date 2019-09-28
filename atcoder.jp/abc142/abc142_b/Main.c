#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
  int n,k,ans=0,h;

  scanf("%d %d", &n, &k);

  for (int i = 0; i < n; i++) {
    scanf("%d", &h);
    if (h >= k) {
      ans++;
    }
  }

  printf("%d\n", ans);
  return 0;
}
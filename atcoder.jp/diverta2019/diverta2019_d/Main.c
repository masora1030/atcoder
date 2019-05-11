#include <stdio.h>

int main(int argc, char const *argv[]) {
  long long int N, count=0, i, M;
  scanf("%lld", &N);
  for (i = 1; i*i <= N; i++) {
    if (N % i == 0) {
      M = N/i;
      if (i+2 <= M) {
        count += M-1;
      }
    }
  }
  printf("%lld\n", count);
  return 0;
}
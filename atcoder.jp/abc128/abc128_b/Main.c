#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
  int N, p[100], i,swap,j,key[100],k;
  char S[100][11], tmp[11];

  scanf("%d\n", &N);
  for (i = 0; i < N; i++) {
    scanf("%s ", S[i]);
    scanf("%d\n", &p[i]);
  }

  for (i = 0; i < N; i++) {
    key[i] = i+1;
  }

  for(i=1;i<N;i++){
    for(j=1;j<N;j++){
      if(strcmp(S[j-1], S[j])>0){
        strcpy(tmp, S[j-1]);
        strcpy(S[j-1], S[j]);
        strcpy(S[j], tmp);
        swap = p[j-1];
        p[j-1] = p[j];
        p[j] = swap;
        swap = key[j-1];
        key[j-1] = key[j];
        key[j] = swap;
      }
    }
  }

  for (i = 1; i < N; i++) {
    if (strcmp(S[i-1], S[i]) == 0) {
      for (j = i; strcmp(S[j-1], S[j]) == 0; j++) {
        for(k = i; strcmp(S[k-1], S[k]) == 0; k++){
          if(p[k-1] < p[k]){
            swap = p[k-1];
            p[k-1] = p[k];
            p[k] = swap;
            swap = key[k-1];
            key[k-1] = key[k];
            key[k] = swap;
          }
        }
      }
      i=j;
    }
  }

  for (i = 0; i < N; i++) {
    printf("%d\n",key[i]);
  }


  return 0;
}
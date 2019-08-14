#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, x, min=32, count=0;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> x;
    for (int j = x; j%2 == 0; j=j/2) {
      count++;
    }
    if (count < min) {
      min = count;
    }
    count = 0;
  }

  std::cout << min << '\n';

  return 0;
}

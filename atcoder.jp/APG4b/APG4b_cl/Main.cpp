#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n,a,ans;
  string op;
  
  cin >> n;
  cin >> a;
  ans = a;
  
  for (int i=0; i < n; i++) {
    cin >> op >> a;
    if (op == "+") {
      ans += a;
    } else if (op == "-") {
      ans -= a;
    } else if (op == "*") {
      ans *= a;
    } else {
      if (a == 0) {
        cout << "error" << endl;
        break;
      } else {
        ans /= a;
      }
    }
    cout << i+1 << ":" << ans << endl;
  }
}
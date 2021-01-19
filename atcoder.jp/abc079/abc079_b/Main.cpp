# include <bits/stdc++.h>
# define ll long long
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<ll> dp(n+1);
  dp[0] = 2;
  dp[1] = 1;
  for (int i=1; i<n; i++) {
    dp[i+1] = dp[i-1]+dp[i];
  }
  
  cout << dp[n] << endl;
  
  return 0;
}
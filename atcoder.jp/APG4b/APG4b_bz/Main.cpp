# include <bits/stdc++.h>
# define ll long long

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i=0; i < n; i++) {
    cin >> a.at(i);
  }
  
  map<int, int> mp;
  for (auto p : a) {
    if (mp.count(p)) {
      mp[p] += 1;
    } else {
      mp[p] = 1;
    }
  }
  
  int ans_k = -1;
  int ans_v = -1;
  
  for (auto p : mp) {
    auto k = p.first;
    auto v = p.second;
    if (ans_v < v) {
      ans_k = k;
      ans_v = v;
    }
  }
  
  cout << ans_k << " " << ans_v << endl;
}
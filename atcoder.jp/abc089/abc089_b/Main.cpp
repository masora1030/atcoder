#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector <string> vec(n);
  for (int i=0; i < n; i++) {
    cin >> vec.at(i);
  }
  map <string, int> mp;
  mp["P"] = 0;
  mp["W"] = 0;
  mp["Y"] = 0;
  mp["G"] = 0;
    
  int ans = 0;
  
  for (int i=0; i < n; i++) {
    mp[vec[i]] = 1;
  }
  for(auto itr = mp.begin(); itr != mp.end(); ++itr) {
    ans += itr->second;
  }
  
  if (ans > 3) {
    cout << "Four" << endl;
  }  else {
    cout << "Three" << endl;
  }
  
  
}
#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for(int i=a;i<b;i++)
#define int long long
const int inf = 100100100100100;
const int mod = 1000000007;
const int tmp = 0;

const int maxn = 17;
int n;
int dist[maxn][maxn];
vector<vector<int>> xyz;
int dp[1<<maxn][maxn];

int dfs(int s, int v){

    if(dp[s][v] >= 0){
        return dp[s][v];
    }

    if(s == (1<<n)-1 && v == 0){
        return dp[s][v] = 0;
    }

    int ans = inf;
    rep(u,0,n){
        if(!(s >> u & 1)){
            ans = min(ans, dfs(s | 1 << u, u) + dist[v][u]);
        }
    }

    dp[s][v] = ans;
    return ans;


}

signed main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    
    cin >> n;
  
  	xyz.resize(maxn);
    for(size_t i=0; i<maxn; i++){
      xyz[i].resize(3);
    }

    memset(dp,-1,sizeof(dp));
    fill(dist[0],dist[0]+maxn*maxn,inf);

    

    rep(i,0,n){
        int x, y, z;
        cin >> x >> y >> z;
      	xyz[i][0] = x;
        xyz[i][1] = y;
        xyz[i][2] = z;
    }
    
    rep(i,0,n) {
        rep(j,0,n) {
            if(i!=j){
                dist[i][j] = abs(xyz[j][0]-xyz[i][0]) + abs(xyz[j][1]-xyz[i][1]) + max(tmp,xyz[j][2]-xyz[i][2]);
            }
        }
    }
  
    int ans = dfs(0,0);
    cout << (ans == inf ? -1 : ans) << endl;

}
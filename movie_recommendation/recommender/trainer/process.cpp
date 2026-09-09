#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;
#define f first 
#define s second 
#define pb push_back

bool compare(pair<double,int> a,pair<double,int> b){
	if(a.f < b.f) return true;
	if(a.f == b.f) return a.s < b.s;
	return false;
}

int32_t main(int argc, char **argv){
	// the trainer directory is passed in by the caller so the data files are
	// found relative to the checkout rather than an absolute path
	string dir = (argc > 1) ? argv[1] : ".";
	if(!dir.empty() && dir.back() != '/') dir += '/';

	freopen((dir + "test_file.txt").c_str(),"r",stdin);
	freopen((dir + "test_out.txt").c_str(),"w",stdout);
	int n,m;
	cin>>n>>m;
	vector<pair<double,int>> v[n];
	pair<double,int> tmp;

	for(int i=0;i<n;++i){
		for(int j=0;j<m;++j){
			cin>>tmp.f;
			tmp.s = j+1;
			v[i].pb(tmp);
		}
		sort(v[i].begin(),v[i].end(),compare);
	}
	freopen((dir + "input.txt").c_str(),"r",stdin); // The Original Input file 
	double b4[n][m];
	for(int i=0;i<n;++i)
		for(int j=0;j<m;++j)cin>>b4[i][j];

	for(int i=0;i<n;++i){
		for(auto j=(int)v[i].size()-1;j>=0;--j)if(b4[i][v[i][j].s-1]==0){
			cout << v[i][j].s << ' ';
		}
		cout << endl;
	}

	return 0;	
}
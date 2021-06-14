#include<iostream>
using namespace std;
int main() {
	int t,w,h,n;
	cin >> t;
	for (int test=0; test < t; test++) {
		cin >> h >> w >> n;
		for (int wid = 0; wid < w; wid++) {
			for (int hig = h - 1; hig >= 0; hig--) {
				n--;
				if (n == 0) {
					cout<<((h-hig)*100)+wid+1<<endl;
				}
			}
		}
	}
}
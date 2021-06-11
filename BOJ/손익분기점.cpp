#include <iostream>
#include <string>
using namespace std;

int main() {
	int a, b, c;
	cin >> a >> b >> c;
	int cost = 0;
	cost = c - b;
	if (cost <= 0) cout << "-1" << endl;
	else cout << a / cost + 1;
}
#include<iostream>
#include<string>
using namespace std;

int main() {
	int num;
	int sum = 0;
	string str = "";
	cin >> num;
	cin >> str;
	for (int i = 0; i < num; i++) {
		sum += str[i]-'0';
	}
	cout << sum << endl;
}
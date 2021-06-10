#include <iostream>
#include <string>

using namespace std;
int self(int n) {
	string str = to_string(n);
	int sum = n;
	for (int i = 0; i < str.length(); i++)
		sum += str[i]-48;
	return sum;
}
int main() {
	bool not_self_number[10001] = { false };
	for (int i=1;i<10001;i++){
		int res = self(i);
		if (res < 10000) 
			not_self_number[res] = true;

	}

	for (int i = 1; i < 10000; i++) {
		if (not_self_number[i] == false)
			cout  << i << endl;
	}
}
#include <iostream>
#include <string>
using namespace std;
int main() {
	int n;
	int score = 0;
	int score_stk = 0;
	string str = "";
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> str;
		for (int j = 0; j < str.length(); j++) {
			if (str[j] == 'O')
				score_stk += 1;
			if (str[j] == 'X')
				score_stk = 0;
			score += score_stk;
		}
		cout << score << endl;
		score = 0;
		score_stk = 0;
	}
}
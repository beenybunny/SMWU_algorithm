#include <iostream>
#include <vector>
#include <algorithm>
#define MAX_ATM 1000
using namespace std;


void atm() {
	int n, sum=0, waiting=0;
	vector<int> times_vec;

	cin >> n;
    int b;
	for (int i = 0; i < n; i++) {
		cin >> b;
		times_vec.push_back(b);	
	}
	sort(times_vec.begin(), times_vec.end());

	for (int i = 0; i < n; i++) {
		sum += times_vec[i] + waiting;
		waiting += times_vec[i];
	}
	cout << sum;
}

int main(){
    atm();
    return 0;
}
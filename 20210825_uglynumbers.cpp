// Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. 
// Given a number n, the task is to find n’th Ugly number.

// Examples:  

// Input  : n = 7
// Output : 8

// Input  : n = 10
// Output : 12

// Input  : n = 15
// Output : 24

// Input  : n = 150
// Output : 5832

int getNthUglyNo(int n){
	lookup[0] = 1;
	int i2, i3, i5 = 0;
	for(int i=1; i<n; i++){
		int mul2, mul3, mul5;
		mul2 = lookup[i2]*2;
		mul3 = lookup[i3]*3;
		mul5 = lookup[i5]*5;
		lookup[i] = min(mul2, min(mul3, mul5));
		// cout << lookup[i] << endl;

		if(lookup[i] == mul2){
			i2++;
		}
		if(lookup[i] == mul3){
			i3++;
		}
		if(lookup[i] == mul5){
			i5++;
		}
	}
	return lookup[n-1];
}

int main(){
	int result = getNthUglyNo(10);
	cout << result << endl;
}

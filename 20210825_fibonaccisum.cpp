#include <iostream>
#include <time.h>

using namespace std;

#define NIL -1
#define MAX 100

int lookup[MAX];

void _initialize(){
	for(int i=0; i<MAX; i++){
		lookup[i] = NIL;
	}
}

int fib(int n){
	if(lookup[n] == NIL){
		if(n <2){
			lookup[n] = n;
		}else{
			lookup[n] = fib(n-1) + fib(n-2);
		}
	}
	return lookup[n];
}

int fib2(int n){
	lookup[0], lookup[1] = 0, 1;
	for(int i=2; i<n; i++){
		lookup[i] = lookup[i-2] + lookup[i-1];
	}
	return lookup[n];
}

int fib3(int n){
	int n1=0;
	int n2=1;
	for(int i=2; i<=n; i++){
		int sum = n1 + n2;
		n1 = n2;
		n2 = sum;
	}
	return n2;
}

int main(){
	_initialize();
	clock_t begin, end;
	begin = clock();
	int result = fib3(8);
	end = clock();
	cout << result << endl;
	cout << (double)(end-begin)/CLOCKS_PER_SEC << endl;
}


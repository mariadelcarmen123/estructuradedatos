#include <iostream>

using namespace std;

int factorial(int n);

int main()
{
	int fact, n;
	do {
		cout << "Ingrese el valor de n: ";
		cin >> n;
	} while (n < 0);
	fact = factorial(n);
	cout << n << "!=" << fact << endl;
	return 0;
}

int factorial(int n) {
	if (n == 0)
		return 1;
	else
		return n * factorial(n - 1);
}

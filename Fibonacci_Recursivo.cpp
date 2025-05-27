#include <iostream>

using namespace std;

int fibonacci(int n);

int main() {
	int n, serie;
	do {
		cout << "Ingrese cuantos numeros desea generar: ";
		cin >> n;
	} while (n < 0);
	serie = fibonacci(n);
	cout << "El ultimo numero de la serie Fiboancci es: " << serie << endl;
	return 0;
}

int fibonacci(int n) {
	if (n <= 1)
		return n;
	else
		return fibonacci(n - 1) + fibonacci(n - 2);
}

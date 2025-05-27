#include <iostream>

using namespace std;

int sumaRecursiva(int n);

int main()
{
	int n, suma;
	do {
		cout << "Ingrese cuantos numeros quiere sumar: ";
		cin >> n;
	} while (n < 1);
	suma = sumaRecursiva(n);
	cout << "Suma de 1 hasta " << n << " es: " << suma << endl;
	return 0;
}

int sumaRecursiva(int n) {
	if (n == 1)
		return n;
	else
		return n + sumaRecursiva(n - 1);
}

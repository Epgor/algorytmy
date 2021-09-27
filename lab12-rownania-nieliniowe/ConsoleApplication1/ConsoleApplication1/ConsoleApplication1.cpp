/// Lab10.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.


#include <iostream>
#include <iomanip>
#include <math.h>

double p(double x)
{
	return 1;
}
double f(double x)
{
	double liczba;
	liczba = sqrt(3 + 4 * pow(x, 2));
	return liczba;
}
double legendre(double x, int n)
{
	if (n < 0)
	{
		return 0;
	}
	if (n == 0)
	{
		return 1;
	}
	else if (n == 1)
	{
		return x;
	}
	double liczba;
	liczba = (2 * (n - 1) + 1) * x*legendre(x, n - 1) / n;
	liczba -= (n - 1)*legendre(x, n - 2) / n;
	return liczba;
}
double phi(double x, int i)
{
	return legendre(x, i);
}
double cPoch(double x, int i, double(*fun)(double))
{
	return p(x)*phi(x, i)*fun(x);
}
double lambdaPoch(double x, int i, double(*fun)(double))
{

	return p(x)*(pow(phi(x, i), 2));
}
double xI(double a, double b, double n, int i)
{
	return (a + (i / n)*(b - a));
}

double metodaSimpsona(double a, double b, double n, int k, double(*fun)(double, int, double(*funin)(double)), double(*fu)(double))
{
	double h = (xI(a, b, n, 1) - a) / 2;
	double tI, suma;
	suma = fun(xI(a, b, n, 1), k, fu);
	suma += fun(xI(a, b, n, n), k, fu);
	for (int i = 0; i < n; i++)
	{
		tI = (xI(a, b, n, i + 1) + xI(a, b, n, i)) / 2;
		suma += (4 * fun(tI, k, fu));
	}
	for (int i = 1; i < n; i++)
	{
		suma += (2 * fun(xI(a, b, n, i), k, fu));
	}
	return suma * h / 3;
}
double lambdaI(double a, double b, int i, double(*fun)(double))
{
	return metodaSimpsona(a, b, 200, i, lambdaPoch, fun);
}
double cI(double a, double b, int i, double(*fun)(double))
{
	return metodaSimpsona(a, b, 200, i, cPoch, fun) / lambdaI(a, b, i, fun);
}
double Gx(double a, double b, double x, double(*fun)(double), double n)
{
	double suma = 0;
	for (int i = 0; i <= n; i++)
	{
		suma += cI(a, b, i, fun)*phi(x, i);
	}
	return suma;
}

int main()
{

	std::cout << std::setprecision(15) << Gx(-1, 1, -0.25, f, 7);

}

// Uruchomienie programu: Ctrl + F5 lub menu Debugowanie > Uruchom bez debugowania
// Debugowanie programu: F5 lub menu Debugowanie > Rozpocznij debugowanie

// Porady dotyczące rozpoczynania pracy:
//   1. Użyj okna Eksploratora rozwiązań, aby dodać pliki i zarządzać nimi
//   2. Użyj okna programu Team Explorer, aby nawiązać połączenie z kontrolą źródła
//   3. Użyj okna Dane wyjściowe, aby sprawdzić dane wyjściowe kompilacji i inne komunikaty
//   4. Użyj okna Lista błędów, aby zobaczyć błędy
//   5. Wybierz pozycję Projekt > Dodaj nowy element, aby utworzyć nowe pliki kodu, lub wybierz pozycję Projekt > Dodaj istniejący element, aby dodać istniejące pliku kodu do projektu
//   6. Aby w przyszłości ponownie otworzyć ten projekt, przejdź do pozycji Plik > Otwórz > Projekt i wybierz plik sln
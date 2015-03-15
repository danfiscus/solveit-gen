#include <iostream>
#include <math.h>
#include <time.h>
#include <cstdlib>

using namespace std;

int main()
{
	int s1,s2,s3,a1,a2,a3;
	srand(time(0));
	a1 = rand() % 178 + 1;
	cout << "Angle 1: " << a1 << endl;
	int x = 180-a1;
	a2 = rand() % x + 1;
	cout << "Angle 2: " << a2 << endl;
	a3 = 180-a1-a2;
	cout << "Angle 3: " << a3 << endl;
	int y = a1+a2+a3;
	cout << "Total of angles: " << y << endl;

	s3 = rand();
	s1 = s3 * (sin(a1)/sin(a3));
	s2 = s3 * (sin(a2)/sin(a3));
	cout << "Side 1: " << s1 << endl;
	cout << "Side 2: " << s2 << endl;
	cout << "Side 3: " << s3 << endl;
	return 0;
}

#include <iostream>
#include <boost/lexical_cast.hpp>

void printRow(int n, int i)
{
	if(n == 0)
		return;

	int n2 = n*n;
	int m2 = (n-1)*(n-1);
	if(n % 2 == 0)
	{
		if(i == 0)
			for(int k = n2-n+1; k > n2+1-2*n; --k)
				std::cout << k << "\t";
		else
		{
			std::cout << n2-n+1+i << "\t";
			printRow(n-1, i-1);
		}
	}
	else
	{
		if(i == n-1)
		{
			for(int k = n2-2*(n-1);k <= n2+1-n; ++k)
				std::cout << k << "\t";
		}
		else
		{
			printRow(n-1,i);
			std::cout << n2-i << "\t";
		}
	}
}

int main(int argc, char** argv)
{
	int n = boost::lexical_cast<int>(argv[1]);

	for(int i = 0; i < n; ++i)
	{
		printRow(n, i);
		std::cout << "\n";
	}

}

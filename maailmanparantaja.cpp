#include <iostream>
#include <fstream>
#include <string>
#include <boost/lexical_cast.hpp>

int main(int argc, char** argv)
{
	std::ifstream infile(argv[1]);

	std::string number, temp;
	while(getline(infile, temp))
		number += temp;

	while(number.length() > 2)
	{
		int last = boost::lexical_cast<int>(number.c_str()[number.length()-1]);
		number.resize(number.length()-1);
		int y = boost::lexical_cast<int>(&number.c_str()[number.length()-2]);

		last *= 2;
		
		int div = y - last;
		int c = (100 + div) % 100;
		number.resize(number.length()-2);

		if(div < 0)
		{
			for(auto i = number.rbegin(); i != number.rend(); ++i)
			{
				if(*i == '0' && i != number.rend()-1)
					*i = '9';
				else
				{
					*i = *i-1;
					break;
				}
			}
		}
		char t[3];
		sprintf(t, "%02d", c);
		number += t;
	}

	int y = boost::lexical_cast<int>(number);
	if( y % 7 == 0)
		std::cout << "JEE!\n";
	else
		std::cout << "VOI EI!\n";

	return 0;


}

#include <iostream>
#include <vector>
#include <boost/lexical_cast.hpp>
#include <fstream>

int main(int argc, char** argv)
{
	std::ifstream infile(argv[1]);
	std::string strsize, n;
	getline(infile, strsize);
	int size = boost::lexical_cast<int>(strsize);
	std::vector<std::vector<int> > v;
	v.push_back(std::vector<int>());
	while(getline(infile, n))
	{
		v.back().push_back(boost::lexical_cast<int>(n));
	}
	while(true)
	{
		v.push_back(std::vector<int>());
		for(int i=0; i<v[v.size()-2].size(); i+=2)
		{
			v.back().push_back(v[v.size()-2][i]+v[v.size()-2][i+1]);
		}
		std::cout << v.back().size() << std::endl;
		if(v.back().size()==1) break;
	}
	for(auto it=v.rbegin(); it!=v.rend(); ++it)
	{
		for(auto i=it->begin(); i!=it->end(); ++i)
		{
			std::cout << *i << " ";
		}
		std::cout << std::endl;
	}
}

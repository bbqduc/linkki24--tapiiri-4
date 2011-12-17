#include <iostream>
#include <sstream>
#include <bitset>

int bishopthreat(int x, int y, int side)
{
	return std::min(x,y)+std::min(x,side-y)+std::min(side-x, y)+std::min(side-x,side-y);
}

int horsethreat(int x, int y, int side)
{
	std::bitset<8> b;
	if(x<2)
	{
		b.set(0);
		b.set(4);
		if(x<1)
		{
			b.set(1);
			b.set(5);
		}
	}
	else if(x>side-3)
	{
		b.set(3);
		b.set(7);
		if(x>side-2)
		{
			b.set(2);
			b.set(6);
		}
	}
	if(y<2)
	{
		b.set(1);
		b.set(2);
		if(y<1)
		{
			b.set(0);
			b.set(3);
		}
	}
	else if(y>side-3)
	{
		b.set(5);
		b.set(6);
		if(y>side-2)
		{
			b.set(4);
			b.set(7);
		}
	}
	return b.count();
}

int main(int argc, char** argv)
{
	int side;
	std::stringstream ss;
	ss << argv[1];
	ss >> side;

	unsigned int threats=0;
	for(int i=0; i<side; ++i)
	{
		for(int j=0; j<side; ++j)
		{
			threats+=bishopthreat(i,j,side-1);
			threats+=8-horsethreat(i,j,side);
		}
	}
	
	std::cout << threats << std::endl;
}

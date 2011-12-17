import sys

f=open(sys.argv[1])
l=f.readlines()
f.close()

plants=[]
num = int(l[0])
for line in l[1:]:
	if len(line):
		s=line.split(" ")
		y=int(s[1])
		plants.append(y)
plants.sort()
median=plants[len(plants)/2]

summ=0
for p in plants:
	summ+=abs(median-p)
print summ

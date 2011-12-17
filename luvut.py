# -*- coding: UTF-8 -*-
import sys, re

numbers=[
("yksi" , "1"),
("kaksi", "2"),
("kolme", "3"),
("neljä", "4"),
("viisi", "5"),
("kuusi", "6"),
("seitsemän", "7"),
("kahdeksan", "8"),
("yhdeksän", "9"),
("kymmenen", "0"),
("kymmentä", "K"),
("toista", "O"),
("sataa", "S"),
("sata" , "s"),
("tuhatta", "T"),
("tuhat", "t"),
("miljoona","n")
]

f=open(sys.argv[1])
lines=f.readlines()
f.close()

def value(s):
	ret=0
	if "T" in s:
		sp=s.split("T")
		return int(1000*value(sp[0])+value(sp[1]))
	elif "S" in s:
		sp=s.split("S")
		if "t" in sp[0]:
			return 1000+100*value(sp[0][1:])+value(sp[1])
		return int(100*value(sp[0])+value(sp[1]))
	elif "K" in s:
		sp=s.split("K")
		r=int(10*value(sp[0][-1])+value(sp[1]))
		if "t" in sp[0]:
			r+=1000
		if "s" in sp[0]:
			r+=100
		return r
	if "t" in s:
		ret=1000
		s=s.replace("t","")
	if "s" in s:
		ret+=100
		s=s.replace("s","")
	if "O" in s:
		ret+=10
		s=s.replace("O","")
	if len(s): return ret+int(s[0])
	else: return ret 

summ=0
for l in lines:
	l=l.replace("\n","")
	for key in numbers:
		l=re.sub(key[0], key[1], l)
	summ+=value(l)
print summ

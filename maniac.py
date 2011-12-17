import sys, random

def f(pot, enemycard):
	a = random.randint(5, 14) + pot
	if a < enemycard -1:
		return 0
	if a > enemycard +1:
		return 2
	else:
		return 1

enemycard=0
pot=1
raised=0
first=True
random.seed(None)
while 1:
	try:
		line=sys.stdin.readline()
	except KeyboardInterrupt:
		break
	if first:
		enemycard=int(line)
		first=False
	else:
		if len(line):
			pot=int(line.split(" ")[0])
			raised=int(line.split(" ")[1].replace("\n",""))
			c = f(pot,enemycard)
			if raised == 0:
				c = max(c,1)
			print c

import sys

f=open(sys.argv[1])
l=f.readlines()
f.close()

names=[]
times=[]
herp=["SU", "RU", "PU", "VU"]

for s in l[1:]:
	sp=s.split("\t")
	for x in sp:
		if x.replace("\n","")=="-": sp[sp.index(x)]=999999
	names.append(sp[0])
	times.append([int(sp[1]), int(sp[2]), int(sp[3]), int(sp[4])])

bestindexes=[[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
besttimes=[[99999,99999,99999,99999,99999],[99999,99999,99999,99999,99999],[99999,99999,99999,99999,99999],[99999,99999,99999,99999,99999]]
for t in range(0, len(times)):
	for x in range(0, len(times[t])):
		besttimes[x][4]=times[t][x]
		bestindexes[x][4]=t
		for y in range (3,-1,-1):
			if besttimes[x][y]>besttimes[x][y+1]:
				besttimes[x][y], besttimes[x][y+1] = besttimes[x][y+1], besttimes[x][y]
				bestindexes[x][y], bestindexes[x][y+1] = bestindexes[x][y+1], bestindexes[x][y]
			else: break
besttime=99999
bestguys=[]
currenttime=0
for i in range(0,4):
	usedguys=[]
	currenttime=besttimes[0][i]
	usedguys.append(bestindexes[0][i])
	for j in range(0,4):
		if bestindexes[1][j] in usedguys:
			continue
		currenttime+=besttimes[1][j]
		usedguys=usedguys[:1]
		usedguys.append(bestindexes[1][j])
		for k in range(0,4):
			if bestindexes[2][k] in usedguys:
				continue
			currenttime+=besttimes[2][k]
			usedguys=usedguys[:2]
			usedguys.append(bestindexes[2][k])
			for l in range(0,4):
				if bestindexes[3][l] in usedguys:
					continue
				currenttime+=besttimes[3][l]
				usedguys=usedguys[:3]
				usedguys.append(bestindexes[3][l])
				if currenttime<besttime:
					besttime=currenttime
					bestguys=usedguys
				currenttime-=besttimes[3][l]
			currenttime-=besttimes[2][k]
		currenttime-=besttimes[1][j]
for x in range(0, len(herp)):
	print herp[x] + ": " + names[bestguys[x]]

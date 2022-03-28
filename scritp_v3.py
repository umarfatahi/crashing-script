import itertools

for a,b,c in itertools.product(itertools.count(0),range(0,10),range(0,10)):
	print(a,b,c)
	if a > 20: break

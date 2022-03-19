import math

C = 50
H = 30
D = [x for x in input().split(",")]

ans = []

for d in D:
	ans.append(str(int(round(math.sqrt(2*C*float(d)/H)))))

print(','.join(ans))
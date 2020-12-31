# p.72 frog問題を再帰で全探索する

def func(n,h):
	# n=0のときはコスト0
	if n==0: return 0

	cost = 10**10

	cost = min(cost, func(n-1,h)+abs(h[n]-h[n-1]))

	if n>1:
		cost = min(cost, func(n-2,h)+abs(h[n]-h[n-2]))

	return cost

N = 7
H = [2, 9, 4, 5, 1, 6, 10]
print(func(N-1,H))
# p.73 frog問題をメモ化再帰でとく
# 再帰回数の上限を設定：これをやらんとバグって舞う
import sys
sys.setrecursionlimit(10 ** 6)
N=int(input())
h=list(map(int, input().split()))
INF = 10**10
memo=[INF]*N
def func(n):
	# memoに何か値あればやめる
	if memo[n] < INF:
		return memo[n]
	if n == 0:
		return 0

	memo[n] = min(memo[n], func(n-1)+abs(h[n]-h[n-1]))
	if n > 1:
		memo[n] = min(memo[n], func(n-2)+abs(h[n]-h[n-2]))
	return memo[n]
print(func(N-1))

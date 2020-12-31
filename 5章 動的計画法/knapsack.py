# p.78 ナップサック問題 ABC32 D
# https://atcoder.jp/contests/abc032/tasks/abc032_d


N, W = map(int, input().split())
v, w = [], []
for _ in range(N):
	tmpv, tmpw = map(int, input().split())
	v.append(tmpv)
	w.append(tmpw)

# dp[i][w]は、i番目までの荷物をおもさwまでを許して入れたときの価値の最大値
dp = [[0]*(W+1) for i in range(N+1)]
# 配列の数とか添え字のところに注意したい
for i in range(1,N+1):
	for j in range(1,W+1):
		if j >= w[i-1]:
			# i番目の荷物を選ぶ
			dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]]+v[i-1])
		# i番目に荷物を選ばない
		dp[i][j] = max(dp[i][j], dp[i-1][j])

print(dp[N][W])
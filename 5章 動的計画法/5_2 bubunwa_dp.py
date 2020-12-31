# p.89 問題5.2
# 部分和問題を動的計画で

A = list(map(int, input().split()))
W = int(input())
N =len(A)
# dp[i][j] i番目までの要素でおもさjにできるかどうか
dp = [[False]*(W+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1,N+1):
	for j in range(W+1):
		if j >= A[i-1]:
			# i番目を選ぶ
			dp[i][j] = dp[i][j] or dp[i-1][j-A[i-1]]
		# i番目を選ばん
		dp[i][j] = dp[i][j] or dp[i-1][j]
print(dp[N][W])
# ABC185 編集距離 (動的計画法)
# https://atcoder.jp/contests/abc185/tasks/abc185_e

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[i][j] i番目までのAとj番目までのBを見た時の最小得点
dp = [[10**10]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
	dp[i][0] = i
for j in range(1, M+1):
	dp[0][j] = j

for i in range(1,N+1):
	for j in range(1,M+1):
		# 文字列同じやったら
		if A[i-1]==B[j-1]:
			dp[i][j] = min(dp[i][j], dp[i-1][j-1])
		else:
			# 文字列違う場合
			dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
		# A[i]を捨てる場合
		dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
		# B[j]を捨てる場合
		dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
print(dp[N][M])




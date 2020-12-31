# p.89 問題5.3
# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

N = int(input())
P = list(map(int, input().split()))
M = sum(P)
# dp[i][j] i番目までの問題でj点をれるかどうか
dp = [[False]*(1+M) for _ in range(N+1)]
dp[0][0]=True
for i in range(1,N+1):
	for j in range(M+1):
		if j>=P[i-1]:
			# i番目を選ぶ
			dp[i][j] = dp[i][j] or dp[i-1][j-P[i-1]]
		# i番目を選ばない
		dp[i][j] = dp[i][j] or dp[i-1][j]

# N番目までのやつで得点0~Mをつくれるかどうかを数えていく
ans = sum([1 if dp[N][j] else 0 for j in range(M+1)])
print(ans)
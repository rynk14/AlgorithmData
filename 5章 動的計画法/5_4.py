# p.89 問題5.4

a = list(map(int, input().split()))
W = int(input())
K = int(input())
N =len(a)
# dp[i][j]:i番目まででjを表すのに必要な数字の最小数
dp = [[10*5]*(W+1) for _ in range(N+1)]
dp[0][0]=0
for i in range(1, N+1):
	for j in range(W+1):
		# i番目を選ぶ
		if j>=a[i-1]:
			dp[i][j] = min(dp[i][j], dp[i-1][j-a[i-1]]+1)

		# i番目を選ばない
		dp[i][j] = min(dp[i][j], dp[i-1][j])

for i in range(N+1):
	if dp[i][W] <= K:
		print("Yes")
		exit()

print("No")

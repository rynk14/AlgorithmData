# p.88 問題5.1 
# https://atcoder.jp/contests/dp/tasks/dp_c

N = int(input())
A, B, C = [], [], []
for _ in range(N):
	a, b, c = map(int, input().split())
	A.append(a), B.append(b), C.append(c)

# dp[i][j] i日目に行動jをして得られる、i日目までの最大幸福度
# j=0,1,2 をa,b,cと見立てる
dp = [[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
	# i日目にj=0 (A) を選ぶ場合
	dp[i][0] = max(dp[i-1][1]+A[i-1], dp[i-1][2]+A[i-1])
	# i日目にj=1 (B) を選ぶ場合
	dp[i][1] = max(dp[i-1][0]+B[i-1], dp[i-1][2]+B[i-1])
	# i日目にj=2 (C) を選ぶ場合
	dp[i][2] = max(dp[i-1][0]+C[i-1], dp[i-1][1]+C[i-1])

ans = max([dp[N][j] for j in range(3)])
print(ans)


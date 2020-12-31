# p.61 flog問題 (動的計画)
# https://atcoder.jp/contests/dp/tasks/dp_a

N = int(input())
H = list(map(int, input().split()))

dp = [0]*N
dp[1] = abs(H[1]-H[0])
for i in range(2,N):
	dp[i] = min((dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2])))
print(dp[-1])

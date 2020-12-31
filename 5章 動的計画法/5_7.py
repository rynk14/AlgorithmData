# p.89 問題5.7 
# https://atcoder.jp/contests/dp/tasks/dp_f

s = input()
t = input()
S, T = len(s), len(t)

def max_str(x, y):
	if len(x)<len(y):
		return y
	else:
		return x

# dp[i][j] sのi番目までとtのj番目までで作れる一致してる最長の文字列
dp = [[""]*(T+1) for _ in range(S+1)]

for i in range(1, S+1):
	for j in range(1,T+1):
			# i, j番目を採用
			if s[i-1]==t[j-1]:
			    dp[i][j] = max_str(dp[i][j], dp[i-1][j-1]+s[i-1])
			else:
				dp[i][j] = max_str(dp[i-1][j], dp[i][j-1])
print(dp[S][T])
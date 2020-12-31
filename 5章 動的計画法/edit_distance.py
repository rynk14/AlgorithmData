# p.82 編集距離
"""
文字列S, Tが与えられ、
・変更：S中の文字を一つ選んで好きな文字に変更する
・削除：S中の文字を1つ選んで削除する
・挿入：Sの好きな箇所に好きな文字を1文字挿入する
の3つの操作ができるとき、SとTを同じ文字列にするには
最低何回の操作が必要になるか
"""
S, T = "logistic", "algorithm"
s, t = len(S), len(T)
# dp[i][j]:Sの最初のi文字分と、Tの最初のj文字分との間の編集距離
dp = [[10**10]*(t+1) for i in range(s+1)]
dp[0][0]=0
for i in range(s+1):
	for j in range(t+1):
		# 変更
		if i>0 and j>0:
			if S[i-1]==T[j-1]: # 一致してたらコストの追加はなし
				dp[i][j] = min(dp[i][j], dp[i-1][j-1])
			else: # 一致してなかったら変更してコスト＋１
				dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
		# 削除 i文字目を削除するので、i-1までのやつにコスト+1
		if i>0: dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
		# 挿入 挿入はTの文字を消すことと同値であるのでTのj文字目を削除する
		if j>0: dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
print(dp[s][t])
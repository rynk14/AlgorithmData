# p.107 問題6.1 座標圧縮

a = list(map(int, input().split()))
N = len(a)
# 重複なしで整列したやつをつくる
b = sorted(list(set(a)))

Ans = [-1]*N
# forでb[i]がaのどこにおるかをやってく
# ここで使うのが配列の二分探索
for i in range(N):
	left, right = 0, N-1
	while (1):
		mid = (left+right)//2
		if b[mid]==a[i]:
			order = mid
			break
		elif b[mid]<a[i]:
			left = mid + 1
		elif b[mid]>a[i]:
			right = mid - 1

		if left==right:
			if b[left]==a[i]:
				order = left
			break
	Ans[i] = order

print(*Ans)
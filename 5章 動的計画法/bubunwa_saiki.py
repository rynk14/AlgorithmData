"""
p.55部分和問題を再帰関数で全探索する
部分和問題
N個の数列が与えられ、そのうちのいくつかの和が
ある整数Wとなることはあるかどうか
"""
# n個の整数でwを表す
def bubunwa(n, w, a):
	# ベースケース
	if n==0:
		if w==0:
			return True
		else:
			return False

	# a[n-1]を選ばない場合 
	if bubunwa(n-1, w, a): return True
	# a[n-1]を選ぶ場合
	if bubunwa(n-1, w-a[n-1], a): return True

A = [2,4,8]
W = 13
if bubunwa(len(A), W, A):
	print("Yes")
else:
	print("No")

# 4章：再帰
"""
p.46ユークリッドの互除法
mをnで割ったあまりをrとすると
GCD(m, n)=GCD(n, r)
である
"""

def GCD(m, n):
	# ベースケース
	if n==0: # あまりが0ならば終わり
		return m
	# 再帰呼び出し
	return GCD(n, m%n)
print("ユークリッドの互除法")
print("GCD(51, 15)={}".format(GCD(51, 15)))

print("\n")

"""
p.47フィボナッチ数列再帰version
F_0=0
F_1=1
F_N=F_N-1+F_N-2 (N>=2)
"""

def fibo(n):
	# ベースケース
	if n==0:
		return 0
	elif n==1:
		return 1

	# 再帰呼び出し
	return fibo(n-1)+fibo(n-2)

print("フィボナッチ数列")
print("fibo(7)={}".format(fibo(7)))


"""
フィボナッチ数列を再帰でやるのは無駄が多いので
次のようにやる
"""
def fibo_kai(n):
	# 例外処理
	if n==0:
		return 0
	elif n==1:
		return 1

	f = [0, 1]
	for i in range(2,n+1):
		f.append(f[i-1]+f[i-2])

	return f[-1]

print("fibo_kai(7)={}".format(fibo_kai(7)))

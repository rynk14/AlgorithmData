# p.51 問題4.6 部分和問題を高速にする

A = list(map(int, input().split()))
W = int(input())
N = len(A)

"""
bubunwa[i,w,a]に対応する値を格納する
一回計算したやつを流用するため
ちなみにbubunwa[i,w,a]は、配列aのi番目までの要素の
任意の個数の和でwを表現できるかどうかのTrue or Falseである
"""
memo = [[-1]*(W+1) for i in range(N+1)]

def bubunwa_memo(i, w, a):
	# ベースケース
    if i==0:
    	if w==0:
    		return True
    	else:
    		return False

    # メモをチェックして既に計算済みなら答えを返す
    if memo[i][w]!=-1: return memo[i][w]

    # a[i-1] (aのi番目) を選ばん
    # i-1番目までの要素でwをつくれるかどうか
    if bubunwa_memo(i-1, w, a): memo[i][w]=1

    # a[i-1]を選ぶ
    if bubunwa_memo(i-1, w-a[i-1], a): memo[i][w]=1


if bubunwa_memo(N,W,A):
	print("Yes")
else:
	print("No")
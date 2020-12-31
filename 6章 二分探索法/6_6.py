# p.108 問題6.6
# https://atcoder.jp/contests/abc026/tasks/abc026_d

import math
import bisect as bs
A, B, C = map(int, input().split())

# f(t)=At+Bsin(Ctπ)=100を満たすtの範囲
t_lower = (100-B)//A
t_upper = (100+B)//A + 1
# [lower upper]の区間から探索をはじめてどんどん区間幅を小さくしていく

def f(x):
	return A*x + B*math.sin(C*x*math.pi)

# 100と等しいかどうかの判定函数
def judge(y):
	if abs(y-100) <= 10**(-6):
		return True
	else:
		return False

while (1):
	t_mid = (t_lower+t_upper)/2
	if judge(f(t_mid)):
		ans = t_mid
		break
	# Fの中に100入れるならの二分探索して探索区間を半分にしていく
	F = [f(t_lower), f(t_mid), f(t_upper)]
	index_of_t = bs.bisect_left(F, 100)
	if index_of_t==1: # 真ん中より小さかったら右端を今の真ん中に更新
		t_upper = t_mid
	elif index_of_t==2: # 真ん中よりでかかったら左端を今の真ん中に更新
		t_lower = t_mid

print(ans)


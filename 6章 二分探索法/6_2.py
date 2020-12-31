# p.107 問題6.2 
# https://atcoder.jp/contests/abc077/tasks/arc084_a

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(), B.sort(), C.sort()

# Aの各要素a_iに対して、a_iよりも大きくなる添え字を二分探索する
# a_iよりも大きいb_iに対して、それよりも大きいCの添え字を二分探索する
# p.97に書いてる考え方

import bisect as bs
import numpy as np

b_index = [bs.bisect(B, A[i]) for i in range(N)]
bigger_c = [N-bs.bisect(C, B[j]) for j in range(N)]
bigger_c = np.cumsum(list(reversed(bigger_c)))
ans = 0
for b in b_index:
	if 0<=b and b<N:
		ans += bigger_c[-b-1]

print(ans)
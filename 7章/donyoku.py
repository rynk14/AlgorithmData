# p.119 貪欲法
# https://atcoder.jp/contests/agc009/tasks/agc009_a

N = int(input())
A, B = [], []
for _ in range(N):
	a, b = map(int, input().split())
	A.append(a), B.append(b)

bottan = 0
for i in range(N-1, -1, -1):
	a = A[i] + bottan
	if a%B[i]!=0:
		bottan += B[i]-a%B[i]
print(bottan)
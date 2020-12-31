# p.121 問題7.1

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(), b.sort()
# a_i<b_jを満たすペア(a_i, b_j)を最大何ペア作れるか
ans = 0
now = 0
for i in range(N):
	while (1):
		if a[i]<b[now]:
			ans += 1
			now += 1
			break
		else:
			now += 1

		if now==N:
			print(ans)
			exit()
print(ans)
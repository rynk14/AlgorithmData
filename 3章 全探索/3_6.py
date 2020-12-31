# p.41 問題3.6 ABC51 B

K, N = map(int, input().split())

# 0<=X, Y, Z<=K かつ X+Y+Z=Nであるような(X,Y,Z)の場合の数を求める
ans = 0
for X in range(K+1):
  for Y in range(K+1):
    Z = N-X-Y
    if 0<=Z and Z<=K:
      ans += 1

print(ans)

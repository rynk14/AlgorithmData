# p.40 問題3.5 ABC81 B
def dividable_count(n):
    ans = 0
    while (n%2==0):
        n /= 2
        ans += 1
    return ans

N = int(input())
A = list(map(int, input().split()))
ans = 10000
# 全探索 各要素に対して2で割れる回数を求めていく
for a in A:
    ans = min(ans, dividable_count(a))
print(ans)

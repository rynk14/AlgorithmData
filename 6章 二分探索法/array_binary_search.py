# p.94 配列の二分探索

a = list(map(int, input().split()))
key = int(input())
N = len(a)
a.sort()
# 配列aの中から、keyがあるかどうかを判定し、あればその添え字も返す
ans = "No"
index = "-1"
left, right = 0, N-1
while (1):
	if key==a[(left+right)//2]:
		ans = "Yes"
		index = (left+right)//2
		break
	elif key>a[(left+right)//2]:
		left = (left+right)//2 + 1
		if left==right:
			if key==a[left]:
				ans = "Yes"
				index = left
			break

	elif key<a[(left+right)//2]:
		right = (left+right)//2 -1
		if right==left:
			if key==a[right]:
				ans = "Yes"
				index = right
			break
print(ans, index)
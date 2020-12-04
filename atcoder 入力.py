# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:45:22 2020

@author: rnona
"""
#入力が文字列の時
n = input()

# 整数 1 つ
N = int(input())

# 整数複数個
N, K = map(int, input().split())


# 整数 N 個 (改行区切り)
L = [int(input()) for i in range(N)]

# 整数 N 個 (スペース区切り)
A = list(map(int, input().split()))

# 整数 (縦 H 横 W の行列)
S = [list(map(int, input().split())) for i in range(3)]
# [[a,b], [c,d], [e,f]]みないなリスト
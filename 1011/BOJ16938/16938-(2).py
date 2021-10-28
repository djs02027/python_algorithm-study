# 백준이는 문제를 N개 가지고 있고,
# 모든 문제의 난이도를 정수로 수치화했다.

# i번째 문제의 난이도는 Ai이다.
# 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다.

# 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는
# X보다 크거나 같아야 한다.
import sys

sys.stdin = open('input.txt')

testNum, L, R, X = map(int, input().split())
test_level = list(map(int, input().split()))
test_level.sort()
cnt = 0

for i in range(1 << testNum): #16인데 15까지 돌으므로 (0~1111)
    cac=0
    maxv=-1
    minv=9876543210
    for j in range(testNum): #4
        if i & (1 << j):  #1, 10, 11 100 101 111 vs( 1 10 100 1000)
            cac+=test_level[j]
            if L > cac and cac > R:
                continue
            maxv=max(maxv,test_level[j])
            minv=min(minv,test_level[j])
    if L <= cac and cac <= R and maxv-minv >= X:
        cnt+=1
print(cnt)
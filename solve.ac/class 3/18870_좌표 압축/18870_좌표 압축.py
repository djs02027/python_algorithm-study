#https://jason9319.tistory.com/356 참고
#https://hongcoding.tistory.com/111
import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numset = set(numbers)
a = list(numset)
a.sort()
print(a)
numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i
print(numdict)
# 각각의 numbers의 키를 이용해서 각가의 압축값을 뽑아낸다.
for i in numbers:
    print(numdict[i], end=' ')
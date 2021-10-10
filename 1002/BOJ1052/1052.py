import sys
sys.stdin = open('input.txt')
'''

N개의 물병을 가지고 있고 각 물병에는 물을 무한대로 부을 수 있다.
처음에 모든 물병에는 물이 1리터씩 들어있다. 
한 번에 K개의 물병을 옮길 수 있다. 
이동을 한 번보다 많이 하기는 싫다. 
물병의 물을 적절히 재분배해서,
먼저 같은 양의 물이 들어있는 물병 두 개를 고른다.
그 다음에 한 개의 물병에 다른 한 쪽에 있는 물을 모두 붓는다. 
K개를 넘지 않는 비어있지 않은 물병을 만듦
상점에서 사는 물병은 물이 1리터 들어있다.

'''
'''
3 1
'''


# 시간초과 발생
def pouringwater(n):
    global cnt
    while n > 1:
        if n == 1 and cnt[0] == 0:
            return cnt
        n = n - 1
        for j in range(n):
            if pour[n] == 0 and arr[n] == arr[j]:
                tmp = arr[n]
                arr[n] = 0
                arr[j] = tmp + arr[j]
                pour[n] = 1
                if arr[n] == 0:
                    arr.pop(n)
                    pour.pop(n)
                break
        else:
            cnt += 1
            arr.append(1)
            pour.append(0)
    return -1


N, K = map(int, sys.stdin.readline().split())
arr = [1] * N
pour = [0] * N
cnt = 0
pouringwater(len(arr))
print(cnt)


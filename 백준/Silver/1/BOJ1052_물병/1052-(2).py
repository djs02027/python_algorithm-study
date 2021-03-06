import sys

sys.stdin = open('input.txt')

'''

이진수로 접근하는 방법이 있었다.

N이 1부터 8일 때 사오지않고 옮길 수 있는 병의 개수를 구해보면 N을 이진수로 변경했을 때 1의 개수가 된다는 것을 알 수 있다. 
만약 1의 개수가 K이하라면 옮길 수 있지만 초과한다면 옮길 수 없다.

그렇다면 1의 개수가 K개를 초과할 때는 어떻해야할까?

만약 N=6이고 K=1이라고 하자. 이를 이진수로 표현하면 110이 된다. 이때 1의 개수를 1개로 만들기위해서는 2^1의 자리에 1을 더한다. 
즉 6에 2를 더하는 것이다. 그렇다면 1000이되며 물병을 옮길 수 있게된다.
'''
'''
3 1
3을 2진수로 11이면 처음 1 이나오는 위치를 찾으면 0번이 되고 
2^0은 1이된다 이 결과값을 3(N)에 더한다.
3+1=4(N)이 된다. 다시 4를 2진수로 바꾸어서 1의 갯수가 K개 초과하는지 확인하며 초과하면 반복작업을 한다.
'''




N, K = map(int, input().split())

answer = 0
while bin(N).count('1') > K:
    plus = 2 ** (bin(N)[::-1].index('1'))
    answer += plus
    N += plus
print(answer)


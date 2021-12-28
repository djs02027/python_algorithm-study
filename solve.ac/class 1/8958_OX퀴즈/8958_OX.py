import sys
sys.stdin=open('input.txt')
T=int(input())


for tc in range(1,T+1):
    count = 0
    cac=0
    arr=list(map(str,input()))
    for s in arr:
        if s=='O':
            count+=1
        elif s == 'X':
            count=0
        cac+=count
    print(cac)
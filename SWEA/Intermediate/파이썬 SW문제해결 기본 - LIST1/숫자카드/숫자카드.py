import sys
sys.stdin=open('숫자카드.txt')
T=int(input())

for tc in range(1,T+1):
    N = int(input())
    arr=input()
    checked=[0]*10
    result=[]
    for a in arr:
        checked[int(a)]+=1
    max_value=-1
    max_key=-1
    for k,v in enumerate(checked):
        if max_value<=v :
            max_value=v
            max_key=k
    print("#{} {} {}".format(tc, max_key, max_value))




'''
왼쪽 줄 위로 앞 바퀴가 지나 간 시간 t
왼쪽 줄 위로 뒷 바퀴가 지나 간 시간 t + 500
오른쪽 줄 위로 앞 바퀴가 지나 간 시간 t + 1000
오른쪽 줄 위로 뒷 바퀴가 지나 간 시간 t + 1500

자동차가 오른쪽에서 올 때도 같은 규칙으로 오른쪽과 왼쪽을 바꾸어 측정하면 된다
'''

'''
    1000
|왼          |오

4 
17 517 1432 1932 =t --> 17 왼쪽 박스에서 측정
432 932 1017 1517 =t --> 432 오른쪽 박스에서 측정

6
235 451 735 951 2351 2851
1235 1351 1451 1735 1851 1951

'''
import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    leftline = list(map(int, input().split()))
    rightline = list(map(int, input().split()))
    cnt=0
    while leftline:
        temp = leftline.pop(0)
        flag = False
        if temp + 1500 in rightline:
            flag=True
        if flag:
            if temp+1000 in rightline:
                cnt+=1
    print(cnt)

#실패
import sys

sys.stdin = open('input.txt')
'''
1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다.
양수가 적혀 있을 경우에는 오른쪽으로, 
음수가 적혀 있을 때는 왼쪽으로 이동한다

'''
N = int(input())
balloon = list(map(int, input().split()))
idx = 0
result=[idx]
tmp = balloon[idx]
while balloon:
    # 인덱스로 풍선의 쪽지를 확인
    rear=len(balloon)

    tmpidx=idx
    # 음수인지 양수인지 확인
    if tmp < 0: #왼쪽(음수)
        # 인덱스값확인
        for i in range(abs(tmp)):
            if idx==0:
                idx = (rear + 1) % len(balloon)
                # break
            idx-=1
        result.append(idx)
        tmp = balloon[idx]
        balloon.pop(tmpidx)
        idx-=1


    elif tmp > 0: #오른쪽
        for i in range(tmp):
            if idx==len(balloon):
                idx = 0
                # break
            idx+=1
        result.append(idx)
        tmp=balloon[idx]
        balloon.pop(tmpidx)
        idx-=1


print(result)
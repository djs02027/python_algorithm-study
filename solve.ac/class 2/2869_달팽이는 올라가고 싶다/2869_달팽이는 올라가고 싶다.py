#  (a-b)*n +a = v
# a만큼 올랐다 b만큼 떨어지기를 반복하기 때문에
# a-b의 거리만큼 올라가는 것을 n만큼 반복하고
# 마지막 날에는 a만큼 올라가고서 더 이상 떨어지지 않기 때문이다.
import math
A,B,V=map(int,input().split())
# ceil 함수를 이용하면 소수를 올림 하는 정수를 반환하고
# 반대로 소수를 내림한 정수를 반환할 때는 floor를 이용한다
print(math.ceil((V-A)/(A-B)+1))
import math


def solution(w, h):



    # 직선이 지나는 점의 개수 -> 최대공약수
    # 최대공약수가 1일때 잘라지는 사각형의 개수는 w+h-1이 된다. (처음 겹피는 사각형 때문에 1를 뺀다.)
    # 전체 사각형의 개수에서 잘라지는 사각형의 개수를 빼면
    GCD = math.gcd(w, h)
    result = (w * h) - ((((w + h) // GCD) - 1) * GCD)

    answer = result

    return answer
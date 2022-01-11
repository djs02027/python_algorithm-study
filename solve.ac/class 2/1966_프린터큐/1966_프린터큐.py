from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = deque(list(map(lambda x: arr[x], range(len(arr)))))
    print(result)
    count = 0
    while result:

        maxv = max(list(result))
        front = result.popleft()
        print(result)
        M -= 1
        if maxv == front:
            count += 1
            if M < 0:
                print(count)
                break
        else:
            result.append(front)
            if M < 0:
                M = len(result) - 1


    # result=sorted(result, reverse=True)
    # print(result)
    # cnt=0
    # for i in range(len(result)):
    #     if i==M:
    #         print(cnt)
    #     cnt+=1

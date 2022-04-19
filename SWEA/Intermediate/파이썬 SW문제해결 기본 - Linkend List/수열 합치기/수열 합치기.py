T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    txt = []
    for _ in range(M):
        arr = list(map(int, input().split()))
        start = arr[0]

        if txt:
            cnt = 0
            for a in arr:
                txt.insert((start + cnt) - 1, a)
                cnt += 1
        else:
            for a in arr:
                txt.append(a)
    print(txt)

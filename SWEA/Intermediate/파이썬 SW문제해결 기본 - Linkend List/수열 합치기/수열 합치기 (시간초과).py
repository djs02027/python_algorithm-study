T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    txt = []
    for _ in range(M):
        arr = list(map(int, input().split()))
        start = arr[0]

        if txt:
            idx = len(txt)
            for t in range(len(txt)):
                if start < txt[t]:
                    idx = t
                    break
            cnt = 0
            for a in arr:
                txt.insert((idx + cnt), a)
                cnt += 1
        else:
            for a in arr:
                txt.append(a)
    print('#{} {}'.format(tc, ' '.join(map(str, txt[-10:][::-1]))))

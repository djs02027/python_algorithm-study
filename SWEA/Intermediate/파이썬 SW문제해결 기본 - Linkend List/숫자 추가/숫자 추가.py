T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    arr = list(map(int, input().split()))
    for _ in range(M):
        idx, V = map(int, input().split())

        arr.insert(idx,V)
    print('#{} {}'.format(tc,arr[L]))


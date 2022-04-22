# 합칠 수열의 첫글자를 뽑아서 기존 수열과 비교해서 들어갈 인덱스 찾기
# - 큰 숫자가 없으면 맨 뒤에 붙이기 (for문과 if문 활용)
# - 수열이 다 합쳐지면 으로 뒤에서부터 역순으로 10개 추출


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    txt = []
    for _ in range(M):
        arr = list(map(int, input().split()))
        start = arr[0]


        idx = len(txt)
        for t in range(len(txt)):
            if start < txt[t]:
                idx = t
                break
        #해당 칸에 삽입
        txt[idx:idx]=arr
        # txt.insert((idx + cnt), a)


    #배열을 [-10::]하면 뒤에서부터 10개를 잘라서 출력 해주고 [::-1] 한번 더해 주면 리버스..
    print('#{} {}'.format(tc, ' '.join(map(str, txt[-10:][::-1]))))

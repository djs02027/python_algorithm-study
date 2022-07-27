H, W = map(int, input().split())
block = list(map(int, input().split()))
result = 0
for i in range(1, W - 1):

    Left = max(block[:i+1]) # i를 두번 포함하게 해서 제일 큰값을 갖게 해줌
    Right = max(block[i:])
    minv = min(Left, Right)
    result+=abs(block[i]-minv)

print(result)
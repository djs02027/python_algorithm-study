N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
# MaxTrees = 2000000000
MaxTrees=max(trees)
mid=0
result=0
while start<=MaxTrees:
    mid = (start + MaxTrees) // 2
    cac = 0
    # 속도는 List comprehensive가 빠름
    cac=sum(t-mid if mid < t else 0 for t in trees)

    if cac >= M:
        start = mid + 1
        result=mid
    else:
        MaxTrees = mid - 1

print(result)
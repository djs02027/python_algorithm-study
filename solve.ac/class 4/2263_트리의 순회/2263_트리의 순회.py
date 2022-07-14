import sys
sys.setrecursionlimit(10**9)

def preOrder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return
    parents = postOrder[post_end]
    #preorder이므로 루트 -> 왼 -> 오 순으로 진행
    #루트
    print(parents, end=" ")

    left = index[parents] - in_start
    right = in_end - index[parents]
    # left, right로 나눠 분할 정복 방식으로 트리를 추적하여 전위 순회를 찾아낸다.
    # 왼쪽자식과 오른쪽자식의 갯수는 어떤 순회 방식이든 같으므로..
    # 왼쪽
    preOrder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    # 오른쪽
    preOrder(in_end - right + 1, in_end, post_end - right, post_end - 1)


N = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

index = [0] * (N + 1)
# 여기서 후위 순회의 끝 값은 항상 루트 노드 이기 때문에
# 중위 순회 값의 index들을 저장해주는 배열을 따로 만들어서
# 쉽게 중위 순회에서의 root 노드의 index 값을 찾아낼 수 있다.
for i in range(N):
    index[inOrder[i]] = i  # i의 순서를 거스르면 인덱스로 중위순회의 순서가 나옴

preOrder(0, N - 1, 0, N - 1)

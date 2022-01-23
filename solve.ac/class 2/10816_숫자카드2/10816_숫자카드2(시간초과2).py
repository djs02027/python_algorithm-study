
# 처음 올립니고, 한글 잘 못합니다. 사람들이 질문을 더 많이봐서 여기에 올렸어요.
#
# 1. 딕셔너리 쓰기.
#
# 딕셔너리를와 for 루프를 사용해서 숫자 카드에 적혀있는 정수를 key로 쓰고, 그 정수가 적힌 카드의수를 value로 쓸수있어요.
#
# 이분탐색보다 더 빨른속도가 나왔어요.
#
# 2. sys.stdin.readline()과 sys.stdout.write() 쓰기
#
# input()대신 sys.stdin.readline(), print()대신 sys.stdout.write()을 쓰면, 속도가 훨씬 빨라저요.
#
# sys.stdout.write()는, 새 라인을 생성 않합니다.
#
# 둘다 import sys 한다음 쓸수있고, jupyter나 colab애서 않돌아가지만 맞는답이에요.
#
# 태스트 하고싶으면 터미널에서는 돌아가요.
#
# 도움이 되었기를 바랍니다!

N=int(input())
cards=list(map(int,input().split()))
cards.sort()
M=int(input())
checklist={k:0 for k in map(int,input().split())}


print(checklist)
for i in cards:
    if i in checklist.keys():
        checklist[i]+=1

print(' '.join(map(str,checklist.values())))
T=int(input())
for tc in range(1,T+1):
    R,S = input().split()
    for s in range(len(S)):
        print(int(R)*S[s], end="")
    print()
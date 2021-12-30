import  sys
sys.stdin=open('input.txt')
T=int(input())
text=set()
for tc in range(1,T+1):
    text.add(input())
# print(text)
text=list(text)
arr=[[''] for _ in range(20000)]
for tx in text:
    arr[len(tx)].insert(0,tx)


for i in range(20000):
    arr[i]=sorted(arr[i])
    for j in range(len(arr[i])):
        if arr[i][j]:
            print(arr[i][j])
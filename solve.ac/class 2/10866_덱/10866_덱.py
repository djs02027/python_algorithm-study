import  sys
N=int(input())
dequeue = []
for _ in range(N):
    text=sys.stdin.readline().split()
    if text[0]=='push_back':
        dequeue.append(text[1])
    elif text[0]=='push_front':
        dequeue.insert(0,text[1])
    elif text[0]=='pop_front':
        if dequeue:
            tmp=dequeue.pop(0)
            print(tmp)
        else:
            print(-1)
    elif text[0]=='pop_back':
        if dequeue:
            tmp=dequeue.pop(-1)
            print(tmp)
        else:
            print(-1)
    elif text[0]=='size':
        print(len(dequeue))
    elif text[0]=='empty':
        if dequeue:
            print(0)
        else:
            print(1)
    elif text[0]=='front':
        if dequeue:
            print(dequeue[0])
        else:
            print(-1)
    elif text[0]=='back':
        if dequeue:
            print(dequeue[-1])
        else:
            print(-1)
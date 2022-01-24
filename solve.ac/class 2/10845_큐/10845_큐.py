import sys
N=int(input())
commands=[]
queue=[]
for _ in range(N):
        #  sys.stdin.readline은 줄바꿈(\n)까지 받아온다
        text=sys.stdin.readline().split()

        if text[0]=='push':
            queue.append(text[1])
        elif text[0] == 'pop':
            if queue:
                tmp = queue.pop(0)
                print(tmp)
            else:
                print(-1)
        elif text[0] == 'size':
            print(len(queue))
        elif text[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif text[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif text[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)





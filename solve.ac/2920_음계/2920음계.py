import sys
sys.stdin=open('input.txt')
information= { 1:'c', 2:'d', 3:'e', 4:'f', 5:'g', 6:'a', 7:'b', 8:'C'}
result=''
play=map(int,input().split())
for i in play:
    result+=information.get(i)

if result=='cdefgabC':
    print('ascending')
elif result=='Cbagfedc':
    print('descending')
else:
    print('mixed')
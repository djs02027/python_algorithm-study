#마이너스 기호를 만날 때 다음 마이너스 까지, 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한 번에 빼 주면 문제에서 원하는 답을 얻을 수 있다.

text=input()
cac=0
total=text.split('-')
for t in total[0].split('+'):
    cac+=int(t)
for t in total[1:]:
    for i in t.split('+'):
        cac-=int(i)
print(cac)


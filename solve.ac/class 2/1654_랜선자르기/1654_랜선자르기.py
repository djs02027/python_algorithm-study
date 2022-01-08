line_num, need_num = map(int, input().split())
lines = []
for ln in range(line_num):
    lines.append(int(input()))
start, end = 1, max(lines)  # 가장 짧은 길이 1을 start로, 랜선 중 가장 긴 길이를 end

while start <= end:
    middle = (start + end) // 2
    line_cnt = 0
    for i in lines:
        line_cnt += i // middle

    if line_cnt >= need_num:  # 필요한 갯수보다 많으니깐 길이를 더 크게 잘라야함
        start = middle + 1
    else:  # 필요한 갯수보다 적은경우  길이를 더 작게 잘라야함
        end = middle - 1

print(end)
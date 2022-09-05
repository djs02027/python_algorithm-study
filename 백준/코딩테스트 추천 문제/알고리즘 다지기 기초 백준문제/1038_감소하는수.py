from itertools import combinations

#
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 30, 31, 32, 40, 41, 42, 43, 50, ... ]

N=int(input())
nums = list()
for i in range(1, 11):      #  1~10개의 조합 만들기 (0~9개니깐)
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합을 감소하는 수로 변경
        nums.append(int("".join(map(str, comb))))

nums.sort()   # 오름차순
try:
    print(nums[N])
except:
    print(-1)
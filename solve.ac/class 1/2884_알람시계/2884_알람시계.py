
h,m= map(int,input().split())


if m >= 45:
    m = m - 45
elif m < 45:
    if h == 0:
        h = 24 - 1
    else:
        h = h - 1

    m = (60 + m) - 45;

print("{} {}".format(h,m))
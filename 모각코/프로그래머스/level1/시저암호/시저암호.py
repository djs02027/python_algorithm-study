def solution(s, n):
    # A 65 Z= 90 // a =97 z=122
    result = []
    for i in s:
        num = ord(i) + n
        if 65 <= ord(i) <= 90 and 65 <= num <= 90:
            result.append(chr(num))
        elif 97 <= ord(i) <= 122 and 97 <= num <= 122:
            result.append(chr(num))
        elif 65 <= ord(i) <= 90 and num > 90:
            result.append(chr(num - 26))
        elif 97 <= ord(i) <= 122 and num > 122:
            result.append(chr(num - 26))

        if i == ' ':
            result.append(' ')
    print(result)
    answer = ''.join(map(str, result))
    return answer
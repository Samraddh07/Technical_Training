def repeatString(s, n, addition):
    if len(s) >= n:
        return s
    
    res = s + addition
    return repeatString(res, n, addition)

s = input('Enter your string: ')
n = int(input('Enter an integer: '))

rs = (repeatString(s, n, s))[:n+1].count('a')
print(rs)
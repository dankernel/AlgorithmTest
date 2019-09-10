def f(s, n):

    i = 0
    string = s[i:i+n]
    cnt = 0
    ret = ''

    while i < len(s):
        if s[i:i+n] == string:
            cnt += 1
        else:
            if cnt == 1:
                ret += string
            else:
                ret += str(cnt) + string
            cnt = 1
            string = s[i:i+n]
        i += n

    if cnt == 1:
        ret += string
    else:
        ret += str(cnt) + string
    
    return ret

def solution(s):
    m = len(s)
    
    for i in range(len(s)):
        ret = len(f(s, i + 1))
        
        if ret < 1:
            ret = len(s)

        m = min(m, ret)

    return m

ret = solution("aabbaccc")
print(ret)

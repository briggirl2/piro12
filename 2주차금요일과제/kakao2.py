def is_valid(s):
    cnt = 0
    ans = True
    for i in s:
        if i == '(':
            cnt += 1
        elif cnt == 0:
            ans = False
            break
        else:
            cnt -= 1
    if cnt > 0:
        ans = False
    return ans


def find_u(s):
    ln = rn = temp = 0
    for index, i in enumerate(s):
        if i == '(':
            ln += 1
        else:
            rn += 1
        if ln == rn:
            return index
    return temp


def solution(s):
    ans = ''
    if not s:
        return ans
    if is_valid(s):
        return s

    end_of_u = find_u(s) + 1
    u = s[:end_of_u]
    v = s[end_of_u:]

    v = solution(v)
    if is_valid(u):
        ans = u + v
    else:
        ans = '(' + v + ')'
        for i in u[1:-1]:
            if i == '(':
                ans += ')'
            else:
                ans += '('
    return ans





print('start')
print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))
print('end')
Tc = int(input())
for tc in range(Tc):
    s = input()
    cnt = 0
    ans = 'YES'
    for i in s:
        if i == '(':
            cnt += 1
        elif cnt == 0:
            ans = 'NO'
            break
        else:
            cnt -= 1
    if cnt > 0:
        ans = 'NO'
    print(ans)
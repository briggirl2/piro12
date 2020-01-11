s = input()
ans = len(s)

for i in range(1, len(s)//2+1):
    prev = s[: i]
    zipLen = 0
    temp = 1
    for j in range(2*i, len(s)+1, i):
        now = s[j-i: j]
        if prev == now:
            temp += 1
        else:
            zipLen += i
            if temp != 1:
                zipLen += len(str(temp))
            prev = now
            temp = 1
        if zipLen >= ans:
            break

    zipLen += i
    if temp != 1:
        zipLen += len(str(temp))
    zipLen += len(s) - j
    ans = min(zipLen, ans)

print(ans)

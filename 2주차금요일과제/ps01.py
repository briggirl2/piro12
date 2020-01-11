n = int(input())
ans = 0
for m in range(1, n):
    tempSum = sum(map(int, str(m))) + m
    if tempSum == n:
        ans = m
        break
print(ans)
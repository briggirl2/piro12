n = int(input())
ans = 0
for m in range(1, n):
    tempSum = sum(map(int, str(m))) + m
    if tempSum == n:
        ans = m
        break
print(ans)

#
# 분해합 = 생성자 + 생성자의 자릿수의 합
# 따라서 생성자가 가장 작기 위해서는 자릿수의 합이 가장 커야한다.
# 자릿수의 합은 자릿수 * 9 일 때가 가장 크다
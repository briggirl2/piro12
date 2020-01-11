n = int(input())
cnt = {1: 0}
for i in range(2, n + 1):
    cnt[i] = cnt.get(i-1, 0)
    if i % 3 == 0:
        cnt[i] = min(cnt.get(i//3, 0), cnt[i])
    if i % 2 == 0:
        cnt[i] = min(cnt.get(i//2, 0), cnt[i])
    cnt[i] = cnt[i] + 1
print(cnt[n])
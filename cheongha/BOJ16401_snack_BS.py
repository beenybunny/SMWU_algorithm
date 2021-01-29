m,n = map(int, input().split())
snack = list(map(int, input().split()))

left = 1
right = 1000000000
ans = 0

def check(mid):
    cnt = 0
    for i in range(0, n):
        cnt += snack[i] // mid
    if cnt >=m:
        return True
    return False

while(left <= right):
    mid = (left + right) // 2
    if (check(mid)):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)

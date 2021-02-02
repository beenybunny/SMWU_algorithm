import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
s = 0

for i in reversed(range(len(l))):
    left = 0; right = len(l)-1;
    find = l[i]
    while(True):
        if right == i:
            right = right - 1
        if left == i:
            left = left + 1
        if left >= right: break
        s = l[left] + l[right]
        if s > find:
            right = right -1
        if s < find:
            left = left + 1
        if s == find:
            arr.append(find)
            ans = ans + 1
            break
print(ans)

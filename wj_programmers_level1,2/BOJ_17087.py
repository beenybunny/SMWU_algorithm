def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n, s = map(int, input().split())
pos = map(int, input().split()) # 동생들의 위치
s_pos = [ abs(p-s) for p in pos] # 동생들과 수빈이의 위치 차이 리스트
ans = 1000000000
if len(s_pos) == 1: # 동생이 한명일 경우
    print(s_pos[0]) # 차이를 그대로 출력
else:
    for i in range(0, len(s_pos)-1): # 위치 차이들 간의 최대공약수
        g = gcd(s_pos[i], s_pos[i+1])
        if ans > g:
            ans = g
    print(ans)

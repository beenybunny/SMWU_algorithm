import sys
#dfs - stack사용 (파이썬에서는 그냥 list로 구현, pop,append)

visited = [1]
virus = []

def sol():
    com = 1 #시작 노드
    dfs(com)

def dfs(com): #해당 분기
    #global visited 해줘야하나?
    for i in virus[com]:
        if i not in visited:
            visited.append(i)
            dfs(i)

if __name__ == "__main__":
    n= int(input())
    m = int(input())

    virus = [[] for i in range(n + 1)]
    '''
    virus=[]
    for i in range(m):
        x,y = map(int,sys.stdin.readline().split())
        virus.append((x,y))
    print(sorted(virus))
    '''

    for j in range(m):
        x, y = map(int, sys.stdin.readline().split())
        virus[x].append(y) #인접행렬? 경우에는 sort하면 안되겠지ㅡㅡ
        virus[y].append(x) #안해주면 아래 케이스 같은 경우 에러남.
        '''
        10
        7
        1 2
        2 3
        3 4 
        5 6
        7 8
        8 9
        9 1
        '''
    #sol(sorted(virus))
    sol()
    print(len(visited)-1)
#값 가장 적게 갈 수 있는 길로! 다익스트라
#상하좌우로만 갈 수 있어서 bfs랑 비슷하게 하되, 가중치를 고려해야함
#전형적인 다익스트라,, 한 지점을 기준으로 특정 지점까지 최단경로를 구하고
#가중치가 주어질 때 다익스트라를 활용.
import queue
import math

def solution(cave,N,cnt):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = 0, 0
    q = queue.PriorityQueue()
    dist = [[math.inf]*N for _ in range(N)]

    dist[x][y] = 0 #첫 정점
    q.put((cave[0][0],x,y)) #첫 정점

    while q:
        w,x,y = q.get()
        if x== N-1 and y==N-1:
            print("Problem {0}: {1}".format(cnt,w))
            return
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            #if N>nx>=0 and N>ny>=0: #이게되나,,,?
            if 0 <= nx < N and 0<= ny < N:
                nw = w + cave[nx][ny]
                if nw < dist[nx][ny]:
                    dist[nx][ny] = nw
                    q.put((nw,nx,ny))

def get_inputs(N):
    cave = [[] for i in range(N)]

    for i in range(N):
        cave[i].extend(input().split())
        cave[i] = list(map(int,cave[i]))

    return cave

if __name__== "__main__":
    cnt = 1
    N = int(input())  # 동굴의 크기
    while N != 0 :
        cave = get_inputs(N)
        solution(cave,N,cnt)
        N = int(input())
        cnt+=1
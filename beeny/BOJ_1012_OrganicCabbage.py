import queue
visited = []
cabbage_field = []
def plant(M,N,K):
    global cabbage_field
    cabbage_field = [[0 for i in range(N)] for j in range(M)]
    for i in range(K):
        X, Y = input().split()
        X, Y = int(X), int(Y)
        cabbage_field[X][Y] = 1
    return cabbage_field

def bfs(m,n,M,N):
    que = queue.Queue()  # ()써줘야하는 거 주의 !
    global visited
    check_m = [1, -1, 0, 0]
    check_n = [0, 0, 1, -1]
    visited[m][n] = 1
    que.put((m,n))

    while not(que.empty()):
        mm,nn = que.get()
        for i in range(len(check_m)):
            new_m = mm + check_m[i]
            new_n = nn + check_n[i]

            if new_m >= M or new_m < 0 or new_n >= N or new_n < 0 :
                continue
            if visited[new_m][new_n] == 1 or cabbage_field[new_m][new_n] == 0:
                continue
            que.put((new_m,new_n))
            visited[new_m][new_n] =1
def solution(M,N,K):
    global cabbage_field
    global visited
    worm = 0

    cabbage_field = plant(M,N,K) #return을안하면,,NoneType이 되네

    visited = [[0 for i in range(N)] for j in range(M)]

    for m in range(len(cabbage_field)):
        for n in range(len(cabbage_field[m])):
            if visited[m][n] == 0 and cabbage_field[m][n] == 1:
                bfs(m,n,M,N)
                worm+=1

    return worm


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        M,N,K = input().split()
        worm = solution(int(M),int(N),int(K))
        print(worm)
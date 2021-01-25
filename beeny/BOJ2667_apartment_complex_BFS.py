#https://www.acmicpc.net/problem/2667
import sys
import queue

def find_start(start_i):
    global visited
    global q
    global comp
    
    for i in range(start_i, length):
        for j in range(length):
            if apartment[i][j] == 1 and visited[i][j] == 0 : 
                q.put((i,j))
                visited[i][j] = 1
                comp+=1
                apart[comp-1]+=1
                start_i =i
                return start_i
            
                '''
                break 
        if q.qsize() != 0 :
            break
        '''
    
size = int(sys.stdin.readline().strip())
visited = [[0 for i in range(size)] for j in range(size)]
q = queue.Queue()
apartment = []
comp = 0
apart=[0 for i in range(size**2)] #SIZE를 어떻게 설정하지,,
start_i = 0 #새로 시작하는 단지 찾을 행 

for i in range(size):
    apartment.append(list(map(int,sys.stdin.readline().strip())))

length = len(apartment)

start_i = find_start(start_i)
                
di = [1,-1,0,0]
dj = [0,0,1,-1]

while q.qsize() != 0: #OR while not q.empty()
    i,j = q.get()
    for x in range(4):
        ni = i+di[x]
        nj = j+dj[x]
        if ni < 0 or ni>=length or nj < 0 or nj >= length: continue
        elif apartment[ni][nj] == 1 and visited[ni][nj] != 1: #이어져 있고 방문한 적이 없다면
            q.put((ni,nj))
            visited[ni][nj] = 1 #i,j로 썻기때문에 무한루프1
            apart[comp-1]+=1
            
    if q.empty():
        start_i = find_start(start_i)
            
print(comp)
apart.sort()
for i in apart:
    if i != 0 : print(i) 

#한개의 동으로 된 단지도 단지로 쳐야함
#range고쳤는데 또 runtime에러 -> apart 크기 때문에 런타임 에러 난거였음!!!!!!!!1
    

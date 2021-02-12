import queue

dfs_checked_vertex = []
def dfs(N, V ,links_list):
    global dfs_checked_vertex
    dfs_checked_vertex.append(V)
    length = len(dfs_checked_vertex)

    if length >= N:
        return 0

    for link in links_list[V]:
        if link not in dfs_checked_vertex:
            dfs(N,link,links_list)

def bfs(N,V,links_list):
    bfs_checked_vertex = [V]
    bfs_queue = queue.Queue(maxsize = N)

    while True:
        for link in links_list[V]:
            if link not in bfs_checked_vertex:
                bfs_checked_vertex.append(link)
                bfs_queue.put(link)
        if bfs_queue.empty():
            return bfs_checked_vertex
        V = bfs_queue.get()

    return bfs_checked_vertex
if __name__ == "__main__":
    N,M,V = input().split(" ")
    N = int(N)
    links_list = [[]*N for i in range(N+1)]
    #pdb.set_trace()
    for i in range(int(M)):
        link = input().split(" ")
        links_list[int(link[0])].append(int(link[1]))
        links_list[int(link[1])].append(int(link[0]))

    for links in links_list:
        links.sort()
    dfs(int(N),int(V),links_list)
    bfs_checked = bfs(int(N),int(V),links_list)

    for i in dfs_checked_vertex:
        print(i,end=' ')
    print("")
    for i in bfs_checked:
        print(i,end=' ')

#https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10 ** 9) #6으로 해도 되네,,

def tree_dfs(i):
    for node in tree[i]:
        #if node not in found :
        if not found[node]:
            parents[node]=i
            #found.append(node)
            found[node] = True
            tree_dfs(node)

numOfNode = int(sys.stdin.readline().strip())
tree =[[]*i for i in range(numOfNode+1)]#인접리스트로
parents = [0 for i in range(numOfNode+1)]
#found = [root] #이미 루트 찾은 노드들? 스택역할
found = [False for _ in range(numOfNode+1)]
root = 1


for _ in range(numOfNode-1):
    a,b = map(int,sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)

found[root] = True
tree_dfs(root)

for i in range(2,numOfNode+1):
    print(parents[i])
    
'''발생한 runtime error: maximum recursion depth exceeded
-> 파이썬에는 시스템의 안정을 위해 재귀의 한도(10^4)가 정해져 있고 그 한도를 푸는 방법이
sys.setrecursionlimit(10000) -> 재귀 한도를 100000까지 풀어줌.

'''

'''
BOJ 9095
ex)4를 1,2,3의 합으로 나타내는 방법
1.1.1.1
1,1,2
1,2,1
2,1,1
2,2
1,3
3,1

'''
import sys
import pdb

def get_dp(i):
    global dp
    sum_= 0

    if i <= 3 and i >= 1: #for문안에 넣는 거 아닌거 주의! 
            return dp[i]
        
    for j in range(i-1,i-4,-1):
        #pdb.set_trace()
        if j >=1 and dp[j]==0 :
            #print("없음: ",j)
            dp[j]=get_dp(j)
        sum_+=dp[j]
    return (sum_) #재귀니까 return해주는 거 중요! 
    
amount = sys.stdin.readline().strip()
numbers = []
for i in range(int(amount)):
    number=sys.stdin.readline().strip()
    #numbers.append(map(int,number)) 이건 왜 안되지? 찾아보기
    numbers.append(int(number))

#print(numbers)
dp = [0 for i in range(12)] #n이 최대 11이라고 해서  
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in numbers:
    print(get_dp(i))

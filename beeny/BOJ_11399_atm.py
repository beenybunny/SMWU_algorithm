import sys
def solution(withdraw_time):
    sum =0
    waiting = 0
    for i in withdraw_time:
        sum += waiting+ i
        waiting += i
    print(sum)
    return
if __name__ == "__main__":
    n = int(input())
    withdraw_time= list(map(int,sys.stdin.readline().split()))
    solution(sorted(withdraw_time))
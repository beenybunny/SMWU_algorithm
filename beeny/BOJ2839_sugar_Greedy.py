import sys

n = int(input())
answer = 0
quo =0
rest = 0
common = 15 #3,5 최소공배수

quo = n//5
'''
if n%common == 0 :
    #무조건 답이 있는 경우
    answer+=quo
    answer+=quo//3
#-> 여기는 사실 필요없을 듯..
'''

if quo > 0 or n < 5: #n은 무조건 3이상의 값이 들어옴.
    #5로 나눴을 때 목이 있다 -> 5의 몫에서 하나씩 빼가면서 3에 담았을 때 담을 수 있는지
    #n이 5보다 작은 경우 (3일 때,,)
    rest = n%5
    answer+=quo

    if (rest % 3 ==0):
        answer+=rest//3

    else :
        while(answer > 0):
            answer-=1
            rest +=5
            if(rest % 3 == 0) :
                answer+=rest//3
                break

if answer == 0:
    answer = -1
print(answer)
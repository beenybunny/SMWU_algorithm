import sys

case = int(input())

for _ in range(case):
    answers = input()
    sum=0
    score = 0
    for ans in answers:
        if ans == "O" :
            score+=1
            sum += score
        elif ans == "X":
            score = 0
    print(sum)

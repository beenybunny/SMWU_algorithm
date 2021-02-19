#오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
days = ["","SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

day_idx = 2 #시작 월요일 인덱스

answer = 0

m,d = input().split()
m = int(m)
d = int(d)

answer = sum(month_days[:m-1])
answer+= d-1 #경과한 날짜
answer%=7

answer = (day_idx+answer)
if answer > 7 : answer = 1

print (days[answer])

# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까?
# 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
# 첫째 줄에 빈칸을 사이에 두고 x, y입력. SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력

m, d=map(int, input().split( ))
day=0

for i in range(2,m):
    
    if i in [4,6,9,11]: day+=30
    elif i in [2]: day+=28
    elif i in [3,5,7,8,10,12]: day+=31
    
if m!= 1: day+=31
    
day+=d

daylist=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

print(daylist[day%7-1])

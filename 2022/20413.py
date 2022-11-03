# MVP 다이아몬드  

N = int(input())
grade = [0] + list(map(int,input().split( )))
grade_order = ['B','S','G','P','D']
mvp = input()
acc, answer = 0,0
for m in mvp:
    idx = grade_order.index(m)
    answer += grade[idx+1]-1-acc if idx < 4 else grade[4]
    acc = grade[idx+1]-1-acc if idx < 4 else grade[4]
print(answer)

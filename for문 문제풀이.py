''' A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for문을 사용하여 A 학급의 평균 점수를 구해 보자. '''

a= [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
tot=0
for i in a:
    tot += i
average=tot/len(a)
print (average)

 #연습
 

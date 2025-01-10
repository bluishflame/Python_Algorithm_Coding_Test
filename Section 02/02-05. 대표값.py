# Section 02-04 대표값
'''
N명의 학생의 수학점수가 있다. 
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하시오. 

평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호가 답이고,
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생 번호가 빠른 학생의 번호를 답으로 한다. 

첫 번째 줄에는 자연수 N(5<=N<=100)이 주어진다.
두 번째 줄에는 각 학생의 수학 점수인 N개의 자연수가 주어진다. 
학생의 번호는 앞에서부터 1로 시작해서 N까지이다. 

첫 번째 줄에는 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 
평균은 소수 첫째 자리에서 반올림한다. 
'''

import sys
# sys.stdin = open("input.txt", "rt")

N = int(input())
MathList = list(map(int, input().split()))

Total = sum(MathList)
Avg = Total/len(MathList)
Round_Avg = round(Avg)

min_diff = float('inf')
max_score = -1
student_number = -1

for i, score in enumerate(MathList) :
    diff = abs(score-Round_Avg)
    
    if diff < min_diff or (diff==min_diff and score > max_score) or (diff==min_diff and score==max_score and i+1 < student_number) :
        min_diff = diff
        max_sxore = score
        student_number = i+1
        
print(Round_Avg, student_number)

'''
1) 평균 계산: round를 사용하여 소수 첫째 자리에서 반올림
2) 평균과 가까운 학생 찾기:
    min_diff는 평균과의 최소 차이를 저장
    max_score는 평균과 가까운 학생 중 가장 높은 점수를 저장
    student_number는 평균과 가까운 학생의 번호를 저장
3) 조건 비교 순서:
    차이가 더 작은 경우를 우선으로 체크
    차이가 같을 경우, 더 높은 점수를 우선
    점수도 같을 경우, 학생 번호가 더 빠른 순서로 선택
    
'''

# 모범 답안

'''
import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n) 
min = 2147000000

for idx, x in enumerate (a) : 
    tmp = abs(x-ave)
    if tmp < min : 
        min = temp 
        score = x 
        res = idx+1
    elif tmp == min : 
        if x > score :
            score = x
            res = idx+1
    
print(ave, res)
'''

'''
enumerate -> idx에는 인덱스 번호를, x는 인덱스에 해당하는 값을 반환한다, 즉 리스트의 인덱스 값과 실제 값을 쌍으로 대응해주는 것이 enumerate
abs -> 두 값의 절댓값 반환
'''
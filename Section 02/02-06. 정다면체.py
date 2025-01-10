# Section 02-06 정다면체
'''
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
가장 확률이 높은 숫자를 출력하는 프로그램을 작성하시오. 

정답이 여러 개일 경우 오름차순으로 출력한다. 

첫 번째 줄에는 자연수 N과 M이 주어진다. N과 M은 4, 6, 8, 12, 20 중 하나이다. 

첫 번째 줄에 답을 출력한다. 
'''

import sys
# sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

count = [0]*(N+M+2)

for i in range(1, N+1) :
    for j in range(1, M+1) :
        count[i+j] += 1

max_count = max(count)

for index in range(len(count)) :
    if count[index] == max_count :
        print(index, end= " ")

'''
1) 입력 받기: N, M = map(int, input().split())
2) 리스트 생성: count 리스트를 만들어서 합의 빈도를 저장 (0으로 초기화)
3) 이중 반복문: 모든 주사위를 던지는 경우를 계산 (for i in range...)
4) 최빈값 찾기: max()를 사용해서 최빈값 계산
5) 출력: print()를 사용해서 결과 출력

'''

# 모범 답안

'''
import sys 
sys.stdin = open("input.txt", "rt")

n, m - map(int, input().split())
cnt [0]*(n+m+3)
max = -2147000000

for i in range (1, n+1) : 
    for j in range(1, m+1) :
        cnt[i+j] += 1

for i in range(n+m+1) :
    if cnt[i] > max :
        max = cnt[i]

for i in range(n+m+1) :
    if cnt[i] == max :
        print(i, end=' ') 
        

'''
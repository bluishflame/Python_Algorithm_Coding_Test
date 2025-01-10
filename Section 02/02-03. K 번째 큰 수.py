# Section 02-03 K 번째 큰 수
'''
1부터 100 사이의 자연수가 적힌 N장의 카드가 있고, 숫자는 중복될 수 있다.
이 중 3장을 뽑아 각 카드에 적힌 수의 합을 기록하려고 한다.
3장을 뽑을 수 있는 모든 경우를 기록한다. 
기록한 값 중 K 번째로 큰 수를 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 자연수 N(3<=N<=100)과 K(1<=K<=50)이 입력되고 그 다음 줄에는 N개의 카드 값이 입력된다.
첫 번째 줄에는 K번째 수를 출력한다. 
'''

import sys
# sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
Card = list(map(int, input().split()))

Sum = set() 

for i in range(N) :
    for j in range(i+1, N) : 
        for m in range (j+1, N) : 
            Sum.add(Card[i] + Card[j] + Card[m])
         
Sorted_Sum = sorted(Sum, reverse=True)

print(Sorted_Sum[K-1])

'''
1) 세 개의 중첩 반복문 사용 : i, j, k의 인덱스가 겹치지 않도록 j는 i+1, k는 j+1부터 시작
2) 중복 제거 : set 자료구조를 사용하여 중복 제거
3) 정렬 : sorted를 사용하여 내림차순으로 정렬
4) K번째 수 출력 : K-1을 사용하여 1부터 시작하는 K를 인덱스로 변환
'''

# 모범 답안

'''
import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(n) :
    for j in range(i+1, n) : 
        for m in range(j+1, n) : 
            res.add(a[i]+a[j]+a[m]) 
    
res = list(res)
res.sort(revers=True)
print(res[k-1])        
            
'''
'''
중복을 제거하는 자료 구조  ->  set()
삼중 반복문에서 중복을 제거하기 위해서 +1 씩을 해주고 있음 
set의 경우 append가 아니라 add
'''
# Section 02-01 K 번째 약수
'''
어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 p는 q의 약수이다
두 개의 자연수 N과 K가 주어졌을 때 N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오

첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다 N은 1이상 10,000 이하이다 K는 1이상 N 이하이다
첫째 줄에 N의 약수들 중 K번째 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 -1을 출력한다
'''

import sys
# sys.stdin=open("input.txt","rt")

N, K = map(int, input().split())

list = []

for i in range(1, N+1):
    if N%i == 0 :
        list.append(i)
        
if len(list) >= K :
    print(list[K-1])
else:
    print(-1)

'''
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1) :
    if n%i == 0: 
        cnt+=1
    if cnt == k :
        print(i)
        break
else : 
    print(-1) 
'''

'''
약수 찾기: N의 약수를 찾으려면 1부터 N까지 반복문을 돌면서 N을 해당 숫자로 나누어 나머지가 0인지 확인합니다. 나머지가 0이라면 그 숫자는 N의 약수입니다.

약수 저장: N의 약수를 찾을 때, 약수를 순서대로 리스트에 저장합니다.

K번째 약수 출력:

약수 리스트의 크기가 K보다 크거나 같다면 K번째 요소를 출력합니다. (리스트 인덱스는 0부터 시작하므로 K-1번째 인덱스를 참조해야 합니다)
만약 K가 약수의 개수보다 크다면 -1을 출력합니다.
'''
# Section 02-02 K 번째 수
'''
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열 중에서 
s번째부터 e번째까지의 수를 오름차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하시오

첫 번째 줄에는 테스트 케이스 T (1<=T<=10)이 주어진다
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k 가 차례로 주어진다
두 번째 줄은 N개의 숫자가 차례로 주어진다 
'''

import sys
sys.stdin=open("input.txt", "rt")

T = int(input())

for t in range(1, T+1):
    N, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    ascendList = numbers[s-1:e]
    
    for i in range(k) :
        min_idx = i 
        for j in range(i+1, len(ascendList)):
            if ascendList[j] < ascendList[min_idx] :
                min_idx = j
        ascendList[i], ascendList[min_idx] = ascendList[min_idx], ascendList[i]
        
    print(f"#{t} {ascendList[k-1]}")
    
'''

- 선택 정렬 (Selection Sort)
    1) 배열에서 최소값을 반복적으로 찾아 정렬하는 방식
    2) K번째 수만 필요하기 때문에 완전히 정렬할 필요 없이, K번째 값까지만 정렬하면 됩다다

- 알고리즘 설명:
    1) 구간 추출: s부터 e까지의 숫자열을 추출
    2) 선택 정렬 수행:
        2-1) K번째까지 정렬만 수행
        2-2) 매번 남은 숫자 중 가장 작은 값을 찾아 앞으로 이동
    3) 결과 반환: K번째 수를 출력

'''

# 모범 답안
    
'''
T = int(input())
for t in range(T) : 
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t, a[k-1]))

'''

'''
T = int(input())  
for t in range(1, T + 1):
    N, s, e, k = map(int, input().split())  
    numbers = list(map(int, input().split()))
    
    sliced_numbers = sorted(numbers[s-1:e])  
    result = sliced_numbers[k-1]  
    
    print(f"#{t} {result}")
    
'''


'''
1) 입력 받기: 먼저 테스트 케이스의 개수 T를 입력받기기
2) 반복문 사용: 각 테스트 케이스에 대해 반복문을 사용하여 아래의 과정을 수행
    2-1) 데이터 추출:
        2-1-1) N, s, e, k를 입력받기
        2-1-2) N개의 숫자열을 입력받기기
    2-2) 구간 추출: 주어진 s부터 e까지의 숫자를 슬라이싱, 이때 Python은 0-based index이므로, s-1부터 e까지 슬라이싱해야 한다 
    2-3) 정렬: 해당 구간을 sorted() 함수를 이용해 오름차순 정렬
    2-4) K번째 수 찾기: 정렬된 리스트에서 k번째 값을 출력, 이때 Python에서는 k-1 인덱스를 사용해야 한다 
    2-5) 결과 출력: 각 케이스의 결과를 #1, #2 형태로 출력
    
'''
# Section 02 최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]       # 가장 작은 값을 찾는는 알고리즘 
arrMin = float('inf')                # arr 리스트 중 가장 작은 값이 기록되는 변수를 가장 큰 값으로 초기화

for i in range(len(arr)) :           # i는 0부터 7까지 8번을 반복
    if arr[i] < arrMin :             # 배열 안에 같은 값이 있을 경우에는 등호가 있는 경우도 고려해야 한다 
        arrMin = arr[i]
        
print(arrMin)
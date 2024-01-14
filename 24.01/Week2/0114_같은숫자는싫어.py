def solution(arr):
    answer = []
    temp = arr[:]
    for num in arr:
        if num != temp:
            answer.append(num)
        temp = num
    return answer
def solution(arr):
    answer = []
    temp = None
    for num in arr:
        if num != temp :
            answer.append(num)
        temp = num
    return answer

## 미친 gpt의 답변
def solution(arr):
    return [num for i, num in enumerate(arr) if i == 0 or num != arr[i-1]]
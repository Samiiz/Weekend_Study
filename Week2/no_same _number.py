def solution(arr):
    answer = []
    for num in arr:
        if not answer or num != answer[-1]:
            answer.append(num)
        
    return answer


def solution(arr):
    answer = []
    temp=arr[:]   # temp array is used to store the last element of the array  
    for num in arr: 
        if num != temp:
            answer.append(num)
            temp=num
        print(answer)
    return answer




def solution(arr):
    return  [arr[i] for i in range(len(arr)) if not(arr[i:i+1] == arr[i+1:i+2])]


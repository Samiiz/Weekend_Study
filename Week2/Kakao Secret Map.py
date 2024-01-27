def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        b=bin(arr1[i]| arr2[i])[2:].zfill(n)
        b =b.replace("0"," ").replace("1","#")
        answer.append(b)
    return answer


def solution(n, arr1, arr2):
    answer =[]
    for i in range(n):
        b=bin(arr1[i]|arr2[i])[2:].zfill(n)
        b=b.replace("0"," ").replace("1","#")
        answer.append(b)
    return answer

def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        z=bin(a | b)[2:].zfill(n)
        z=z.replace("0"," "),replace("1","#")
    answer.append(z)
    return answer        
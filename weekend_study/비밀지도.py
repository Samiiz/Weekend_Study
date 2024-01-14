def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        com = arr1[i] | arr2[i]
        binary_com = format(com,f'0{n}b')
        replaced_arr = binary_com.replace('1','#').replace('0',' ')
        answer.append(replaced_arr)
    return answer

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
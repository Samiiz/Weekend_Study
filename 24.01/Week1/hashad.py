# 첫 번째 과정으로 진행 순서 정립

# 하샤드수인지 확인하려면
# 1. 입력값(예들들어 12)의 자리수를 나눈다
# 2. 나눈 수들을 전부 더한다
# 3. 입력값 % 나눈수의 합 == 0 일때 answer = True 로 할당한다


# 결과

def solution1(x):
    answer = True # answer의 기본값을 True로 할당한다.
    
    X = str(x) # 입력값을 문자열 형태로 받기 위해 형변환 후 X라는 변수에 할당
    a = 0 # 나눈 수들의 합을 구하기 위해 a라는 변수에 0을 할당
    for i in range(len(X)):  # X의 길이("12"라면 2)만큼 for문의 반복 횟수를 정해준다.
        a += int(X[i]) # 문자열로 변경된 X의 i번째 인덱스값들을 정수로 변환한 후 a에 더한다.   -> 반복
    if x % a != 0: # 입력값 x를 a로 나눈 나머지가 0이 아닐시 라는 조건을 만든다.
        answer = False # answer에 False를 할당해서 입력값이 하샤드수가 아닐 시 False를 반환 하게 한다.
    
    return answer # 마지막으로 True or False가 할당된 answer을 반환한다

# 타인 정답을 확이 후 sum함수를 이용하여 재시도

def solution2(x):
    answer = True
    # sum 함수 이용시 코드를 더욱 간결하게 표현 가능하다.
    # sum함수는 반복가능한 객체의 모든 요소들을 더한 값을 반환한다.
    
    
    if x % sum(int(i) for i in str(x)) != 0:
        # int(i) for i in str(x)
        # 각 자릿수에 접근하기 위해 str(x)를 사용하고
        # str(x)의 문자열을 순회하면서 각 문자인 i를 정수로 변환한다.
        # sum 함수를 이용해 정수로 변환된 i 들을 더한다

        answer = False
        # x와 sum으로 더한 수들의 나머지가 0이 아닐시 answer = False로 할당한다

    return answer# 마지막으로 True or False가 할당된 answer을 반환한다

def solution3(x):

    answer = True
    # sum_num 변수를 사용하여 가독성을 좋게 만들 수 있다.
    sum_num = sum(int(i) for i in str(x))

    if x % sum_num != 0:
        answer = False
    
    return answer

스터디 재밌다
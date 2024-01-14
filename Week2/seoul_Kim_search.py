def solution(seoul):
    answer = ''
    i = seoul.index("Kim")
    answer = f"김서방은 {i}에 있다"
    return answer



# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def findKim(seoul):
    # 함수를 완성하세요

    return "김서방은 {}에 있다".format(seoul.index('Kim'))


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))



def solution(seoul):
    answer = ''
    return ('김서방은 %d에 있다' %seoul.index('Kim'))
    
    
    
def findKim(seoul):
    kimIdx = 0
    for kimIdx in range(len(seoul)):
        if seoul[kimIdx] == "Kim":
            return "김서방은 {}에 있다".format(kimIdx)

# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))



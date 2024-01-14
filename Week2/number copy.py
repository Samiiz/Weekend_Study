# def solution(s):
#     num_dict={
#         'zero':'0',
#         'one':'1',
#         'two':'2',
#         'three':'3',
#         'four':'4',
#         'five':'5',
#         'six':'6',
#         'seven':'7',
#         'eight':'8',
#         'nine':'9'
#     }
    
#     answer = ''
#     te=''
    
#     for char in s:
#         if char.isdigit():
#             answer +=char
#         else:
#             te +=char
#             if te in num_dict:
#                 answer +=num_dict[te]
#                 te=''
#     return answer
# print(solution('one4seveneight'))
# print(solution('23four5six7'))
# print(solution('2three45sixseven'))
# print(solution('123'))

# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)



def solution(s) :

    a = ['zero','one', 'two','three', 'four','five','six','seven','eight','nine']
    b = ['0','1','2','3','4','5','6','7','8','9']
    for key ,value in zip(a,b):
        s = s. replace(key, value)
    return int(s)


print(solution('one4seveneight'))
print(solution('23four5six7'))
print(solution('2three45sixseven'))
print(solution('123'))

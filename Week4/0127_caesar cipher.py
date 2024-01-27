# 수박수박수박수
def solution(n):
    answer = ""

    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += "박"
        else:
            answer += "수"
    return answer


# --------------------------------------------
# 시져암호


def solution(s, n):
    answer = ""

    for i in s:
        if i == " ":
            answer += " "

        elif i.islower():
            answer += chr((ord(i) - ord("a") + n) % 26 + ord("a"))

        elif i.isupper():
            answer += chr((ord(i) - ord("A") + n) % 26 + ord("A"))

    return answer


# --------------------------------------
# join comprehension


def solution(s, n):
    return "".join(
        [
            chr(
                ord(i)
                + (not ord(i) == 32)
                * (
                    (n % 26)
                    - 26
                    * (
                        (90 < (ord(i) + (n % 26)) * (ord(i) < 91))
                        + (122 < (ord(i) + (n % 26)))
                    )
                )
            )
            for i in s
        ]
    )


# ---------------------------------------


def caesar(s, n):
    str = []
    for x in list(s):
        if x == " ":
            str.append(x)
        elif ord(x.lower()) + (n % 26) <= ord("z"):
            str.append(chr(ord(x) + (n % 26)))
        else:
            str.append(chr(ord(x) + (n % 26) - 26))
    return "".join(str)


# -------------------------------------------------
def caesar(s: str, n):
    # ints = [ord(c) + n for c in s]
    ints = list()
    for c in s:
        if c.isalpha():
            if ord(c) <= ord("Z"):
                # 대문자
                num = (ord(c) - ord("A") + n) % (ord("Z") - ord("A") + 1) + ord("A")
                ints.append(num)
            else:
                # 소문자
                num = (ord(c) - ord("a") + n) % (ord("z") - ord("a") + 1) + ord("a")
                ints.append(num)
        else:
            ints.append(ord(c))
    enc_chars = [chr(i) for i in ints]

    result = "".join(enc_chars)

    return result

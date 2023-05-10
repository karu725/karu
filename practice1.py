# 숫자 자료형
print(5) # 5
print(-10) # -10
print(3.14) # 3.14
print(1000) # 1000
print(5 + 3) # 8
print(2 * 8) # 16
print(6 / 3) # 2.0
print(3 * (3 + 1)) # 12

# 문자열 자료형
print('풍선') # 풍선
print("나비") # 나비
print("abcdefg") # abcdefg
print("10") # 10
print("파이썬" * 3) # 파이썬파이썬파이썬
# print('작은따옴표") # 오류 발생
# print("큰따옴표') # 오류 발생      
print("I don't want to go to school") # 정상 출력
# print('I don't want to go to school') # 오류 발생

# boolean 자료형
print(5 > 10) # False
print(5 < 10) # True
print(True) # True
print(False) # False
print(not True) # False
print(not False) # True
print(not (5 > 10)) # True

# 변수
# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal +"의 이름은 " + name +"에요")
hobby = "공놀이" # 변수가 갱신됨
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name +"는 어른일까요? " + str(is_adult))

# 주석
# ctrl + /

# Quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명
#  : station

# 변수값
#  : "사당", "신도림", "인천공항" 순서대로 입력

# 출력문장
#  : XX 행 열차가 들어오고 있습니다.

station = "사당"

print(station + "행 열차가 들어오고 있습니다.")


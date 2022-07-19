print("숫자를 입력하세요")
num = input("숫자: ")
#print(num, type(num))

num = int(num)


if num > 0 :
    print("양수")
elif num < 0 :
    print("음수")
else :
    print("0")


print("종료")
'''
public int plus(int a, int b) {
    sum = a+b;
    return sum;
}
자바일 경우
'''

def plus(a,b):
    sum = a+b
    return sum

num = plus(3,7)
print(num)

result = plus("3", "한글")
print(result)

print("==================================")

def my_function():
    print("hello world")

my_function()

def noMsg():
    pass

print(noMsg())
print("==================================")

a,b = (1,2)
print(a)
print(b)

def sum_and_mul(a,b):
    sum = a+b
    mul = a*b
    return sum, mul

num1, num2 = sum_and_mul(3,7)
print(num1)
print(num2)

result = sum_and_mul(3,7)
print(result, type(result))
print(result[0])
print(result[1])

print("==================================")
def plusPrint(a=100,b=100):
    print("a=%d, b=%d 이고 합은 %d 입니다."%(a,b,a+b))

plusPrint(3,7)
plusPrint(7)
#plusPrint(,7) 오류
plusPrint(b=70) #a=100(기본값) b=70
plusPrint(b=7, a=3)

print("==================================")

def sum_many(name, *data):
    print(name)
    #data = (1,2,3,4,5)
    sum = 0
    for num in data:
        sum = sum + num

    return sum

print(sum_many("박깜이",1,2,3,4,5,6,7,8,9))

print("==================================")
def sum_mul(mode, *args):

    if mode == "sum" :
        result = 0
        for i in args:
            result = result + i
    elif mode == "mul":
        result = 1
        for i in args:
            result = result * i
    else:
        result = "오류"

    return result


print(sum_mul("sum", 1,2,3)) #더하기
print(sum_mul("mul", 5,6,7)) #곱하기
print(sum_mul("div"))

print("==================================")

def addPerson(hp, **kwargs):
    print(hp)
    print(kwargs)   #타입 딕션어리

addPerson('010-222-333', name='박깜이', age=12)

print("==================================")

def addPerson2(*hp, **kwargs):
    print(hp)   #타입 튜플
    print(kwargs) #타입 딕션어리

addPerson2('010-222-333', name='박깜이', age=12)
addPerson2('010-222-333', '010-222-333', name='박깜이', age=12)
addPerson2('010-222-333', '010-222-333', name='박깜이', age=12)
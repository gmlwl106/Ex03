
for x in range(10) :
    print(x, end=" ")

print("\n============================================")

for x in range(0, 10, 2) :
    print(x, end=" ")

print("\n============================================")

for x in range(5, -6, -1) :
    print(x, end=" ")

print("\n============================================")

friendList = [('둘리', 10), ('마이콜', 20), ('도우너', 30)]
for i in range(0, 2) :
    name = friendList[i][0]
    age = friendList[i][1]
    print("이름:%s, 나이:%d"%(name, age))
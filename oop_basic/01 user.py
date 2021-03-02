# - *- coding: utf- 8 - *-

class User:

    count = 0

    def __init__(self, name, age, pw):
        self.name = name
        self.age = age
        self.pw = pw
        User.count += 1

    def checkpw(self, pw):
        if self.pw == pw:
            return "Correct pw"
        else:
            return "Incorrect pw"



user1 = User("kim",12,"1234")
user1.email = "abc@gmail.com"
user1.count = 15
#같은이름의 클래스변수, 인스턴스변수 -> 인스턴스변수 호출

user2 = User("lee",13, "1111")
user3 = User ("jun",18 , "1122")


print(user1.name)
print(user1.email)
print(user1.checkpw("1111"))
print(User.count) #3
print(user1.count)#15
print(user2.count)#3
print(user3.count)#3
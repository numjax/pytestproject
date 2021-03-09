# - *- coding: utf- 8 - *-

from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def print_msg(self):
        pass

    @abstractmethod
    def send_msg(self):
        pass

class Email(Message):
    def __init__(self, body, sender):
        self.body = body
        self.sender = sender

    def print_msg(self):
        print("Email body:{}".format(self.body))

    def send_msg(self, receiver):
        print("Send email from {} to {}".format(self.sender, receiver))


class SMS(Message):
    def __init__(self, txt, phone_num):
        self.txt = txt
        self.phone_num =phone_num

    def print_msg(self):
        print("SMS txt:{}".format(self.txt))

    def send_msg(self, receiver):
        print("Send SMS from to {}".format(receiver))

class Katok(Message):
    def __init__(self, txt, katokID):
        self.txt = txt
        self.katokID = katokID

    def print_msg(self):
        print("katok")

email1 = Email("emailbody","abc@gmail.com")

email1.print_msg()
email1.send_msg("def@gmail.com")



# from abc import ABC, abstractmethod
#
# class Message(ABC):
#     @abstractmethod
#     def print_message(self) -> None:
#         pass
#
#     @abstractmethod
#     def send(self, destination: str) -> None:
#         pass
#
# class Email(Message):
#     def __init__(self, content, user_email):
#         self.content = content
#         self.user_email = user_email
#
#     def print_message(self):
#         print("이메일 내용입니다:\n{}".format(self.content))
#
#     def send(self, destination):
#         print("이메일을 주소 {}에서 {}로 보냅니다!".format(self.user_email, destination))
#
#
# class SMS(Message):
#     def __init__(self, content, user_cellphone_num):
#         self.content = content
#         self.user_cellphone_num = user_cellphone_num
#
#     def print_message(self) -> None:
#         print("SMS conent: \n {}".format(self.content))
#
#     def send(self, destination: str) -> None:
#         print("send SMS from {} to {}".format(self.user_cellphone_num, destination))
#
#
# class Katok(Message):
#     def __init__(self, content, user):
#
# # 이메일 인스턴스를 생성한다.
# email = Email("안녕? 오랜만이야 잘 지내니?", "young@codeit.kr")
#
# # 메시지 내용 출력
# email.print_message()
# # 메시지 전송
# email.send("captain@codeit.kr")
#

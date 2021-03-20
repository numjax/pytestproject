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
        print("Katok!!: {}".format(self.txt))

    def send_msg(self, receiver):
        print("Send katok to {}".format(receiver))



class MessageSender:
    def __init__(self):
        self.msgs = []

    def add_msg(self, new_msg):
        self.msgs.append(new_msg)

    def send_all(self):
        for i in self.msgs:
            i.print_msg()

email1 = Email("email body","abc@gmail.com")
email1.receiver = "def@gmail.com"
email1.print_msg()
email1.send_msg(email1.receiver)


sms1 = SMS("sms txt","111-222-3333")
sms1.receiver = "333-444-5555"
sms1.print_msg()
sms1.send_msg(email1.receiver)


katok1 = Katok("katok msg","John")
katok1.receiver = "Tom"
katok1.print_msg()
katok1.send_msg(email1.receiver)

msg_sender1=MessageSender
msg_sender1.add_msg("aa","bb")
msg_sender1.send_all()
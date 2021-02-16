class CreditCard:

    MAX_PAYMENT_LIMIT = 300000000

    def __init__(self, name, password, payment_limit):
        self._name = name
        self._password = password
        self._payment_limit = payment_limit

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_password(self):
        return "비밀번호는 볼 수 없습니다."

    def set_password(self, password):
        self._password = password

    def get_payment_limit(self):
        return self._payment_limit

    def set_payment_limit(self, payment_limit):
        if 0 <= payment_limit <= self.MAX_PAYMENT_LIMIT :

            self._payment_limit = payment_limit
        else:
            print ("0원 ~ {}원 사이로 설정해 주세요.".format(self.MAX_PAYMENT_LIMIT))


card = CreditCard ("Kang Young Hoon", "1234" , 1000000)

print (card.get_name ())
print (card.get_password())
print (card.get_payment_limit())

card.set_name("Sung Tea Ho")
card.set_password("1234")
card.set_payment_limit(-10)

print (card.get_name ())
print (card.get_password())
print (card.get_payment_limit())

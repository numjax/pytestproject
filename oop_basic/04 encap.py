# - *- coding: utf- 8 - *-

class CreditCard:
    MAX_PAYMENT_LIMIT = 3000000

    #인스턴스 변수 앞에 던더를 붙이면 변수를 숨긴다
    def __init__(self, name, password, payment_limit):
        self.name = name
        self.__password = password
        self.__payment_limit = payment_limit

    @property
    def password(self):
        return "Can not display"

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def payment_limit(self):
        return self.__payment_limit

    @payment_limit.setter
    def payment_limit(self, new_payment_limit):
        if new_payment_limit >= 0 and new_payment_limit <= MAX_PAYMENT_LIMIT:
            self.__payment_limit = new_payment_limit
        else:
            print("The limit should be between 0 and 3 million.")



card = CreditCard("kang", "1234", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "kim"
card.password = "1111"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)

'''
중요한 속성의 경우 객체로 바로 접근해서 수정하는 것을 막아야 한다. 
또는 감추거나 변경할 수 없게 해야 한다.

보통 던더+변수명 하면 private로 설정되어 클래스 내부에서만 접근 가능해진다. 
던더를 적으면 파이썬에서는 해당 변수또는메서드명의 네임 맹글링이 발생하는데 
__name
_User__name
'_클래스명__변수또는메서드명'형태로 바뀐다. 
하지만, 이것 역시 네임 맹글링 룰을 알고있는 개발자라면 숨긴 변수에 
바로 접근해서 사용할 수 있다는 단점이 있다. 
(물론 이렇게 하는 변태 개발자는 없겠지만서도 말이다.)

어쨋든 일반적인 객체지향 프로그래밍 언어에서는 
캡슐화를 접근제어자(Access Modifier)를 통해 구현한다.
하지만 파이썬에는 특별한 접근 제어자가 없고 
네임맹글링 룰을 알고 있는 개발자는 언제든 접근이 가능한 단점도 있다.(강제할 방법이 없다)

어쨋든 파이썬은 변수나 메서드의 작명법을 통해 접근제어자를 표기한다.

접근 제어자에는 public , private , protected , default 가 있다.
파이썬에서의 작명법은 아래와 같다.
public → 접두사에 아무 밑줄이 없다. -전역에서 접근가능
private → 접두사에 두개의 밑줄(__)을 적용 - 그 클래스 안에서만 접근 가능
protected → 접두사에 한개의 밑줄(_) 을 적용 - 그 클래스 및 클래스를 상속한 
                                        자식 클래스에서 접근가능
default -> 파이썬에는 존재하지 않는다. - 해당 모듈, 패키지 안에서만 접근가능'''

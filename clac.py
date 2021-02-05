class Calc:

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

    @staticmethod
    def mul(a,b):
        return a*b

    @staticmethod
    def div(a,b):
        return a/b


calc = Calc()

print (calc.add(2,3))
print (calc.sub(2,3))
print (calc.mul(2,3))
print (calc.div(2,3))

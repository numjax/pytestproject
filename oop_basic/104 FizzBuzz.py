
class Game:
    def __init__(self, start_num, end_num):
        self.start_num = start_num
        self.end_num = end_num

    def start(self):

        numbers_to_check = [3,5]
        numbers_to_say = ["Fizz","Buzz"]

        while self.start_num <= self.end_num:

            mystring =""

            for i in range(len(numbers_to_check)):
                if self.start_num % numbers_to_check[i] == 0 :
                    mystring += numbers_to_say[i]

            if mystring=="":
                mystring = self.start_num

            print(mystring)

            self.start_num +=1


game1 = Game(1,20)
game1.start()
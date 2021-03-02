# - *- coding: utf- 8 - *-


def print_hello():
    print("hello")


def add_print_to(original):
    def wrapper():
        print ("begin")
        original()
        print ("end")

    return wrapper


#이렇게 하면 함수 자체가 정의됨
#그러니까 함수 코드가 정의되고 실행이 되지 않은 상태가 됨.
print_hello

#이렇게 하면 함수실행
print_hello()

#아래도 재미있는 실험
add_print_to(print("hello"))
'''
위와 같이 적으면 print("hello")가 일단 실행됨. 그래서 hello라고 콘솔에 찍히고
그다음은 add_print_to함수가 실행되는데, 마지막 줄에 wrapper가 리턴됨.
그런데, wrapper는 함수 자체로 리턴만 되고 실제 실행이 안되기 때문에 그냥 빈칸 출력.
'''


#아래도 재미있는 실험
add_print_to(print("hello"))()
'''
위와 같이 적으면 print("hello")가 일단 실행됨. 그래서 hello라고 콘솔에 찍히고
그다음은 add_print_to함수가 실행되는데, 마지막 줄에 wrapper가 리턴됨.
그런데, 마지막에 괄호가 있기 때문에 아래와 같이 해석됨.
add_print_to(print("hello"))()  ->   wrapper()
그래서 wrapper함수가 실행되는데 일단 첫줄인 print ("begin")가 실행되어 begin이 찍힘.
함수 중간에 orignal()이라는 구문에서 
print("hello")가 호출됨. 
그런데 original()이기 original이 실행된 리턴값을 가져와야 하는데 해당 구문에는 리턴값이 없음.
그래서 NoneType은 호출할 수 없다는 에러 발생. 
'''


#이렇게 하면 리턴값에 wrapper만 기술되고 실행 자체가 안됨.
add_print_to(print_hello)
'''
위를 실행하면 이렇게 됨. 
add_print_to(print_hello)  -> wrapper
그러니까. 함수만 리턴되고 실행은 안된다.
'''

#아래와 같이 하면 함수의 주소가 출력된다.
print(add_print_to(print_hello))
'''
print(add_print_to(print_hello)) -> print(wrapper)
-> print(wrapper의 주소)
<function add_print_to.<locals>.wrapper at 0x0000026D60A6CEE8>
'''


# 이렇게 하면 변수에 함수가
add_print_to(print_hello())
'''
print_hello()를 parameter 위치에 주었을 땐 print_hello 함수가 그냥 호출되어 버린다.
이때, 중요한 것은 이 호출 후 리턴값이 없다는 것을 기억해야 한다.
그러니까 이렇게 된다. 
add_print_to(print_hello())   -> add_print_to("hello")

그래서 add_print_to가 실행될 때 
wrapper의 original()구문에서 호출한 함수의 리턴값이 없으므로  
None이 들어가고 add_print_to 함수에서는 에러를 가지고 있는 wrapper 함수를 return 합니다.

하지만 오류가 발생하지 않았던 이유는 add_print_to(print_hello()) 뒤에 ()를 붙이지 않았기 때문입니다.
즉, 오류가 있는 함수가 정의되었지만 실행은 안되었기 때문에 오류가 나오지 않았습니다.

요약하자면, 아래 방식은 함수를 다시 실행시키지 않았기 때문에 'begin'과 'end'이라는 
문자열이 출력되지 않았으며 None 값이 들어가면서 add_print_to 함수의 return 함수를 실행할 경우 
에러가 발생할 예정입니다.
'''


#그렇기 때문에 아래와 같이 적으면 정상적으로 실행
#add_print_to(print_hello)()   ->    wrapper()
add_print_to(print_hello)()
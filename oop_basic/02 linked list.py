# - *- coding: utf- 8 - *-

'''
단방향 링크드 리스트
왼쪽에 데이터, 오른쪽에 다음노드
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):

        new_node = Node(data)

        #empty linked list
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else: #linked list has a value
            #current tail
            self.tail.next = new_node
            #change current tail
            self.tail = new_node

    def __str__(self):

        iter = self.head

        return_str = ""
        cnt = 0

        while iter is not None:
            if cnt != 0:
                return_str += ", "

            return_str = return_str + str(iter.data)
            iter = iter.next

            cnt += 1

        return return_str

# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 링크드 리스트에 데이터 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

print(linked_list)  # 링크드 리스트 출력


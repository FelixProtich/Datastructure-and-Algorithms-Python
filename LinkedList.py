'''
    A linked list is a data structure for storing a sequence of elements.
    Structure:
        HEAD ---> data|next ---> data|next ---> NULL

    operations:
        Create elements, display elements, find no. of elements, retrieve element, add or
        remove element.

'''
class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

#define class for linkedlist
class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    #method to print
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
    
    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None

    def reverse(l):
        if l.head is None:
            return

        current_node = l.head
        prev_node = None

        while current_node is not None:
            #Track the next node
            next_node = current_node.next

            #modify current node
            current_node.next = prev_node

            #update prev and current
            prev_node = current_node
            current_node = next_node
        
        l.head = prev_node


list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(4)

list2.show_elements()
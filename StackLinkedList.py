class Node :
    def __init__ (self , value = None):
        self.value = value 
        self.next = next
class LinkedList :
    def __init__(self) :
        self.head = None 
class Stack :
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False 
#customStack = Stack()
#print(customStack.isEmpty())
    def __str__(self):
        current = self.LinkedList.head
        stack_contents = []
        while current:
            stack_contents.append(str(current.value))
            current = current.next
        return "\n".join(stack_contents)
    #push
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    #pop 
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else :
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    #peek 
    def peek(self):
        if self.isEmpty():
            return " there is not any element is in stack"
        else:
           nodeValue = self.LinkedList.head.value
           return nodeValue
    #delete 
    def delete(self):
        self.LinkedList.head = None
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print ("____________")
customStack.pop()
print(customStack.delete())
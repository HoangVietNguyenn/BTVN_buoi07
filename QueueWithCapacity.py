class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1 
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ''.join(values)
    def isFull (self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True 
        else:
            return False
    def isEmpty(self):
        if self.top == -1:
            return True 
        else :
            return False
    def enqueue (self,value):
        if self.isFull():
            return "The queue is full"
        else :
            if self.top +1 == self.maxSize :
                self.top += 0
            else :
                self.top += 1
                if self.start == -1 :
                    self.start = 0
            self.items[self.top] = value
            return " The element is inserted at the end of Queue "
    def dequeue (self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else :
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1 
                self.top = -1
            elif self.start +1 == self.maxSize:
                self.start = 0
            else :
                self.start += 1
            self.items[start] = None 
            return firstElement
    def peek ( self):
        if self.isEmpty ():
            return " There is not any element in the Queue"
        else :
            return self.items [self.start]
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1 
        self.start =-1 
# Tạo một hàng đợi có kích thước tối đa là 5
my_queue = Queue(5)

# Kiểm tra hàng đợi có rỗng không
print("Is queue empty?", my_queue.isEmpty())  # Kết quả sẽ là True vì hàng đợi mới được tạo chưa có phần tử nào

# Thêm một số phần tử vào hàng đợi
print(my_queue.enqueue(1))  # Kết quả sẽ là " The element is inserted at the end of Queue "
print(my_queue.enqueue(2))  # Kết quả sẽ là " The element is inserted at the end of Queue "
print(my_queue.enqueue(3))  # Kết quả sẽ là " The element is inserted at the end of Queue "

# Kiểm tra phần tử đầu tiên của hàng đợi
print("First element:", my_queue.peek())  # Kết quả sẽ là 1

# Loại bỏ một phần tử khỏi hàng đợi
print("Removed element:", my_queue.dequeue())  # Kết quả sẽ là 1

# Kiểm tra phần tử đầu tiên của hàng đợi sau khi loại bỏ
print("First element after removal:", my_queue.peek())  # Kết quả sẽ là 2

# Kiểm tra xem hàng đợi có đầy không
print("Is queue full?", my_queue.isFull())  # Kết quả sẽ là False vì hàng đợi vẫn chưa đầy

# Xóa tất cả các phần tử trong hàng đợi
my_queue.delete()

# Kiểm tra xem hàng đợi có rỗng sau khi xóa
print("Is queue empty after deletion?", my_queue.isEmpty())  # Kết quả sẽ là True vì tất cả các phần tử đã được xóa
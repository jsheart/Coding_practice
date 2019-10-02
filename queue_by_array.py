class Queue:
      def __init__(self, n):
            self.size = n
            self.queue = [0] * n
            self.head = -1
            self.tail = -1
            
      def is_empty(self):
            if self.head == self.tail == -1:
                  return True
            else:
                  return False
            
      def __is_full(self):
            if (self.tail + 1) % self.size == self.head:
                  return True
            else:
                  return False
            
      def enqueue(self, num):
            if self.is_empty():
                  self.head = 0
                  self.tail = 0
            else:
                  self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = num
                  
      def dequeue(self):
            if self.is_empty():
                  print("empty queue")
                  return
            elif self.head == self.tail:
                  value = self.queue[self.head]
                  self.head, self.tail = -1, -1
                  return value
            else:
                  value = self.queue[self.head]
                  self.head = (self.head + 1) % self.size
                  return value     
      
      def front(self):
            return self.queue[self.head] if self.head != -1 else None
      
      def extend_queue(self, new_size):
            if self.is_empty():
                  self.queue = [0] * new_size
                  self.size = new_size
            else:
                  temp = []
                  while not self.is_empty():
                        temp.append(self.dequeue())
                  self.head = 0
                  self.tail = len(temp) - 1
                  self.queue = temp + [0] * (new_size - self.size)                
                  self.size = new_size
                  
            
      def __str__(self):
            return ' '.join(str(v) for v in self.queue) if self.queue else 'Empty queue'
if __name__ == '__main__':
      q = Queue(5)
      q.enqueue(1)
      q.enqueue(2)
      q.enqueue(3)
      q.enqueue(4)
      q.dequeue()
      q.dequeue()
      q.enqueue(5)
      q.enqueue(6)
      q.enqueue(7)
      print(q)
      q.extend_queue(8)
      q.enqueue(8)
      q.enqueue(9)
      q.enqueue(10)
      print(q)
      print(q.dequeue())
      print(q.dequeue())
      print(q)
      

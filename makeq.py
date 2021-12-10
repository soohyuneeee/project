import queue
 
a = 7
# Queue 선언
q = queue.Queue()
 
# q에 데이터 추가
q.put('빨간색')
q.put('주황색')
q.put('노란색')
q.put('초록색')
q.put('파란색')
q.put('남색')
q.put('보라색')
 
# q에서 첫번째 원소 제거
print(q.get()) # 1
print(q.get()) # 2
print(q.get()) # 3
print(q.get()) # 4

print(q.queue)
from collections import deque
 
class Queue(deque):
 
    def enqueue(self, x):
        super().append(x)
 
    def dequeue(self):
        super().popleft()
 
    def display(self):
        for node in self.__iter__():
            print(node)
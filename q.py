Queue_item = []
# Enqueue 기능 구현
def Enqueue(x):
    Queue_item.append(x)
    return None

# Dequeue 기능 구현
def Dequeue():
    item_length = len(Queue_item)
    if item_length < 1:
        print("젤리가 없어요!")
        return False
    result = Queue_item[0]
    del Queue_item[0]
    return result

# isEmpty 기능 구현
def isEmpty():
    return not Queue_item
    




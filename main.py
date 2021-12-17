#함수를 만들어야해용ㅇㅇㅇ 함수 만들기 ~~~
#배열만들기
#해야 할 것
#1.jelly를 큐로 바꾸기
#2.hj,wj를 큐에서 가져온 jelly로 바꾸기
class Queue():
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.queue[0]
            self.queue = self.queue[1:]
            
        return dequeue_object
            
    def peek(self):
        peek_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            peek_object = self.queue[0]
            
        return peek_object
            
    def isEmpty(self):
        is_empty = False
        if len(self.queue) == 0:
            is_empty = True
        return is_empty

que=Queue()

que.enqueue('빨간색')
Queue.enqueue('주황색')
Queue.enqueue('노란색')
Queue.enqueue('초록색')
Queue.enqueue('파란색')
Queue.enqueue('남색')
Queue.enqueue('보라색')
print(Queue)
def search_list(n, x):  #젤리 위치를 파악해 몇번째에 위치했는지 리턴해주는 코드
    for i in range(0, n): 
        if x == jelly[i]: 
            return i 
    return -1 
def search_list2(n,x):  #젤리 위치를 파악해 젤리의 이름을 리턴해주는 코드
    for i in range(0,n):
        if hj[0]== jelly[i]:
            return jelly[i]
    return -1
#que=q.Queue
#print(que)


print("이 자판기는 젤리를 파는 자판기 입니다. 당신이 원하는 젤리는 무엇인가요~!!~!\n 단 본 자판기는 정해진 규칙이 있습니다..!\n 자판기 안의 젤리는 빨간색 주황색 노란색 초록색 파란색 남색 보라색 순으로 준비되어 있습니다.\n 그리고 본 자판기는 여러분이 원하는 젤리를 먹을 수 있게 계산해주는 시스템을 가지고 있습니다.\n여러분이 원하는 젤리는 몇번째에 위치할까요?")
while(True):
    choicetype=int(input("질문에 응답해주세여.\n 1.원하는 색의 젤리를 구매하러 왔다. 2.원하지 않는 젤리 이외의 아무 젤리를 구매하러 왔다. 3.아무젤리나 상관없이 구매하러 왔다. 4.이 프로그램을 그만하고 싶다.\n"))
    jelly=['빨간색','주황색','노란색','초록색','파란색','남색','보라색']
    if choicetype==3:
        print("200원 넣고 바로 구매 하시면 됩니다!")
        break
    




    elif choicetype==2: 
        print("원하지 않는 젤리가 있으시군요!")
        hj=['빨간색','주황색','노란색','초록색','파란색','남색','보라색']
        hj.remove(input("원하지 않는 젤리 색을 선택해주세요!\n 빨간색, 주황색, 노란색, 초록색, 파란색, 남색, 보라색\n"))
        for i in range(7):
            yesno=int(input("원하지 않는 젤리가 더 있습니까?\n 1.Yes 2.No\n"))
            if yesno==2:
                break
            else:
                print(hj)
                hj.remove(input("원하지 않는 젤리 색을 선택해주세요!\n"))
        print("구매자께서 원하는 젤리는 ",hj,"입니다.")
        print("원하시는 젤리 위치를 탐색하여서 가장 적은 돈으로 먹을 수 있는 원하시는 젤리를 찾아드리겠습니다.")
        print("젤리 위치 찾는 중 ...")
        print(hj)
        print(search_list2(len(hj),hj),"맛을 구매 가장 저렴하게 구매 하실수 있습니다.")
        yesorno=int(input("구매하시겠습니까?\n1:yes,2:no\n"))
        if yesorno==1:
            print(search_list(len(hj),search_list2(len(hj),hj))*200,"원을 지불하세요")
            break
        if yesorno==2:
            print("처음으로 돌아갑니다.")

        






    elif choicetype==1:
        print("원하는 색깔의 젤리가 있으시군요!\n")
        wj=input("원하는 색깔의 젤리를 선택해주세요.\n 빨간색, 주황색, 노란색, 초록색, 파란색, 남색, 보라색\n")
        print((search_list(7, wj)+1),"개의 젤리를 뽑으셔야 합니다")
        yesorno=int(input("구매하시겠습니까?\n1:yes,2:no\n"))
        if yesorno==1:
            print((search_list(7, wj)+1)*200,"원을 지불하세요")
            break
        if yesorno==2:
            print("처음으로 돌아갑니다.")




    else:
        print("프로그램을 종료합니다.")
        break
    
        
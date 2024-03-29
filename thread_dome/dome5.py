#encoding:utf-8

import threading
import random
import time

gMoney=1000
gTotalTimes=10
gTimes=0
gCondition=threading.Condition()
class producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money=random.randint(100,1000)
            gCondition.acquire()
            if gTimes >=10:
                gCondition.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gTimes +=1
            gCondition.notify_all()
            gCondition.release()
            time.sleep(0.4)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money=random.randint(100,1000)
            gCondition.acquire()
            while gMoney < money:
                if gTimes >=gTotalTimes:
                    gCondition.release()
                    return
                print('%s准备消费%d元钱，剩余%d元钱，不足'%(threading.current_thread(),money,gMoney))
                gCondition.wait()
            gMoney-=money
            print('%s消费了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gCondition.release()
            time.sleep(0.5)

def main():
    for x in range(3):
        t=Consumer(name="消费者线程%d"%x)
        t.start()
    for x in range(5):
        t=producer(name="生产者线程%d"%x)
        t.start()

if __name__ == '__main__':
    main()
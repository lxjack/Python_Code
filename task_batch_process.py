#_*_ coding: utf-8 _*_
from time import sleep,ctime
import threading

work_quence=[(1,1),(1,2),(1,3),(1,4),(1,5),(2,1),(2,2),(2,3),(2,4),(2,5)]
thread_resource=0
thread_resource_limit=2

def work_func(order, work_time):
    global thread_resource
    print 'start work (%s,%s)' % (str(order), str(work_time)), ctime()
    sleep(work_time)
    thread_resource = thread_resource - 1  #工作线程结束工作  资源--
    print 'end work (%s,%s)' % (str(order), str(work_time)), ctime()


while len(work_quence)> 0:       #当任务序列不为空时
    if thread_resource ==0 :     #线程资源全空闲时 修改current_order
        current_order=work_quence[0][0]
        print "thread resource is all released,current order %s" % str(current_order)

    next_order=work_quence[0][0]

    if current_order==next_order and thread_resource < thread_resource_limit:  #是当前的处理order并且有多余的线程资源
        #开启线程工作
        thread_resource = thread_resource + 1  # 启动工作线程  线程资源++
        order,work_time=work_quence.pop(0)
        t=threading.Thread(target=work_func,args=(order,work_time))
        t.start()
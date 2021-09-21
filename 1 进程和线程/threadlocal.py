def process_student(name):
    std = Student(name)
    #std是局部变量，但是每个函数都要用到它，因此必须传进去
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)

global_dict ={}

def std_thread(name):
    std = Student(name)
    #把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()
import threading

#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student:
    local_school.student = name
    process_student()



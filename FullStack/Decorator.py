#装饰器： 在不更改原函数代码以及调用方式的前提下，为其增添新的功能
#装饰器本质，闭包
#https://www.bilibili.com/video/BV1aJ411H7Ej?p=79


import time

def timer1(f):
    #f = test  f is the real test
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print("Execution time:", end_time - start_time)

    return inner

#timer1 no return
# Have return value
def timer2(f):
    def inner():
        start_time = time.time()
        result = f()
        end_time = time.time()
        print("Execution time:", end_time - start_time)
        return result
    return inner

# have args
def timer3(f):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print("Execution time:", end_time - start_time)
        return result
    return inner
import sys

if __name__ == "__main__":
    # @timer1
    # def test():  # test == inner
    #     time.sleep(1)
    #     return
    #
    # @timer3
    # def test1(*args, **kwargs): #call test is equivalent to call inner
    #     print("This is args:", *args)
    #     time.sleep(1)
    #     return
    #
    # test1("this is good", "how is this")
    print(sys.path)


#apply for python 3.5 or later

import asyncio


"""
async & await key words

"""

# async def func1():
#     print(1)
#     await asyncio.sleep(1)
#     print(2)
#
# async def func2():
#     print(3)
#     await asyncio.sleep(2)
#     print(4)
#
# task = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(task))


# 异步
# 检测并执行某些代码
#伪代码

# 任务列表 = 【任务1， 任务2， 任务3，... , 任务n】
#
# while True:
#     task list, completed task list = 检查任务列表中任务，将"可执行"和"已完成"任务返回
#
#     for task in task list：
#     执行task
#
#     for completed task in completed task：
#     remove completed task in 任务列表
#
# 如果任务列表任务都完成，终止训话

# loop = asyncio.get_event_loop()
# loop.run_until_complete(func())
#
# = asyncio.run(func())  #python 3.7 or later
#
# 在事件循环中添加对象
# Task
# 添加多个任务， task用于并发调度携程，通过使用
# asyncio.create_task(coro)让携程加入时间循环中，等待着别调用。除了使用syncio.create_task(coro)外，可以使用loop.create_task or ensure_future()

# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#
#
# async def main():
#     task = [
#         asyncio.create_task(func()),
#         asyncio.create_task(func())
#     ]
#
#     await asyncio.wait(task)
#
# if __name__=="__main__":
#     asyncio.run(main())

#Future对象

# Task对象继承future对象， Task await结果基于future对象而来

# async def set_after(fut):
#     await asyncio.sleep(2)
#     fut.set_result('666')
#
#
#
# async def main():
#     loop = asyncio.get_running_loop()
#     fut = loop.create_future()
#     await loop.create_task((set_after(fut)))
#
#     data = await fut
#     print(data)
#
# asyncio.run(main())
#
# 3.5 Future  线程/进程 异步编程
# concurrent.futures.thread
# concurrent.futures.process
# import time
# import asyncio
# import concurrent.futures
#
# def func(value):
#     time.sleep(1)
#     return "This is func return"

# async def main():
#     """
#     1/ run in defaul loop executor (default threadPoolExecutor)
#        内部会调用 threadPoolExecutor中的submit方法，向线程池中申请一个线程去执行func,并且返回一个 concurrent.futures.future对象
#        调用asyncio.wrap_future将concurrent.futures.future对象封装成asyncio.future对象。因为concurrent.futures.future对象不支持await，
#        需要转化成asynio.future对象
#
#
#
#     :return:
#     """
#     loop = asyncio.get_running_loop()
#     fut = loop.run_in_executor(None,func)
#     result = await fut
#
#     # #run in customized pool
#     # with concurrent.futures.ThreadPoolExecutor() as pool:
#     #     result = loop.run_in_executor(pool,func)
#
#     # #run in customized pool
#     # with concurrent.futures.ProcessPoolExecutor() as pool:
#     #     result = loop.run_in_executor(pool,func)


# 3.6 asyncio + 不支持异步的模块
# e.g 爬虫


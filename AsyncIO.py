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

class WebsocketConnection:

    def __init__(self, api_key, secret_key, uri, watch_dog, request):
        self.__thread = None
        self.url = uri
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.request = request
        self.__watch_dog = watch_dog
        self.delay_in_second = -1
        self.ws = None
        self.last_receive_time = 0
        # self.logger = logging.getLogger("binance-futures")
        # self.state = ConnectionState.IDLE
        # # global connection_id
        # connection_id += 1
        # self.id = connection_id

testobj = WebsocketConnection('api_key','secret_key','url','watch_dog','request')
print(testobj)

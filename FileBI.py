# import asyncio
# import aiohttp
#
# async def fetch(session, url):
#     print(" Sending Request", url)
#     async with session.get(url, verify_ssl=False) as response:
#         text = await response.text()
#         print("Result", url, len(text))
#     return text
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         url_list = ['www.google.com',
#                     "www.pythonav.com"
#                     ]
#         task_list = [asyncio.create_task(fetch(session,i)) for i in url_list]
#
#         done, pending = await asyncio.wait(task_list)
# if __name__ == "__main__":
#     asyncio.run(main())

a = 0.0003
print(('%.20f'%a)[slice(0,16)].rstrip('0'))
print(a)
print(slice(0,16))
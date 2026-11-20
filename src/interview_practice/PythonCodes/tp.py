import asyncio
import threading

# async def fun1(name):
#     await asyncio.sleep(2)
#     print(name)
#     return name
# async def fun2(name):
#     await asyncio.sleep(2)
#     print(name)

# async def main():
#     f1 = asyncio.create_task(fun1("Awduw"))
#     f2 = asyncio.create_task(fun2('qwe'))
#     n1 = await f1
#     await f2

#     print(n1)

# t1 = threading.Thread(target=lambda: asyncio.run(main()))
# t1.start()

# t1.join()
# print("end")

import time

def func1(name):
    time.sleep(3)
    print("f1", name)
def func2():
    time.sleep(2)
    print("f1")

t1 = threading.Thread(target=func1, args=["Aaksh"])
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
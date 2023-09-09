"""
no idle time allowed:
3 functions: each has idle time of 8
"""
import asyncio


async def one():
    print("first starts")
    await asyncio.sleep(8)
    print("first ends")

async def two():
    print("second starts")
    await asyncio.sleep(8)
    print("second ends")

async def three():
    print("third starts")
    await asyncio.sleep(8)
    print("third ends")

async def main():
    await asyncio.gather(one(), two(), three())

if __name__ == "__main__":
    asyncio.run(main())
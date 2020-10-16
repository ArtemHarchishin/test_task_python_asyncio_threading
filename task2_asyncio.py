import asyncio


async def task(t, msg):
    await asyncio.sleep(t)
    print(msg)


async def main():
    data = ((1, 'hi'), (2, 'bye'), (3, 'fff'))
    tasks = [asyncio.ensure_future(task(t, msg)) for t, msg in data]
    await asyncio.wait(tasks)


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(main())
ioloop.close()

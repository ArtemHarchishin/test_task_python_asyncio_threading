import asyncio


async def task(t, msg):
    if not t:
        while True:
            await asyncio.sleep(1)
            print(msg)
    await asyncio.sleep(t)
    print(msg)


async def main():
    data = ((1, 'hi'), (0, 'bye'), (3, 'fff'))
    tasks = [asyncio.ensure_future(task(t, msg)) for t, msg in data]
    await asyncio.wait(tasks)


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(main())
ioloop.close()

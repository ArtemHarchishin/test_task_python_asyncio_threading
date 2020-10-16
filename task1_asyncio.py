import asyncio

loop = asyncio.get_event_loop()


async def task(t, msg):
    await asyncio.sleep(t)
    print(msg)


async def main():
    data = ((3, 'hi'), (1, 'bye'), (3, 'fff'))
    tasks = [loop.create_task(task(t, msg)) for t, msg in data]


loop.run_until_complete(main())
loop.close()


import asyncio

async def producer(queue):
    for i in range(5):
        item = f'data-{i}'
        print(f'[Producer] Produced {item}')
        await queue.put(item)
    await queue.put(None)

async def consumer(queue, processed):
    while True:
        item = await queue.get()
        if item is None:
            await queue.put(None)
            break
        result = item.upper()
        print(f'[Consumer] Consumed {item} -> {result}')
        processed.append(result)

async def aggregator(processed, future):
    while len(processed) < 3:
        await asyncio.sleep(0)
    summary = ','.join(processed[:3])
    print(f'[Aggregator] Aggregated: {summary}')
    future.set_result(summary)

async def notifier(future):
    result = await future
    print(f'[Notifier] Got aggregated result: {result}')

async def future_setter(future):
    await asyncio.sleep(0)
    future.set_result('Manual future set!')

async def future_waiter(future):
    result = await future
    print(f'[FutureWaiter] Got manual future: {result}')

async def main():
    queue = asyncio.Queue()
    processed = []
    agg_future = asyncio.Future()
    manual_future = asyncio.Future()

    await asyncio.gather(
        producer(queue),
        consumer(queue, processed),
        aggregator(processed, agg_future),
        notifier(agg_future),
        future_setter(manual_future),
        future_waiter(manual_future),
    )

if __name__ == '__main__':
    asyncio.run(main())

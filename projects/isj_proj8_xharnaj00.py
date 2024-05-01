import asyncio
import aiohttp

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return response.status, url
    except Exception as e:
        return type(e).__name__, url

async def get_urls(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        responses = await asyncio.gather(*tasks)
    return responses

if __name__ == '__main__':
    urls = ['https://www.fit.vutbr.cz', 'https://www.szn.cz', 'https://www.alza.cz', 'https://office.com', 'https://aukro.cz']

    # for MS Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    res = asyncio.run(get_urls(urls))

    print(res)

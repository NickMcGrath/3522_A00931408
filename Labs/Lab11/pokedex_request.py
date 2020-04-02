import aiohttp
import asyncio


class Moves:
    def __init__(self, name: str, id_: int, generation: str, accuracy: int,
                 pp: int, power: int, type_: str, damage_class: str,
                 effect_short: str):
        self.name = name
        self.id = id_
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type = type_
        self.damage_class = damage_class
        self.effect_short = effect_short


class APIClass:
    @classmethod
    async def get_json(cls, url: str, session: aiohttp.ClientSession):
        response = await session.request(method='GET', url=url)
        json_response = await response.json()
        return json_response

    @classmethod
    async def process_requests(cls, id_list: list):
        url = 'https://pokeapi.co/api/v2/ability/{}'
        async with aiohttp.ClientSession() as session:
            list_urls = [url.format(req_id) for req_id in id_list]
            coroutines = [cls.get_json(a_url, session) for a_url in list_urls]
            responses = await asyncio.gather(*coroutines)
            print(responses)


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response = loop.run_until_complete(APIClass.process_requests([1, 2]))
    print(response)
    print(type(response))

if __name__ == '__main__':
    main()

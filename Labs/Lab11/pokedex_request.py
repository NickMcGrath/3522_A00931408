import aiohttp
import asyncio
import json


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

    def __str__(self):
        """Returns the current state of the Move"""
        return f'current state of Request={str(vars(self))}'


class APIClass:
    @classmethod
    async def get_move(cls, url: str, session: aiohttp.ClientSession) -> dict:
        response = await session.request(method='GET', url=url)
        # "Read response’s body as JSON, return dict .json()"
        json_response = await response.json()
        a_move = Moves(
            name=json_response['name'],
            id_=json_response['id'],
            generation=json_response['generation']['name'],
            accuracy=json_response['accuracy'],
            pp=json_response['pp'],
            power=json_response['power'],
            type_=json_response['type']['name'],
            damage_class=json_response['damage_class']['name'],
            effect_short=json_response['effect_entries'][0]['short_effect']

        )

        return a_move

    @classmethod
    async def process_requests(cls, id_list: list):
        url = 'https://pokeapi.co/api/v2/move/{}'
        async with aiohttp.ClientSession() as session:
            list_urls = [url.format(req_id) for req_id in id_list]
            coroutines = [cls.get_move(a_url, session) for a_url in list_urls]
            responses = await asyncio.gather(*coroutines)
            print(responses)
            for res in responses:
                print(res)


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response = loop.run_until_complete(APIClass.process_requests([1, 2]))
    # print(response)
    # print(type(response))


if __name__ == '__main__':
    main()

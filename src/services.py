from aiohttp import ClientSession

from config import Config


class Services:
    def __init__(self):
        pass

    async def get_weather(self, city: str) -> str:
        params = {
            "q": city,
            "appid": Config().api_token,
            "units": "metric",
            "lang": "ru",
        }
        async with ClientSession() as session:
            async with session.get(
                url=Config().api_url,
                params=params
            ) as res:
                if not res.ok:
                    return "Город не найден"

                data = await res.json()
                desc = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                return f"Погода в {city} - {desc}, температура - {round(temp)}°C"

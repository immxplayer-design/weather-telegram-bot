import requests
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "YOUR_BOT_TOKEN"
WEATHER_API_KEY = "YOUR_API_KEY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("weather"))
async def weather(message: Message):
    city = "London"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    data = requests.get(url).json()

    temp = data["main"]["temp"]

    await message.answer(
        f"🌤 Weather in {city}: {temp}°C"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

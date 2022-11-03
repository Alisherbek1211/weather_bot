from aiogram import types,Bot,Dispatcher,executor

from api import obhavo

TOKEN = 'Bot_Token'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Assalomu Alaykum. Ob-Havo bo'timizga xush kelibsiz!")

@dp.message_handler(content_types='text')
async def first_handler(message:types.Message):
    shahar = message.text
    data = obhavo(shahar)
    if data == "Hatolik":
        await message.answer("Ma'lumot topilmadi!")
    else:
        await message.answer(data)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
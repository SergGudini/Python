import logging, requests, re
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6600874372:AAH8XjZlXb5BPCy7P1FM6FqCmBXV8HvhPNw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
# Обработчик команд  /start, /help
    await message.reply("Вычислять выражения! /calc\nСобака /dog")

@dp.message_handler(commands=['calc'])
async def send_calc(message: types.Message):
# Вычисление выражений
    expr = message.text.replace('/calc','')
    result = expr + ' = ' + str(eval(expr))
    await message.answer(result)

@dp.message_handler(commands=['dog'])
async def send_dog(message: types.Message):
    contents = requests.get('https://random.dog/woof.json').json()
    await message.answer(contents)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
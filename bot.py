import json
import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()    # (content_types=['text'])
async def echo_send(message: types.Message):    # start(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
     .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Ненормативная лексика в чате запрещена')
        await message.delete()

executor.start_polling(dp, skip_updates=True)

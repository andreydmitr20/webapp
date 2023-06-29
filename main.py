from aiogram import Bot, Dispatcher, executor, types  # pylint: disable=import-error
from aiogram.types.web_app_info import WebAppInfo  # pylint: disable=import-error
from config import config, l
from lng import lng, set_lng

set_lng('en')

bot = Bot(config.bot_token)
l(config.bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(
        lng('open_web_page'),
        web_app=WebAppInfo(url='https://memenu.me/api/user/test/')
    ))

    await message.answer(
        lng('hi'),
        reply_markup=markup
    )

executor.start_polling(dp)

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6850530350:AAF7DsatVvVwNTLfXx07h2ZWqjOQ6q7BIzE')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://artyommedved.github.io/testpreloader.githib.io/')))
    await message.answer('Привет, мой друг!, Чтобы начать крутить кэйсы, пополни свой счет(/balance), по вопросам команд(/help)', reply_markup=markup)
    
executor.start_polling(dp)


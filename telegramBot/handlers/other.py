from aiogram import types, Dispatcher
from keyboards import kb_other

'*****start bot****'
async def command_start(message : types.Message):
    await message.answer('У що будемо грати?', reply_markup=kb_other)


'*****info****'
async def command_info(message : types.Message):
    await message.answer('Привіт! Я -@ ,творець цього бота. Якщо в вас є якісь побажання до бота прошу пішіть')

'*****start****'
def register_hendlers_other(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'menu'])
    dp.register_message_handler(command_info, commands=['info'])

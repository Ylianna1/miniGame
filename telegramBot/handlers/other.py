from aiogram import types, Dispatcher
from keyboards import kb_otherOne, kb_otherTwo

'*****start bot****'
async def command_start(message : types.Message):
    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()
    if chips>=3:
        await message.answer('У що будемо грати?', reply_markup=kb_otherTwo)
    else:
        await message.answer('У що будемо грати?', reply_markup=kb_otherOne)


'*****info****'
async def command_info(message : types.Message):
    await message.answer('Привіт! Я Юліанна, творець цього бота. Якщо в вас є якісь побажання до бота прошу пішіть')

'*****start****'
def register_hendlers_other(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'menu'])
    dp.register_message_handler(command_info, commands=['info'])

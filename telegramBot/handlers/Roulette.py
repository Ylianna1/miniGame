from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
#from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from create_bot import dp, bot
#import keyboards.other_button
import random
from asyncio import sleep

'***********Кнопки відповідей***************'
rooleteButton = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
Button1 = KeyboardButton(text='Крутити рулетку')
Button2 = KeyboardButton('Ні')
rooleteButton.add(Button1, Button2)

kb_roolet_back = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
Button1 = KeyboardButton('Повернутися')
kb_roolet_back.add(Button1)

@dp.callback_query_handler(text="Y")
async def Yes(Yes: types.CallbackQuery):
    await Yes.message.answer('Кидайте кубик:', reply_markup=rooleteButton)

'***********Game***************'

@dp.message_handler(text=['Крутити рулетку', 'рулетка' , 'Рулетка','крутити рулетку'])
async def coinGame(message : types.Message):
    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()
    if chips>2:
        bot_data=await bot.send_dice(message.chat.id, emoji='🎰') 
        bot_data=bot_data['dice']['value']
        chips=chips-3
        d = open('text_infoGame/points.txt', "w")
        d.write(str(chips))
        d.close()
        await sleep(2)
        if bot_data==64 or bot_data==1 or bot_data==43 or bot_data==22 :
            Victory = random.choice(open("handlers/media/web.txt", 'r', encoding='UTF-8').readlines())
            await message.answer("Вітаю з перемогою!")        
            await sleep(1)
            await message.answer("А ось ваш приз!")   
            await sleep(1)   
            await message.answer(Victory, reply_markup=rooleteButton)
        else:
            await message.answer("Наступного разу пощастить!")
            await message.answer("Спробувати ще?", reply_markup=rooleteButton)
    else:
        await message.answer("Вас недостатньо фішок", reply_markup=kb_roolet_back)
   
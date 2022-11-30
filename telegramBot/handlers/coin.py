from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from create_bot import dp
from asyncio import sleep
from keyboards import kb_other
import random

'***********Кнопки відповідей***************'

buttn_coin = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('Орел')
b2 = KeyboardButton('Решка')
buttn_coin.add(b1,b2)

buttn_continuation = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
backmenu = KeyboardButton('Ні')
continuation = KeyboardButton('Так')
buttn_continuation.add(continuation, backmenu)


@dp.message_handler(text=['Так', 'так'])
async def contin(message : types.Message):
    await message.answer('Орел чи решка?', reply_markup=buttn_coin)

@dp.message_handler(text=['Повернутися','ні', 'Ні','повернутися','Назад','назад'])
async def back(message : types.Message):
    await message.answer('Привіт, давай пограємо!', reply_markup=kb_other)
'***********Game***************'

@dp.message_handler(text=['Орел','Решка'])
async def coinGame(message : types.Message):
    options=['Орел', 'Решка','Ребро']
    ans=(random.choice(options))
    if ans =='Ребро':
        video = open("handlers/media/rebro.mp4", 'rb')
    elif ans =='Решка':
        video = open("handlers/media/reshka.mp4", 'rb')
    elif ans=='Орел':
        video = open("handlers/media/Orel.mp4", 'rb')
    await message.answer_video(video)
    await sleep(7)
    await message.answer(ans)
    if  ans == message.text: 
        await message.answer('🎉🎉🎉Ви вгадали! Бажаєте повторити?🎉🎉🎉', reply_markup=buttn_continuation)
    else :
        await message.answer('Нажаль Ви не вгадали.😢 Бажаєте повторити?', reply_markup=buttn_continuation)
    
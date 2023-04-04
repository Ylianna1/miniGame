from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from create_bot import dp
from asyncio import sleep
from keyboards import kb_otherTwo, kb_otherOne
import random


d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
chips = int(d.read())
d.close()

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
    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()
    if chips>=3:
        await message.answer('У що будемо грати?', reply_markup=kb_otherTwo)
    else:
        await message.answer('У що будемо грати?', reply_markup=kb_otherOne)
'***********Game***************'

@dp.message_handler(text=['Орел','Решка'])
async def coinGame(message : types.Message):

    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()

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
        chips+=1
        await message.answer('🎉🎉🎉Ви вгадали!🎉🎉🎉')
        await sleep(1)
        await message.answer(f'Кількість ваших фішок: {chips}🎫')
        await sleep(1)
        await message.answer('Бажаєте повторити?', reply_markup=buttn_continuation)
    else :
        chips=chips
        await message.answer('Нажаль Ви не вгадали.😢')
        await sleep(1)
        await message.answer(f'Кількість ваших фішок: {chips}🎫')
        await sleep(1)
        await message.answer('Бажаєте повторити?', reply_markup=buttn_continuation)

    d = open('text_infoGame/points.txt', "w")
    d.write(str(chips))
    d.close()
    
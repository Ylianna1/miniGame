from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from create_bot import dp
from asyncio import sleep
import random

'***********Кнопки відповідей***************'

cuefa = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('✊')
b2 = KeyboardButton('🖐')
b3 = KeyboardButton('✌️')
b4 = KeyboardButton('👌')
cuefa.add(b1, b2, b3, b4) #cuefa(цуефа) інша назва гри

buttn_continuation = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
backmenu = KeyboardButton('Повернутися')
continuation = KeyboardButton('Повторити')
buttn_continuation.add(continuation, backmenu)

@dp.message_handler(text=['Повторити','повторити'])
async def contin(message : types.Message):
    await message.answer('Камінь, ножниці, папір!!!', reply_markup=cuefa)

'***********Game***************'
points=0
point=0
i=0
b=['✊','🖐','✌️','👌']

@dp.message_handler(text=b)
async def StoneGame(message : types.Message):

    global points
    global point
    global i
    
    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()

    if i < 3:
        i+=1
        ans=(random.choice(b))
        await message.answer(ans)
        if  ans == message.text:
            await message.answer('Ничия')
        elif message.text =="Камінь" or message.text == "камінь" or message.text == "✊":
            if ans == "✌️":
                points+=1
                await message.answer("Ви отримуєте бал")
            else:
                point+=1
                await message.answer("Бал мій")
        elif message.text == "Папір" or message.text == "папір" or message.text == "🖐":
            if ans == "✊" or ans == '👌':
                points+=1
                await message.answer("Ви отримуєте бал")
            else:
                point+=1
                await message.answer("Бал мій")
        elif message.text == "Колодязь" or message.text == "колодязь" or message.text == "👌":
            if ans == "✊" or ans == '✌️':
                points+=1
                await message.answer("Ви отримуєте бал")
            else:
                point+=1
                await message.answer("Бал мій")
        elif message.text == "Ножеці" or message.text == "ножеці" or message.text == "✌️":
            if ans == "🖐":
                points+=1
                await message.answer("Ви отримуєте бал")
            else:
                point+=1
                await message.answer("Бал мій")
    else:
        i=0
        if points >= 2:
            await message.answer('Вітаю, Ви перемогли!!!')
            await message.answer('🎉')
            chips+=2
        elif points == point:
            await message.answer('У нас нічия')
            await message.answer('👏')
            chips+=1
        else:
            await message.answer('Бу-га-га-га.Це моя перемога!!!')
            await message.answer('😈')
            chips=chips
        await sleep(1)
        await message.answer(f'Ви набрали {points} бали')
        await sleep(1)
        await message.answer(f'Кількість ваших фішок: {chips}🎫')
        await message.answer('Бажаєте повторити?', reply_markup=buttn_continuation)
        points=0
        point=0
        
        d = open('text_infoGame/points.txt', "w")
        d.write(str(chips))
        d.close()
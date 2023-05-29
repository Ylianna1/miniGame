from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from create_bot import dp, bot
from asyncio import sleep

'***********Кнопки відповідей***************'
bowlingButton = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
Button1 = KeyboardButton(text='🎱')
bowlingButton.add(Button1)

kb_bowling = InlineKeyboardMarkup(row_width=1)
Button1 = InlineKeyboardButton(text='Так', callback_data='++')
Button2 = InlineKeyboardButton(text='Нi', callback_data='No')
kb_bowling.add(Button1, Button2)

@dp.callback_query_handler(text="++")
async def Yes(Yes: types.CallbackQuery):
    await Yes.message.answer('Запускайте шар:', reply_markup=bowlingButton)

'***********Game***************'
frames=0
points_bowling=0

@dp.message_handler(text=['🎱', 'Боулінг', 'боулінг', 'шар', 'Шар', 'Запустити шар', 'запустити шар'])
async def coinGame(message : types.Message):
    global frames
    global points_bowling
    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()
    if frames<4:
        bot_data =await bot.send_dice(message.chat.id, emoji='🎳')
        bot_data=bot_data['dice']['value']   
        if bot_data<3:
            bot_data=bot_data-1
            await sleep(3)
            await message.answer(f'Кількість збитих кегель:  {bot_data}',  reply_markup=bowlingButton)
        elif bot_data==6:
            await sleep(3)
            await message.answer('Strike',  reply_markup=bowlingButton)
        else:
            await sleep(3)
            await message.answer(f'Кількість збитих кегель:  {bot_data}',  reply_markup=bowlingButton)
        points_bowling+=bot_data             
        frames+=1
    else:
        bot_data =await bot.send_dice(message.chat.id, emoji='🎳')
        bot_data=bot_data['dice']['value']
        if bot_data<3:
            bot_data=bot_data-1
            await sleep(3)
            await message.answer(f'Кількість збитих кегель:  {bot_data}')
        elif bot_data==6:
            await sleep(3)
            await message.answer('Strike')
        else:
            await sleep(3)
            await message.answer(f'Кількість збитих кегель:  {bot_data}')
        points_bowling+=bot_data           
        await sleep(1)
        await message.answer(f'Кількість очків: {points_bowling}')
        if points_bowling>15:
            chips=chips+3
        elif points_bowling==30:
            chips=chips+9
        elif points_bowling==0:
            chips=chips
        elif points_bowling<=15:
            chips=chips+1
        else:  
            chips=chips+1    
        await sleep(1)
        frames=0        
        await message.answer(f'Кількість ваших фішок: {chips}🎫')
        d = open('text_infoGame/points.txt', "w")
        d.write(str(chips))
        d.close()
        await sleep(1)
        await message.answer('Почати спочатку?', reply_markup=kb_bowling)




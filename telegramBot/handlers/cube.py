from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from create_bot import dp, bot
from asyncio import sleep

'***********Кнопки відповідей***************'
cubeButton = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
Button1 = KeyboardButton(text='🎲🎲')
cubeButton.add(Button1)

kb_cube = InlineKeyboardMarkup(row_width=1)
Button1 = InlineKeyboardButton(text='Так', callback_data='Y')
Button2 = InlineKeyboardButton(text='Нi', callback_data='No')
kb_cube.add(Button1, Button2)

@dp.callback_query_handler(text="Y")
async def Yes(Yes: types.CallbackQuery):
    await Yes.message.answer('Кидайте кубик:', reply_markup=cubeButton)

'***********Game***************'

@dp.message_handler(text=['🎲🎲','Куб','куб'])
async def coinGame(message : types.Message):
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)

    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await message.answer("Ви програли!")
        await message.answer('Бажаєте повторити?', reply_markup=kb_cube)
    elif bot_data < user_data:
        await message.answer("Ви перемогли!")
        await message.answer('Бажаєте повторити?', reply_markup=kb_cube)
    else:
        await message.answer("Ничия!")
        await message.answer('Бажаєте повторити?', reply_markup=kb_cube)
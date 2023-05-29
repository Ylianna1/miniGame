from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from create_bot import dp 
import handlers.coin, handlers.StonePaper, handlers.trueFalse, handlers.cube, handlers.bowling, handlers.Roulette

# ---------------Кнопки списку ігор---------------
kb_otherOne = InlineKeyboardMarkup(row_width=1)
kb_otherTwo = InlineKeyboardMarkup(row_width=1)
gameButton1 = InlineKeyboardButton(text='Орел чи решка?', callback_data='gameButton1')
gameButton2 = InlineKeyboardButton(text='Правда чи брехня?', callback_data='gameButton2')
gameButton3 = InlineKeyboardButton(text='Кубик', callback_data='gameButton3')
gameButton4 = InlineKeyboardButton(text='Камінь, ножиці, папір', callback_data='gameButton4')
gameButton5 = InlineKeyboardButton(text='Боулінг', callback_data='gameButton5')
gameButton7 = InlineKeyboardButton(text='Рулетка', callback_data='gameButton7')

kb_otherOne.add(gameButton1, gameButton2, gameButton3, gameButton4, gameButton5)
kb_otherTwo.add(gameButton1, gameButton2, gameButton3, gameButton4, gameButton5, gameButton7)

# ---------------Кнопки списку опцій---------------

Button3 = InlineKeyboardButton(text='Повернутися', callback_data='back')

kb_function_coin_call = InlineKeyboardMarkup(row_width=2)
start_coin = InlineKeyboardButton(text='Почати гру', callback_data='start_coin')
info_coin = InlineKeyboardButton(text='Правила', callback_data='info_coin')
kb_function_coin_call.add(start_coin, info_coin, Button3)

kb_function_trueFalse_call = InlineKeyboardMarkup(row_width=2)
start_trueFalse = InlineKeyboardButton(text='Почати гру', callback_data='start_trueFalse')
info_trueFalse = InlineKeyboardButton(text='Правила', callback_data='info_trueFalse')
kb_function_trueFalse_call.add(start_trueFalse, info_trueFalse, Button3)

kb_function_Stone_call = InlineKeyboardMarkup(row_width=2)
start_Stone = InlineKeyboardButton(text='Почати гру', callback_data='start_Stone')
info_Stone = InlineKeyboardButton(text='Правила', callback_data='info_Stone')
kb_function_Stone_call.add(start_Stone, info_Stone, Button3)

kb_function_emoji_call = InlineKeyboardMarkup(row_width=2)
start_emoji = InlineKeyboardButton(text='Почати гру', callback_data='start_emoji')
info_emoji = InlineKeyboardButton(text='Правила', callback_data='info_emoji')
kb_function_emoji_call.add(start_emoji, info_emoji, Button3)

kb_function_bowling_call = InlineKeyboardMarkup(row_width=2)
start_bowling = InlineKeyboardButton(text='Почати гру', callback_data='start_bowling')
info_bowling = InlineKeyboardButton(text='Правила', callback_data='info_bowling')
kb_function_bowling_call.add(start_bowling, info_bowling, Button3)

kb_function_roulette_call = InlineKeyboardMarkup(row_width=2)
start_roulette = InlineKeyboardButton(text='Почати гру', callback_data='start_roulette')
info_roulette = InlineKeyboardButton(text='Правила', callback_data='info_roulette')
kb_function_roulette_call.add(start_roulette, info_roulette, Button3)

kb_function_back = InlineKeyboardMarkup(row_width=2)
kb_function_back.add( Button3)


# ---------------Функції---------------

@dp.callback_query_handler(text="gameButton1")
async def coin_call(coin_call: types.CallbackQuery):
    await coin_call.message.delete()
    await coin_call.message.answer("Гра 'Орел чи решка?'", reply_markup=kb_function_coin_call)

@dp.callback_query_handler(text="gameButton2")
async def trueFalse_call(trueFalse_call: types.CallbackQuery):
    await trueFalse_call.message.delete()
    await trueFalse_call.message.answer("Гра 'Правда чи брехня?'", reply_markup=kb_function_trueFalse_call)

@dp.callback_query_handler(text="gameButton3")
async def emoji_call(emoji_call: types.CallbackQuery):
    await emoji_call.message.delete()
    await emoji_call.message.answer("Гра 'Кубик'", reply_markup=kb_function_emoji_call)

@dp.callback_query_handler(text="gameButton4")
async def Stone_call(Stone_call: types.CallbackQuery):
    await Stone_call.message.delete()
    await Stone_call.message.answer("Гра 'Камінь, ножиці, папір'", reply_markup=kb_function_Stone_call)

@dp.callback_query_handler(text="gameButton5")
async def bowling_call(bowling_call: types.CallbackQuery):
    await bowling_call.message.delete()
    await bowling_call.message.answer("Гра 'Боулінг'", reply_markup=kb_function_bowling_call)

@dp.callback_query_handler(text="gameButton7")
async def roulette_call(roulette_call: types.CallbackQuery):
    await roulette_call.message.delete()
    await roulette_call.message.answer("Гра 'Рулетка'", reply_markup=kb_function_roulette_call)


# ---------------Функції початку ---------------

@dp.callback_query_handler(text="start_coin")
async def coin_call(coin_call: types.CallbackQuery):
    await coin_call.message.delete()
    await coin_call.message.answer('Орел чи решка?', reply_markup=handlers.coin.buttn_coin)

@dp.callback_query_handler(text="start_trueFalse")
async def trueFalse_call(trueFalse_call: types.CallbackQuery):
    await trueFalse_call.message.delete()
    await trueFalse_call.message.answer('Готові?', reply_markup=handlers.trueFalse.kb_answers)

@dp.callback_query_handler(text="start_Stone")
async def Stone_call(Stone_call: types.CallbackQuery):
    await Stone_call.message.delete()
    await Stone_call.message.answer('Камінь, ножниці, папір!!!', reply_markup=handlers.StonePaper.cuefa)

@dp.callback_query_handler(text="start_emoji")
async def emoji_call(emoji_call: types.CallbackQuery):
    await emoji_call.message.delete()
    await emoji_call.message.answer('Кидайте кубик:', reply_markup=handlers.cube.cubeButton)

@dp.callback_query_handler(text="start_bowling")
async def bowling_call(bowling_call: types.CallbackQuery):
    await bowling_call.message.delete()
    await bowling_call.message.answer('Кидайте шар', reply_markup=handlers.bowling.bowlingButton)

@dp.callback_query_handler(text="start_roulette")
async def roulette_call(roulette_call: types.CallbackQuery):
    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()
    await roulette_call.message.delete()
    await roulette_call.message.answer(f'Кількість ваших фішок: {chips}🎫')
    await roulette_call.message.answer('Запуск стоїть 3🎫 фішки. Запустити?', reply_markup=handlers.Roulette.rooleteButton)



# ---------------Функції правил---------------

@dp.callback_query_handler(text="info_coin")
async def info_call(info_call: types.CallbackQuery):
    f = open('text_infoGame/coin.txt', 'r', encoding='UTF-8')
    infoGame = f.read()
    f.close()
    await info_call.message.delete()
    await info_call.message.answer(infoGame,  reply_markup=kb_function_back)

@dp.callback_query_handler(text="info_trueFalse")
async def info_call(info_call: types.CallbackQuery):
    f = open('text_infoGame/TrueFalse.txt', 'r', encoding='UTF-8')
    infoGame = f.read()
    f.close()
    await info_call.message.delete()
    await info_call.message.answer(infoGame,  reply_markup=kb_function_back)

@dp.callback_query_handler(text="info_Stone")
async def info_call(info_call: types.CallbackQuery):
    f = open('text_infoGame/StonePaper.txt', 'r', encoding='UTF-8')
    infoGame = f.read()
    f.close()
    await info_call.message.delete()
    await info_call.message.answer(infoGame,  reply_markup=kb_function_back)

@dp.callback_query_handler(text="info_emoji")
async def info_call(info_call: types.CallbackQuery):
    f = open('text_infoGame/cube.txt', 'r', encoding='UTF-8')
    infoGame = f.read()
    f.close()
    await info_call.message.delete()
    await info_call.message.answer(infoGame,  reply_markup=kb_function_back)

@dp.callback_query_handler(text="info_bowling")
async def info_call(info_call: types.CallbackQuery):
    f = open('text_infoGame/bowling.txt', 'r', encoding='UTF-8')
    infoGame = f.read()
    f.close()
    await info_call.message.delete()
    await info_call.message.answer(infoGame,  reply_markup=kb_function_back)

@dp.callback_query_handler(text="info_roulette")
async def info_call(info_call: types.CallbackQuery):
    f = open('text_infoGame/Roulette.txt', 'r', encoding='UTF-8')
    infoGame = f.read()
    f.close()
    await info_call.message.delete()
    await info_call.message.answer(infoGame,  reply_markup=kb_function_back)

# ---------------Функція поверненя---------------

@dp.callback_query_handler(text="back")
async def back_call(back_call: types.CallbackQuery):
    await back_call.message.delete()
    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()
    if chips>=3:
        await back_call.message.answer('Привіт, давай пограємо!', reply_markup=kb_otherTwo)
    else:
        await back_call.message.answer('Привіт, давай пограємо!', reply_markup=kb_otherOne)

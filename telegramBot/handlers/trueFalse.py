from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from create_bot import dp
import keyboards.other_button
import random
from asyncio import sleep


'***********Кнопки відповідей***************'

kb_answers = InlineKeyboardMarkup(row_width=1)
Button1 = InlineKeyboardButton(text='Так', callback_data='Yes')
Button2 = InlineKeyboardButton(text='Нi', callback_data='No')
kb_answers.add(Button1, Button2)

ButtonOptions = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('Правда')
b2 = KeyboardButton('Брехня')
ButtonOptions.add(b1,b2)


'***********гра***************'

points=0
g=0


def check():
    opt=[1, 2]
    answers=(random.choice(opt))
    return answers

b=check()

@dp.message_handler(text=['Правда','Брехня'])
async def StoneGame(message : types.Message):

    global points
    global g
    global b

    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()

    if b == 2:
        await sleep(0.5)
        if message.text =='Правда':
            await message.answer("Правильно")
            points+=1
        else:
            await message.answer("Не правильно")
    else:       
        await sleep(0.5)
        if message.text =='Брехня':
            await message.answer("Правильно")
            points+=1
        else:
            await message.answer("Не правильно")
    if g != 5:
        await sleep(0.5)
        g=g+1
        b=check()
        if b == 1:
            Fact = random.choice(open("handlers/question/FalseAnswers.txt", 'r', encoding='UTF-8').readlines())
            await message.answer(Fact, reply_markup=ButtonOptions)
        else:
            Fact = random.choice(open("handlers/question/TrueAnswers.txt", 'r', encoding='UTF-8').readlines())
            await message.answer(Fact, reply_markup=ButtonOptions)
    else:
        g=0
        if points < 3:
            chips=chips
            await message.answer('Не здавайтесь! ')           
        elif points == 6:
            chips+=12
            await message.answer('Ви молодець! Вірно відповіли на всі відповіді')           
        else:
            chips+=6
            await message.answer('Чудова робота! Ви відповіли на більшість відповідей правильно.')
        await sleep(1)
        await message.answer(f'Кількість ваших фішок: {chips}🎫')
        await sleep(1)
        await message.answer('Хочите повторити?', reply_markup=kb_answers)

        d = open('text_infoGame/points.txt', "w")
        d.write(str(chips))
        d.close()


@dp.callback_query_handler(text="Yes")
async def StoneGame(StoneGame: types.CallbackQuery):
    global b
    if b == 1:
        Fact = random.choice(open("handlers/question/FalseAnswers.txt", 'r', encoding='UTF-8').readlines())
        await StoneGame.message.answer(Fact, reply_markup=ButtonOptions)
    else:
        Fact = random.choice(open("handlers/question/TrueAnswers.txt", 'r', encoding='UTF-8').readlines())
        await StoneGame.message.answer(Fact, reply_markup=ButtonOptions)


@dp.callback_query_handler(text="No")
async def End(End: types.CallbackQuery):
    d = open('text_infoGame/points.txt', 'r', encoding='UTF-8')
    chips = int(d.read())
    d.close()
    if chips>=3:
        await End.message.answer('Привіт, давай пограємо!', reply_markup=keyboards.other_button.kb_otherTwo)
    else:
        await End.message.answer('Привіт, давай пограємо!', reply_markup=keyboards.other_button.kb_otherOne)
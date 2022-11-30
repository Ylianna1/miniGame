from aiogram.utils import executor
from aiogram import types
from create_bot import dp 
from handlers import other

async def on_startup(_):
    print('Bot onlain')

other.register_hendlers_other(dp)

# '*****spiking****'
@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привіт':
        await message.answer('Привіт і тобі')
    else :
        await message.answer('Цей бот вас не розуміє')

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

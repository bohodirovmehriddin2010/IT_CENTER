from aiogram.types import Message
from aiogram.dispatcher import FSMContext


from loader import dp,bot
from utils.env import ADMIN_ID
from utils import texts, buttons
from utils.states import aplication
from asyncio import create_task


@dp.message_handler(content_types=('text'), state=aplication.name)
async def passenger_handler(message: Message, state: FSMContext):
    name = message.text
    
    
    await state.update_data({
        'name': name
    })
    
    await message.answer(texts.phone, reply_markup=buttons.PHONE)
    
    await aplication.phone.set()
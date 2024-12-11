from aiogram.types import Message
from aiogram.dispatcher import FSMContext


from loader import dp,bot
from utils.env import ADMIN_ID
from utils import texts
from utils.states import aplication
from asyncio import create_task


async def aplication_handler_task(message: Message, state: FSMContext):

    phone = message.contact.phone_number

    await state.update_data({
        'phone':phone
    })
    
    await message.answer(texts.age)
   
    
    await aplication.age.set()


@dp.message_handler(content_types=('contact', 'text'), state=aplication.phone)
async def passenger_handler(message: Message, state: FSMContext):
    await create_task(aplication_handler_task(message, state))
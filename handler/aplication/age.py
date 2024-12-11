from aiogram.types import Message
from aiogram.dispatcher import FSMContext


from loader import dp
from utils import texts, buttons
from utils.states import aplication
from .handler import aplication

from asyncio import create_task



async def application_handler_task(message: Message, state: FSMContext):
    
    age = message.text
    
    
    await state.update_data({
        'age': age
    })
    
    await message.answer(texts.kurslar, reply_markup=buttons.COUNT)
    
    await aplication.course.set()
    
    
    
@dp.message_handler(content_types=['text'], state=aplication.age)
async def passenger_handler(message: Message, state: FSMContext):
    await create_task(application_handler_task(message, state))
from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp
from utils import texts, buttons
from utils.states import aplication
from asyncio import create_task

async def aplication_handler_task(message: Message, state: FSMContext):

    course = message.text
    await state.update_data({
        'course': course
    })

    await message.answer(texts.field, reply_markup=buttons.SEND_GROUP)

    await aplication.check.set()


@dp.message_handler(content_types=['text'], state=aplication.course)
async def passenger_handler(message: Message, state: FSMContext):
    if message.text in [buttons.CANCEL]:
        await message.answer(texts.kurslar, reply_markup=buttons.COUNT)
        await aplication.check.set()
    else:
        await create_task(aplication_handler_task(message,state))
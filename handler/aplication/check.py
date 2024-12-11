from aiogram. types import Message
from aiogram.dispatcher import FSMContext


from loader import dp, bot
from utils import buttons, texts
from utils.env import GROUP_ID
from.handler import aplication
from asyncio import create_task






async def check_handler_task(message: Message, state: FSMContext):
    
    data = await state.get_data()
    name = data.get('name')
    age = data.get('age')
    phone = data.get('phone')
    course = data.get('course')
    
    await bot.send_message(
    chat_id=GROUP_ID,
    text=texts.check(
        name=name,
        age=age,
        phone=phone,
        course=course
    )
    )


    await message.answer('Arizangiz ADMINga yuborildi!')


    
@dp.message_handler(lambda message: message.text.startswith(buttons.CHECK), state=aplication.check)
async def passenger_handler(message: Message, state: FSMContext):
    if message.text in [buttons.BASE_BACK]:
        await message.answer(texts.START, reply_markup=buttons.ARIZA)
        await aplication.course.set()
    else:
        await create_task(check_handler_task(message,state))
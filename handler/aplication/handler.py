from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp
from utils import texts, buttons
from utils.states import aplication

@dp.message_handler(lambda message: message.text.startswith(buttons.ARIZA), state="*")
async def check_handler(message: Message, state: FSMContext):
    
    await message.answer(texts.name, reply_markup=buttons.NAME)
    await aplication.name.set()


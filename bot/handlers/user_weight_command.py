import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from bot.FSM.states import FSMAddWeightRecord
from bot.db import add_weight

logger = logging.getLogger(__name__)

# creating router`s onject
user_weight_router = Router(name="user weight router")


#TODO: change weight from int to float
# command for record current weight to db
@user_weight_router.message(Command("weight"), StateFilter(default_state))
async def cmd_weight(message: Message, state: FSMContext, admin_id):
    logger.info("Enter /weight command")
    
    await message.answer("Напишите, пожалуйста, ваш текущий вес в кг")
    # setup state to waiting for weight data
    await state.set_state(FSMAddWeightRecord.fill_weight)
    
    logger.info("Exit /weight command")
    

#TODO: add possibility to check weight before commit to db
# handler if weight was sent correct
@user_weight_router.message(
    StateFilter(FSMAddWeightRecord.fill_weight),
    F.text.isdigit()
)
async def process_weight_sent(
    message: Message,
    state: FSMContext,
    session: AsyncSession
):
    # store weight into storage
    await state.update_data(weight=int(message.text))  # type:ignore

    context_data = await state.get_data()
    weight = int(context_data.get("weight"))  # type:ignore

    # add weight to db
    await add_weight(
        session=session,
        telegram_id=message.from_user.id,  # type:ignore
        weight=weight,
    )
    # stop FSM
    await state.clear()
    # send message abour success
    await message.answer(f"Ваш текущий вес {weight} кг был сохранен")


# handler if weight was sent not correct
@user_weight_router.message(StateFilter(FSMAddWeightRecord.fill_weight))
async def warning_not_weight(message: Message):
    await message.answer("Отправьте, пожалуйста, целое число")

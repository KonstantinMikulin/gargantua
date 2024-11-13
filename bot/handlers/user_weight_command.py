import logging

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from bot.FSM.states import FSMAddWeightRecord

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
    
    

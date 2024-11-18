import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from bot.FSM import FSMAddMeasurmentRecord
from bot.db import add_chest, add_waist, add_hips
from bot.keyboards import cancel_keyboard

logger = logging.getLogger(__name__)

# creating router`s onject
user_measure_router = Router(name="user measurements router")


# command /measure
@user_measure_router.message(Command("measure"),StateFilter(default_state))
async def cmd_measure(message: Message, state: FSMContext):
    await message.answer(
        text="Отправьте обхват груди",
        reply_markup=cancel_keyboard    
    )
    # setup state to waiting for waist measurements data
    await state.set_state(FSMAddMeasurmentRecord.fill_chest)


# handler if chest`s data was sent correct
@user_measure_router.message(
    StateFilter(FSMAddMeasurmentRecord.fill_chest),
    F.text.isdigit()
)
async def process_chest_sent(
    message: Message,
    state: FSMContext,
    session: AsyncSession
):
    # store chest in storage
    await state.update_data(chest=message.text)  # type:ignore

    # set next state
    await state.set_state(FSMAddMeasurmentRecord.fill_waist)

    # send message
    await message.answer(
        text=f"Обхват груди {message.text} см сохранен, {message.from_user.first_name}!\n\n"  # type:ignore
             f"Отправьте обхват талии",
        reply_markup=cancel_keyboard
    )


# handler if waist`s data was sent correct
@user_measure_router.message(
    StateFilter(FSMAddMeasurmentRecord.fill_waist),
    F.text.isdigit()
)
async def process_waist_sent(
    message: Message,
    state: FSMContext,
    session: AsyncSession
):
    # store waist in storage
    await state.update_data(waist=message.text)  # type:ignore

    # set next state
    await state.set_state(FSMAddMeasurmentRecord.fill_hips)

    # send message
    await message.answer(
        text=f"Обхват талии {message.text} был сохранен\n\n"
        f"Отправьте обхват бедер",
        reply_markup=cancel_keyboard
    )


# handler if hips` data was sent correct
@user_measure_router.message(
    StateFilter(FSMAddMeasurmentRecord.fill_hips), F.text.isdigit()
)
async def process_hips_sent(
    message: Message,
    state: FSMContext,
    session: AsyncSession
):
    # store hips in storage
    await state.update_data(hips=message.text)  # type:ignore

    # send message
    await message.answer(
        f"Обхват бедер {message.text} был сохранен\n\n"
        f"Спасибо!"
    )
    
    # get data from storage
    context_data = await state.get_data()
    chest = int(context_data.get("chest"))  # type:ignore
    waist = int(context_data.get("waist"))  # type:ignore
    hips = int(context_data.get("hips"))  # type:ignore

    # add all records to db
    await add_chest(
        session=session,
        telegram_id=message.from_user.id,  # type:ignore
        chest=chest,
    )
    
    await add_waist(
        session=session,
        telegram_id=message.from_user.id,  # type:ignore
        waist=waist,
    )

    await add_hips(
        session=session,
        telegram_id=message.from_user.id,  # type:ignore
        hips=hips,
    )

    # stop FSM
    await state.clear()


# handler if data of waist, hips or chest was sent not correct
@user_measure_router.message(
    StateFilter(
        FSMAddMeasurmentRecord.fill_chest,
        FSMAddMeasurmentRecord.fill_waist,
        FSMAddMeasurmentRecord.fill_hips,
    )
)
async def warning_not_correct_mesurment(message: Message):
    await message.answer(
        text="Отправьте правильные данные, пожалуйста",
        reply_markup=cancel_keyboard
    )

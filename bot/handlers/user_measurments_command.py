from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode, ShowMode

from bot.dialogs import AddMeasurmentsSG

# creating router`s onject
user_measure_router = Router(name="user measurements router")


#TODO: add validation message before inserting into db
#TODO: add 'skip' button
# command /measure
@user_measure_router.message(Command("measure"))
async def cmd_measure(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        state=AddMeasurmentsSG.add_chest,
        mode=StartMode.NORMAL,
        show_mode=ShowMode.AUTO,
    )


# # handler if chest`s data was sent correct
# @user_measure_router.message(
#     StateFilter(FSMAddMeasurmentRecord.fill_chest),
#     F.text.isdigit()
# )
# async def process_chest_sent(
#     message: Message,
#     state: FSMContext,
#     session: AsyncSession
# ):
#     # store chest in storage
#     await state.update_data(chest=message.text)  # type:ignore

#     # set next state
#     await state.set_state(FSMAddMeasurmentRecord.fill_waist)

#     # send message
#     await message.answer(
#         text=f"Обхват груди {message.text} см сохранен, {message.from_user.first_name}!\n\n"  # type:ignore
#              f"Отправьте обхват талии",
#         reply_markup=cancel_keyboard
#     )


# # handler if waist`s data was sent correct
# @user_measure_router.message(
#     StateFilter(FSMAddMeasurmentRecord.fill_waist),
#     F.text.isdigit()
# )
# async def process_waist_sent(
#     message: Message,
#     state: FSMContext,
#     session: AsyncSession
# ):
#     # store waist in storage
#     await state.update_data(waist=message.text)  # type:ignore

#     # set next state
#     await state.set_state(FSMAddMeasurmentRecord.fill_hips)

#     # send message
#     await message.answer(
#         text=f"Обхват талии {message.text} был сохранен\n\n"
#         f"Отправьте обхват бедер",
#         reply_markup=cancel_keyboard
#     )


# # handler if hips` data was sent correct
# @user_measure_router.message(
#     StateFilter(FSMAddMeasurmentRecord.fill_hips), F.text.isdigit()
# )
# async def process_hips_sent(
#     message: Message,
#     state: FSMContext,
#     session: AsyncSession
# ):
#     # store hips in storage
#     await state.update_data(hips=message.text)  # type:ignore

#     # send message
#     await message.answer(
#         f"Обхват бедер {message.text} был сохранен\n\n"
#         f"Спасибо!"
#     )
    
#     # get data from storage
#     context_data = await state.get_data()
#     chest = int(context_data.get("chest"))  # type:ignore
#     waist = int(context_data.get("waist"))  # type:ignore
#     hips = int(context_data.get("hips"))  # type:ignore

#     # add all records to db
#     await add_chest(
#         session=session,
#         telegram_id=message.from_user.id,  # type:ignore
#         chest=chest,
#     )
    
#     await add_waist(
#         session=session,
#         telegram_id=message.from_user.id,  # type:ignore
#         waist=waist,
#     )

#     await add_hips(
#         session=session,
#         telegram_id=message.from_user.id,  # type:ignore
#         hips=hips,
#     )

#     # stop FSM
#     await state.clear()


# # handler if data of waist, hips or chest was sent not correct
# @user_measure_router.message(
#     StateFilter(
#         FSMAddMeasurmentRecord.fill_chest,
#         FSMAddMeasurmentRecord.fill_waist,
#         FSMAddMeasurmentRecord.fill_hips,
#     )
# )
# async def warning_not_correct_mesurment(message: Message):
#     await message.answer(
#         text="Отправьте правильные данные, пожалуйста",
#         reply_markup=cancel_keyboard
#     )

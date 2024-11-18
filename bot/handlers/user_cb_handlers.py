from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

user_callback_router = Router(name="user callback router")


# handler for callback_data of cancel record
@user_callback_router.callback_query(F.data == "cancel_record")
async def process_cancel_record_btn(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text( # type: ignore
        text="Внесение данных отменено"
    )
    await state.clear()

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel_btn = InlineKeyboardButton(
    text="Отменить",
    callback_data="cancel_record"
)

cancel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[cancel_btn]]
)

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, ShowMode

from bot.dialogs import AddWeightSG

# creating router`s onject
user_weight_router = Router(name="user weight router")


# command for record current weight to db
@user_weight_router.message(Command("weight"))
async def cmd_weight(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        state=AddWeightSG.add_weight,
        show_mode=ShowMode.DELETE_AND_SEND,
    )

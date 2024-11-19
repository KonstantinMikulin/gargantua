from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode, ShowMode

from bot.dialogs import AddWeightSG

# creating router`s onject
user_weight_router = Router(name="user weight router")


# TODO: add validation message before inserting into db
# TODO: add 'skip' button
# command for record current weight to db
@user_weight_router.message(Command("weight"))
async def cmd_weight(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        state=AddWeightSG.add_weight,
        mode=StartMode.NORMAL,
        show_mode=ShowMode.AUTO,
    )

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode, ShowMode

from bot.dialogs import AddMeasurmentsSG

# creating router`s onject
user_measure_router = Router(name="user measurements router")


# TODO: add 'skip' button
# TODO: let user possibility to choose which measurments to save
# command /measure
@user_measure_router.message(Command("measure"))
async def cmd_measure(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        state=AddMeasurmentsSG.add_chest,
        mode=StartMode.NORMAL,
        show_mode=ShowMode.AUTO,
    )

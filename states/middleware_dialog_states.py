from aiogram.fsm.state import State, StatesGroup

# draft states group for commands validation middleware
# TODO: add nessesary States
class CommandsValidationSG(StatesGroup):
    start_dialog = State()

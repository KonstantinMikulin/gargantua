from aiogram.fsm.state import State, StatesGroup


# states group for getting records
class GetLastRecordsSG(StatesGroup):
    choose = State()
    get_weight = State()
    get_chest = State()
    get_waist = State()
    get_hips = State()

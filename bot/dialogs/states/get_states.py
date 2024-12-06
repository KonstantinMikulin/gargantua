from aiogram.fsm.state import State, StatesGroup


# states group to get one last record
class GetLastRecordsSG(StatesGroup):
    choose = State()
    get_weight = State()
    get_chest = State()
    get_waist = State()
    get_hips = State()


# states group to get all records
class GetAllRecordsSG(StatesGroup):
    choose = State()
    get_all_weight = State()
    get_all_chest = State()
    get_all_waist = State()
    get_all_hips = State()

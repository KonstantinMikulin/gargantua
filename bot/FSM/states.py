from aiogram.fsm.state import State, StatesGroup


class FSMAddWeightRecord(StatesGroup):
    fill_weight = State()


class FSMAddMeasurmentRecord(StatesGroup):
    fill_chest = State()
    fill_waist = State()
    fill_hips = State()

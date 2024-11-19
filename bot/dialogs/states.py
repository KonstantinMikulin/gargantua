from aiogram.fsm.state import State, StatesGroup


# state group for recording weight
class AddWeightSG(StatesGroup):
    add_weight = State()


# state group for recording measurments
class AddMeasurmentsSG(StatesGroup):
    add_chest = State()
    add_waist = State()
    add_hips = State()

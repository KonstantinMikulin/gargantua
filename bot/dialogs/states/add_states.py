from aiogram.fsm.state import State, StatesGroup


# state group for recording weight
class AddWeightSG(StatesGroup):
    add_weight = State()
    check_weight = State()
    weight_progress = State()


# state group for recording measurments
class AddMeasurmentsSG(StatesGroup):
    add_chest = State()
    add_waist = State()
    add_hips = State()
    change_chest = State()
    change_waist = State()
    change_hips = State()
    check_measure = State()
    change_measure = State()
    measurements_progress = State()

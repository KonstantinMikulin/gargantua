from aiogram.fsm.state import State, StatesGroup


# draft state group for creating user account
class FillAccountSG(StatesGroup):
    fill_name = State()
    fill_gender = State()
    fill_birthdate = State()
    fill_current_weight = State()
    send_photo = State()
    fill_done = State()
   
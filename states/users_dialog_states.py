from aiogram.fsm.state import State, StatesGroup


# draft state group for testing default dialog
class DefaultSG(StatesGroup):
    default_dialog = State()


# draft state group for testing starting dialogs
# TODO: add nessesary States
class StartSG(StatesGroup):
    start_dialog = State()


# draft state group for creating user profile
class FillprofileSG(StatesGroup):
    fill_name = State()
    fill_gender = State()
    fill_birthdate = State()
    fill_init_weight = State()
    send_photo = State()
    save_photo = State()
    show_profile = State()
    change_profile = State()
    change_name = State()
    change_gender = State()
    change_dob = State()
    change_init_weight = State()
    fill_done = State()

    
# draft state group for help
# TODO: add nessesary States
class HelpSG(StatesGroup):
    start_help = State()   


# draft state group for desc
# TODO: add nessesary States
class DescSG(StatesGroup):
    start_desc = State()  


# draft state group for testing Gargantua`s story  
# TODO: add nessesary States
class WhatSG(StatesGroup):
    start_what = State()
    
    
# draft state group for testing weight saving data
# TODO: add nessesary States
class MeasureSG(StatesGroup):
    start_weight = State()
    start_measure = State()
        

# draft state group for testing bot`s setup
# TODO: add nessesary States
class SetupSG(StatesGroup):
    start_setup = State()
    
    
# draft state group for testing user`s profile details
# TODO: add nessesary States
class profileSG(StatesGroup):
    start_profile = State()
    
    
# drafr start group for testing reporting system
class ReportSG(StatesGroup):
    start_report = State()
    

# draft state group for testing support function
class SupportSG(StatesGroup):
    start_support = State()


# draft state group for testing contacts sending
class ContactsSG(StatesGroup):
    start_contacts = State()
   
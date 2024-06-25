from aiogram.fsm.state import State, StatesGroup


# draft state group for testing default dialog
class DefaultSG(StatesGroup):
    default_dialog = State()


# draft state group for testing starting dialogs
# TODO: add nessesary States
class StartSG(StatesGroup):
    start_dialog = State()
    start_dialog_help = State()
    start_dialog_desc = State()
    create_account_on_start = State()
    
    
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
    
    
# draft state group for testing user`s account details
# TODO: add nessesary States
class AccountSG(StatesGroup):
    start_account = State()
    
    
# drafr start group for testing reporting system
class ReportSG(StatesGroup):
    start_report = State()
    

# draft state group for testing support function
class SupportSG(StatesGroup):
    start_support = State()


# draft state group for testing contacts sending
class ContactsSG(StatesGroup):
    start_contacts = State()

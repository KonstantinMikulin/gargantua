from bot.dialogs.states import AddWeightSG, AddMeasurmentsSG, GetLastRecordsSG, MainMenuSG
from bot.dialogs.weight_dialog import add_weight_dialog
from bot.dialogs.measure_dialog import add_measurments_dialog
from bot.dialogs.get_last_dialog import get_last_records_dialog
from bot.dialogs.main_menu_dialog import main_menu_dialog

__all__ = [
    "MainMenuSG",
    "AddWeightSG",
    "AddMeasurmentsSG",
    "GetLastRecordsSG",
    "main_menu_dialog",
    "add_weight_dialog",
    "add_measurments_dialog",
    "get_last_records_dialog",
]

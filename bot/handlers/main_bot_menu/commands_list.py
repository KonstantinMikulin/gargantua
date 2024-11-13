from aiogram.types import BotCommand

#TODO: check that all usefull commands was added
# list of commands for bot`s main menu button
main_menu_commands = [
    #TODO: remove /start command from this list
    BotCommand(command="/start", description="Запуск бота"),
    BotCommand(command="/weight", description="Записать вес"),
    BotCommand(command="/measure", description="Записать объемы"),
    BotCommand(command="/cancel", description="Отмена"),
]

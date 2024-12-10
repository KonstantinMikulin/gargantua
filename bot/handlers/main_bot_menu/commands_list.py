from aiogram.types import BotCommand

# list of commands for bot`s main menu button
main_menu_commands = [
    BotCommand(command="/start", description="Запуск бота"),
    BotCommand(command="/help", description="Описание и подсказки"),
    BotCommand(command="/main", description="Основное меню"),
    BotCommand(command="/weight", description="Записать вес"),
    BotCommand(command="/measure", description="Записать объемы"),
    BotCommand(command="/last", description="Показать последнюю запись"),
    BotCommand(command="/records", description="Показать все записи"),
]

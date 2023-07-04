from adminbot import *
from importlib import import_module
from adminbot.modules import ALL_MODULES
for module_name in ALL_MODULES:
        imported_module = import_module("adminbot.modules." + module_name)
bot.run_until_disconnected()


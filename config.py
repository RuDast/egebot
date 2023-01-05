from dotenv import load_dotenv
from colorama import Fore
import os


load_dotenv('dev.env')

try:
    BOT_TOKEN = os.getenv('TOKEN')
except (TypeError, ValueError) as ex:
    print(Fore.RED + f'Config Error: {ex}')

import sqlite3 as sql
from datetime import datetime
from colorama import Fore
from sys import exit


def sql_start():
    global db, cursor
    try:
        db = sql.connect(r'D:\Python\podegebot\database\database.db')
        cursor = db.cursor()
        if db:
            print(Fore.GREEN + 'Successful connection to the database!')
    except:
        print(Fore.RED + 'Error connection to the database!')
        exit()


async def sql_regis(id_chat):
    date = datetime.now().date()
    cursor.execute('SELECT chat_id FROM users WHERE chat_id = ?', [id_chat])
    if cursor.fetchone() is None:
        cursor.execute(
            f'''INSERT INTO users(chat_id, day, month, year) VALUES ({id_chat}, {date.day}, {date.month}, {date.year})''')
        db.commit()

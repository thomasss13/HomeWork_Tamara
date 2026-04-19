#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07

# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import functools
import datetime
import os
import json

STATS_FILE = "debug.log"
STATS_DATA_FILE = "debug_stats.json"

function_stats = {}

def load_stats():

    global function_stats
    if os.path.exists(STATS_DATA_FILE):
        try:
            with open(STATS_DATA_FILE, 'r', encoding = 'utf-8') as f:
                function_stats = json.load(f)
        except (json.JSONDecodeError, IOError):
            function_stats = {}
    else:
        function_stats = {}


def save_stats():

    with open(STATS_DATA_FILE, 'w', encoding = 'utf-8') as f:
        json.dump(function_stats, f, indent = 4, ensure_ascii = False)


def write_log():

    with open(STATS_FILE, 'w', encoding = 'utf-8') as f:
        for func_name, data in function_stats.items():
            count = data['count']
            last_call = data['last_call']
            f.write(f"{func_name}, {count}, {last_call}\n")


def stats_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        
        now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        
        if func_name not in function_stats:
            function_stats[func_name] = {'count': 0, 'last_call': now}
        
        function_stats[func_name]['count'] += 1
        function_stats[func_name]['last_call'] = now
        
        result = func(*args, **kwargs)
        
        save_stats()
        write_log()
        
        return result
    
    return wrapper


load_stats()


@stats_decorator
def render(text, times = 1):

    for _ in range(times):
        print(f"Rendering: {text}")
    return f"Rendered: {text}"


@stats_decorator
def show(message):

    print(f"Showing: {message}")
    return message


@stats_decorator
def calculate(a, b, operation='add'):

    if operation == 'add':
        result = a + b
    elif operation == 'multiply':
        result = a * b
    else:
        result = 0
    print(f"Result: {result}")
    return result


print("===== ТЕСТИРОВАНИЕ ДЕКОРАТОРА =====\n")

render("Header", 2)
show("Welcome")
calculate(5, 3, 'add')

render("Footer", 1)
show("Goodbye")
calculate(10, 2, 'multiply')

render("Content", 3)

print("\n===== СТАТИСТИКА ЗАПИСАНА В ФАЙЛЫ =====")
print(f"- {STATS_FILE} (текстовый лог)")
print(f"- {STATS_DATA_FILE} (JSON для сохранения между запусками)\n")

print("===== СОДЕРЖИМОЕ debug.log =====")
with open(STATS_FILE, 'r', encoding = 'utf-8') as f:
    print(f.read())


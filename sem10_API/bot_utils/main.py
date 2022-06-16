import telebot
from telebot import types
import sqlite3

# подключаем базу данных
conn = sqlite3.connect('planner_hse.db')

# курсор для работы с таблицами
cursor = conn.cursor()

try:
    # sql запрос для создания таблицы
    query = "CREATE TABLE \"planner\" (\"ID\" INTEGER UNIQUE, \"user_id\" INTEGER, \"plan\" TEXT, PRIMARY KEY (\"ID\"))"
    # исполняем его –> ура, теперь у нас есть таблица, куда будем все сохранять!
    cursor.execute(query)
except:
    pass

# подключим токен нашего бота
bot = telebot.TeleBot("your_token")

# напишем, что делать нашему боту при команде старт
@bot.message_handler(commands=['start'])
def send_keyboard(message, text="Привет, чем я могу тебе помочь?"):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)  # наша клавиатура
    itembtn1 = types.KeyboardButton('Добавить дело в список') # создадим кнопку
    itembtn2 = types.KeyboardButton('Показать список дел')
    itembtn3 = types.KeyboardButton('Удалить дело из списка')
    itembtn4 = types.KeyboardButton("Удалить все дела из списка")
    itembtn5 = types.KeyboardButton('Другое')
    itembtn6 = types.KeyboardButton('Пока все!')
    keyboard.add(itembtn1, itembtn2) # добавим кнопки 1 и 2 на первый ряд
    keyboard.add(itembtn3, itembtn4, itembtn5, itembtn6) # добавим кнопки 3, 4, 5 на второй ряд
    # но если кнопок слишком много, они пойдут на след ряд автоматически

    # пришлем это все сообщением и запишем выбранный вариант
    msg = bot.send_message(message.from_user.id,
                     text=text, reply_markup=keyboard)

    # отправим этот вариант в функцию, которая его обработает
    bot.register_next_step_handler(msg, callback_worker)

@bot.message_handler(content_types=['text'])
def handle_docs_audio(message):
    send_keyboard(message, text="Я не понимаю :-( Выберите один из пунктов меню:")

# напишем функции для каждого случая
# эта добавляет строчку с планом в хранилище
def add_plan(msg):
    with sqlite3.connect('planner_hse.db') as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO planner (user_id, plan) VALUES (?, ?)',
                       (msg.from_user.id, msg.text))
        con.commit()
    bot.send_message(msg.chat.id, 'Запомню :-)')
    send_keyboard(msg, "Чем еще могу помочь?")

# просто функция, которая делает нам красивые строки для отправки пользователю
def get_plans_string(tasks):
    tasks_str = []
    for val in list(enumerate(tasks)):
        tasks_str.append(str(val[0] + 1) + ') ' + val[1][0] + '\n')
    return ''.join(tasks_str)

# отправляем пользователю его планы
def show_plans(msg):
    with sqlite3.connect('planner_hse.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT plan FROM planner WHERE user_id=={}'.format(msg.from_user.id))
        tasks = get_plans_string(cursor.fetchall())
        bot.send_message(msg.chat.id, tasks)
        send_keyboard(msg, "Чем еще могу помочь?")

# удаляет все планы для конкретного пользователя
def delete_all_plans(msg):
    with sqlite3.connect('planner_hse.db') as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM planner WHERE user_id=={}'.format(msg.from_user.id))
        con.commit()
    bot.send_message(msg.chat.id, 'Удалены все дела. Хорошего отдыха!')
    send_keyboard(msg, "Чем еще могу помочь?")

# выыделяет одно дело, которое пользователь хочет удалить
def delete_one_plan(msg):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    with sqlite3.connect('planner_hse.db') as con:
        cursor = con.cursor()
        # достаем все задачи пользователя
        cursor.execute('SELECT plan FROM planner WHERE user_id=={}'.format(msg.from_user.id))
        # достанем результат запроса
        tasks = cursor.fetchall()
        for value in tasks:
            markup.add(types.KeyboardButton(value[0]))
        msg = bot.send_message(msg.from_user.id,
                               text = "Выбери одно дело из списка",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, delete_one_plan_)

# удаляет это дело
def delete_one_plan_(msg):
    with sqlite3.connect('planner_hse.db') as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM planner WHERE user_id==? AND plan==?', (msg.from_user.id, msg.text))
        bot.send_message(msg.chat.id, 'Ура, минус одна задача!')
        send_keyboard(msg, "Чем еще могу помочь?")

# привязываем функции к кнопкам на клавиатуре
def callback_worker(call):
    if call.text == "Добавить дело в список":
        msg = bot.send_message(call.chat.id, 'Давайте добавим дело! Напишите его в чат')
        bot.register_next_step_handler(msg, add_plan)

    elif call.text == "Показать список дел":
        try:
            show_plans(call)
        except:
            bot.send_message(call.chat.id, 'Здесь пусто. Можно отдыхать :-)')
            send_keyboard(call, "Чем еще могу помочь?")

    elif call.text == "Удалить дело из списка":
        try:
            delete_one_plan(call)
        except:
            bot.send_message(call.chat.id, 'Здесь пусто. Можно отдыхать :-)')
            send_keyboard(call, "Чем еще могу помочь?")

    elif call.text == "Удалить все дела из списка":
        try:
            delete_all_plans(call)
        except:
            bot.send_message(call.chat.id, 'Здесь пусто. Можно отдыхать :-)')
            send_keyboard(call, "Чем еще могу помочь?")

    elif call.text == "Другое":
        bot.send_message(call.chat.id, 'Больше я пока ничего не умею :-(')
        send_keyboard(call, "Чем еще могу помочь?")

    elif call.text == "Пока все!":
        bot.send_message(call.chat.id, 'Хорошего дня! Когда захотите продолжнить нажмите на команду /start')



bot.polling(none_stop=True)

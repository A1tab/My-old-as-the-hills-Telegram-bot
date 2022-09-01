import telebot
from telebot import types
import random
import datetime
from datetime import datetime, timedelta
import requests
import pyowm
from pyowm.utils.config import get_default_config
from bot_token import *            


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types=['text']) 

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def get_text_messages(message):
    hi = ['Привет', "Ну привет","Ку", "Здравствуй", "Здравствуйте","Здарова","Хай","Privet",'P','П','Прив'] 
    stik = open('C:/Users/250/Desktop/Py/Bot/stikers/ky.webp', 'rb')
    stik2 = open('C:/Users/250/Desktop/Py/Bot/stikers/kek1.tgs', 'rb')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)        
    item1 = types.KeyboardButton('Погода\n🌪')                        # Выводит информацию о сегодняшней погоде 
    item2 = types.KeyboardButton('Анекдоты\n😂')                     # Отправляет анекдоты с сайта ржунемогу.ру
    item3 = types.KeyboardButton('Расписание😢')                     # Показывает расписание на указанную дату
    item4 = types.KeyboardButton('Пары сегодня😡')                   # Показывает расписание на сегодня
    item5 = types.KeyboardButton('🔮Пойти ли на пару?🔮')            # Гадает на посещение пар
    item6 = types.KeyboardButton('Пары завтра🧎‍♂️')                     # Показывает расписание на завтра
    item7 = types.KeyboardButton('Случайный\n💘Роман💘')            # Выводит случайную фотографию Романа
    markup.add(item1,item7,item3,item4,item2,item6,item5)            
             
    bot.send_chat_action(message.chat.id, 'typing')

    if message.text.capitalize() in hi:
        bot.send_message(message.chat.id, 'Бот на месте', reply_markup=markup)
        bot.register_next_step_handler(message, start)
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Используйне панель управления\nP.S. Если бот, вдруг, начнет отправлять сообщения дважды, попроси анекдот и все снова заработает\nДа-да, не удивляйтесь')
        bot.send_sticker(message.chat.id, stik2)
    elif message.text == '/start':
        bot.send_sticker(message.chat.id, stik)
        bot.send_message(message.chat.id, "Добро пожаловать на дефолтный уровень бытия, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот\nНапиши что угодно чтобы получить панель управления".format(message.from_user, bot.get_me()),parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Бот на месте', reply_markup=markup)
        bot.register_next_step_handler(message, start)


def start(message):
    if message.text == 'Расписание😢':
        bot.send_message(message.chat.id, 'Введите дату через точку. Например 25.05')
        bot.register_next_step_handler(message, razp)

    elif message.text == '🔮Пойти ли на пару?🔮':
        dilema(message)
                                    
    elif message.text == 'Погода\n🌪':
        bot.send_chat_action(message.chat.id, 'typing')                
        Pogoda(message)

    elif message.text == 'Случайный\n💘Роман💘':
        RandomRoman(message)

    elif message.text == 'Анекдоты\n😂':                                  
        global anekboard   
        anekboard = types.InlineKeyboardMarkup(row_width=2)

        item1 = types.InlineKeyboardButton('Анекдоты категории б', callback_data='b')
        item2 = types.InlineKeyboardButton('Анекдоты категории б+', callback_data='b+')
        item3 = types.InlineKeyboardButton('Стишки', callback_data='poetry')

        anekboard.add(item1,item2,item3)

        bot.send_message(message.chat.id, 'Стратегический запас анекдотов', reply_markup=anekboard) 

    elif message.text == 'Пары сегодня😡': 
        segodnya(message)               

    elif message.text == 'Пары завтра🧎‍♂️':
        zavtra(message)

    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Используйне панель управления\nP.S. Если бот, вдруг, начнет отправлять сообщения дважды, попроси анекдот и все снова заработает\nДа-да, не удивляйтесь')
        bot.register_next_step_handler(message, start)

    else:
        bot.send_message(message.from_user.id, 'Используйте панель управления')     
        bot.register_next_step_handler(message, start)


def dilema(message):
    try:
        stik1 = open('C:/Users/250/Desktop/Py/Bot/stikers/kek3.PNG', 'rb')
        stik2 = open('C:/Users/250/Desktop/Py/Bot/stikers/kek4.jpg', 'rb')
        stik3 = open('C:/Users/250/Desktop/Py/Bot/stikers/kek5.PNG', 'rb')
        gif = open('C:/Users/250/Desktop/Py/Bot/stikers/tenor.gif', 'rb') 
        Theses = {
        0:'Придется идти. Таков путь.',
        1:'Всегда лучше наблюдать за процессом, чем делать что-то самому.\n <i>—Гомер Симпсон</i>',
        2:'Попытка - первый шаг к провалу.\n <i>—Гомер Симпсон</i>',
        3:'Не вижу смысла выходить из дома. Мы все равно каждый раз возвращаемся обратно.\n <i>—Гомер Симпсон</i>',
        4:'Не вижу смысла выходить из дома. Мы все равно каждый раз возвращаемся обратно.\n <i>—Гомер Симпсон</i>'
        }
        

        Tkey = random.randint(0,4)

        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_sticker(message.chat.id, random.choice([stik1,stik2,stik3]))       
        if Tkey > 0:
            bot.send_message(message.chat.id, '%s входит в %s дом' % (random.choice(['Марс','Юпитер','Сатурн','Нептун','Венера']),random.choice(['первый','третий','четвертый','пятый','шестой','седьмой','восьмой'])))
            bot.send_message(message.chat.id, 'Свечи горят %s, %s, пламя %s' % (random.choice(['ровно','черным пламенем, коптят']),random.choice(['трещат','не трещат']),random.choice(['тусклое','яркое','ослепительное'])))
            bot.send_message(message.chat.id, '%s узор кофейной гущи %s ближе к %s' % (random.choice(['Большой','Малый']), random.choice(['темнеет','светлеет']), random.choice(['ручке','краю'])))
            bot.send_message(message.chat.id, 'Звезды говорят: <b>%s</b>' % 'Останься дома.',parse_mode='html')
            bot.send_message(message.chat.id, Theses[Tkey],parse_mode='html')
        else:
            bot.send_message(message.chat.id, 'Ваша планета-покровитель скрылась за черными тучами')
            bot.send_message(message.chat.id, 'Свечи потухли')
            bot.send_message(message.chat.id, 'Чаша пуста')
            bot.send_message(message.chat.id, 'Звезды говорят: <b>%s</b>' % 'Блять.',parse_mode='html')
            bot.send_message(message.chat.id, Theses[Tkey],parse_mode='html')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_animation(message.chat.id, gif)
    except Exception:
        bot.send_message(message.chat.id, 'Вашу судьбу сложно разобрать, повторите попытку')

    bot.register_next_step_handler(message, start)         


def RandomRoman(message):  

    s = open('C:/Users/250/Desktop/Py/Bot/stikers/Rn.gif', 'rb')
    s1 = open('C:/Users/250/Desktop/Py/Bot/stikers/s1.PNG', 'rb')
    s2 = open('C:/Users/250/Desktop/Py/Bot/stikers/s2.jpg', 'rb')
    s3 = open('C:/Users/250/Desktop/Py/Bot/stikers/s3.jpg', 'rb')
    s4 = open('C:/Users/250/Desktop/Py/Bot/stikers/s4.jpg', 'rb')
    s5 = open('C:/Users/250/Desktop/Py/Bot/stikers/s5.PNG', 'rb')
    s6 = open('C:/Users/250/Desktop/Py/Bot/stikers/s6.PNG', 'rb')
    s7 = open('C:/Users/250/Desktop/Py/Bot/stikers/s7.PNG', 'rb')    
    
    roma = random.choice([s,s1,s2,s3,s4,s5,s6,s7])

    if roma == s:
        bot.send_chat_action(message.chat.id, 'record_video')
        bot.send_animation(message.chat.id, roma)
    else:
        bot.send_sticker(message.chat.id, roma)

    bot.register_next_step_handler(message, start)
    
       
def Pogoda(message):

    owm = pyowm.OWM(WTOKEN) 

    config_dict = get_default_config()
    config_dict['language'] = 'ru'

    place = 'Москва'
    wm = owm.weather_manager()   
    obs = wm.weather_at_place(place) #Задаем город

    w = obs.weather  #Объект со всей погодой в заданном городе

    t = w.temperature('celsius')   #Температура

    Temper = t['temp']
    if Temper > 0:
        Temper = '+'+str(Temper)

    Real_Temper = t['feels_like']
    if Real_Temper > 0:
        Real_Temper = '+'+str(Real_Temper)

    dt = w.detailed_status.capitalize() #Статус погоды

    wi = w.wind()['speed'] #Скорость ветра (без м\с)

    pr = w.pressure['press'] #Давление


    bot.send_message(message.chat.id, f'Температура {Temper}, ощущается как {Real_Temper} \n{dt} \nСкорость ветра: {wi} м/с \nДавление: {pr}')
    bot.register_next_step_handler(message, start)


@bot.callback_query_handler(func=lambda call: True)
def Anekdot(call):

    url1 = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'          
    url2 = 'http://rzhunemogu.ru/RandJSON.aspx?CType=11'
    url3 = 'http://rzhunemogu.ru/RandJSON.aspx?CType=13'

    r1 = requests.get(url1)
    r2 = requests.get(url2)
    r3 = requests.get(url3)

    b = r2.text
    b_plus = r1.text
    poetry = r3.text

    if call.data == 'b':    
        bot.answer_callback_query(call.id)                      #убирает задержку для повторного нажатия кнопки
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= b[12:-2], reply_markup=anekboard)
    elif call.data == 'b+':
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= b_plus[12:-2], reply_markup=anekboard)
    elif call.data == 'poetry':
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= poetry[12:-2], reply_markup=anekboard)
    

global Mo1,Mo2,We1,We2,Th1,Th2,Fr1,Fr2,Sa1,Sa2
Mo1 = ['        10:40|Криптографика|Догнак|пр|И-204-б\n12:40|Организационное и правовое обеспечение информационной безопасности|Догнак|пр|И-204-б\n']
Mo2 = ['        12:40|Организационное и правовое обеспечение информационной безопасности|Догнак|пр|И-204-б\n14:20|Конструктивно-технологическое обеспечение средств связи|Ярлыкова|пр|И-201\n16:20|Социальная инженерия|Жемерикина|пр|A-318\n18:00|Цифровая обработка сигналов|Певзнер|лаб|Г-401-1\n']
We1 = ['        12:40|Основы теории чисел|Зайцев|дистант\n14:20|Конструктивно-технологическое обеспечение средств связи|Ярлыкова|дистант\n12:40|Математические основы теории защиты информации|Зайцев|дистант\n18:00|Теория радиотехнических сигналов|Козлов|\n']
We2 = ['        12:40|Основы теории чисел|Зайцев|дистант\n14:20|Цифровая обработка сигналов|Певзнер|дистант\n12:40|Математические основы теории защиты информации|Зайцев|дистант\n18:00|Теория радиотехнических сигналов|Козлов|\n']
Th1 = ['        10:40|Социальная инженерия|Жемерикина|дистант\n12:40|Организационное и правовое обеспечение информационной безопасности|Догнак|дистант\n14:20|Криптографика|Догнак|дистант\n16:20|Разработка защищенных телекоммуникационных систем специального назначения|Шароватов|дистант\n']
Th2 = ['        12:40|Организационное и правовое обеспечение информационной безопасности|Догнак|дистант\n14:20|Криптографика|Догнак|дистант\n16:20|Разработка защищенных телекоммуникационных систем специального назначения|Шароватов|дистант\n']
Fr1 = ['        16:20|Теория радиотехнических сигналов|Авдеев|пр|A-210\n18:00|Математические основы теории защиты информации|Зайцев|лаб|A-217\n']
Fr2 = ['        16:20|Теория радиотехнических сигналов|Авдеев|лаб|A-210\n18:00|Основы теории чисел|Зайцев|пр|A-217\n']
Sa1 = ['        16:20|Разработка защищенных телекоммуникационных систем специального назначения|Шароватов|пр|И-204-б\n18:00|Разработка защищенных телекоммуникационных систем специального назначения|Шароватов|пр|И-204-б\n']
Sa2 = ['        16:20|Разработка защищенных телекоммуникационных систем специального назначения|Шароватов|пр|И-204-б\n18:00|Разработка защищенных телекоммуникационных систем специального назначения|Шароватов|пр|И-204-б\n']


def razp(message):
    
    date_of_pars = message.text
    splitit = date_of_pars.split('.')

    bot.register_next_step_handler(message, start)  

    try:
        day = int(splitit[0])
        month = int(splitit[1])
        b = datetime(2021,int(month),int(day))
    except ValueError: 
        bot.send_message(message.chat.id, 'Некорректная дата. Вводите <b>числа</b> через точку. Можно даже без нулей, например 3.5\nСейчас вас вернуло в меню',parse_mode='html')
    except Exception:
        bot.send_message(message.chat.id, 'Некорректная дата. Вводите <b>числа</b> через точку. Можно даже без нулей, например 3.5\nСейчас вас вернуло в меню',parse_mode='html')
    else:
        day = int(splitit[0])
        month = int(splitit[1])
        week = None
        stik = open('C:/Users/250/Desktop/Py/Bot/stikers/pizdec.webp', 'rb')
        stik2 = open('C:/Users/250/Desktop/Py/Bot/stikers/kek2.tgs', 'rb')

        b = datetime(2021,int(month),int(day))
        sep = datetime(b.year if b.month >= 9 else b.year - 1, 9, 1) #Определение четности недели
        d1 = sep - timedelta(days=sep.weekday())
        d2 = b - timedelta(days=b.weekday())
        parity = ((d2 - d1).days // 7) % 2

        if parity == 1:
            week = 1
        else:
            week = 2

        t = b.strftime("%w")

        if int(t) == 6:
            if week == 1:
                bot.send_message(message.chat.id, 'Суббота')
                bot.send_message(message.chat.id, Sa1)
            else:
                bot.send_message(message.chat.id, 'Суббота')                            
                bot.send_message(message.chat.id, Sa2)
        elif int(t) == 5:
            if week == 1:
                bot.send_message(message.chat.id, 'Пятница')        
                bot.send_message(message.chat.id, Fr1)
            else:
                bot.send_message(message.chat.id, 'Пятница')
                bot.send_message(message.chat.id, Fr2)
        elif int(t) == 4:
            if week == 1:
                bot.send_message(message.chat.id, 'Четверг')
                bot.send_message(message.chat.id, Th1)          
            else:
                bot.send_message(message.chat.id, 'Четверг')
                bot.send_message(message.chat.id, Th2)
        elif int(t) == 3:
            if week == 1:
                bot.send_message(message.chat.id, 'Среда')
                bot.send_message(message.chat.id, We1)
            else:
                bot.send_message(message.chat.id, 'Среда')
                bot.send_message(message.chat.id, We2) 
        elif int(t) == 2:                              
            bot.send_message(message.chat.id, 'Вторник')
            bot.send_message(message.chat.id, 'Выходной')
            bot.send_sticker(message.chat.id, stik2)
        elif int(t) == 0:                              
            bot.send_message(message.chat.id, 'Воскресенье')
            bot.send_message(message.chat.id, 'Выходной')
            bot.send_sticker(message.chat.id, stik2)
        elif int(t) == 1:
            if week == 1:
                bot.send_message(message.chat.id, 'Понедельник')
                bot.send_message(message.chat.id, Mo1)   
            else:
                bot.send_message(message.chat.id, 'Понедельник')
                bot.send_message(message.chat.id, Mo2)
                bot.send_sticker(message.chat.id, stik)
    finally:
        bot.register_next_step_handler(message, start)


def segodnya(message):

    stik = open('C:/Users/250/Desktop/Py/Bot/stikers/pizdec.webp', 'rb')
    stik2 = open('C:/Users/250/Desktop/Py/Bot/stikers/kek2.tgs', 'rb')

    now = datetime.now() 
    sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)    #Определение четности недели
    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())
    parity = ((d2 - d1).days // 7) % 2
    
    if parity == 1:
        week = 1
    else:
        week = 2 

    t = now.strftime("%w")

    if int(t) == 6:
        if week == 1:
            bot.send_message(message.chat.id, 'Суббота')
            bot.send_message(message.chat.id, Sa1)
        else:
            bot.send_message(message.chat.id, 'Суббота')                           
            bot.send_message(message.chat.id, Sa2)
    elif int(t) == 5:
        if week == 1:
            bot.send_message(message.chat.id, 'Пятница')        
            bot.send_message(message.chat.id, Fr1)
        else:
            bot.send_message(message.chat.id, 'Пятница')
            bot.send_message(message.chat.id, Fr2)
    elif int(t) == 4:
        if week == 1:
            bot.send_message(message.chat.id, 'Четверг')
            bot.send_message(message.chat.id, Th1)          
        else:
            bot.send_message(message.chat.id, 'Четверг')
            bot.send_message(message.chat.id, Th2)
    elif int(t) == 3:
        if week == 1:
            bot.send_message(message.chat.id, 'Среда')
            bot.send_message(message.chat.id, We1)
        else:
            bot.send_message(message.chat.id, 'Среда')
            bot.send_message(message.chat.id, We2)
    elif int(t) == 2:                             
        bot.send_message(message.chat.id, 'Вторник')
        bot.send_message(message.chat.id, 'Выходной')
        bot.send_sticker(message.chat.id, stik2)
    elif int(t) == 0:                             
        bot.send_message(message.chat.id, 'Воскресенье')
        bot.send_message(message.chat.id, 'Выходной')
        bot.send_sticker(message.chat.id, stik2)
    elif int(t) == 1:
        if week == 1:
            bot.send_message(message.chat.id, 'Понедельник')
            bot.send_message(message.chat.id, Mo1)   
        else:
            bot.send_message(message.chat.id, 'Понедельник')
            bot.send_message(message.chat.id, Mo2)
            bot.send_sticker(message.chat.id, stik)

    bot.register_next_step_handler(message, start)    


def zavtra(message):

    stik = open('C:/Users/250/Desktop/Py/Bot/stikers/pizdec.webp', 'rb')
    stik2 = open('C:/Users/250/Desktop/Py/Bot/stikers/kek2.tgs', 'rb')
        
    now = datetime.now()                                    
    sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)         #Определение четности недели
    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())
    parity = ((d2 - d1).days // 7) % 2

    if parity == 1:
        week = 1
    else:
        week = 2 

    t = int(now.strftime("%w")) + 1

    if t == 7:
        t = 0

    if int(t) == 6:
        if week == 1:
            bot.send_message(message.chat.id, 'Суббота')
            bot.send_message(message.chat.id, Sa1)
        else:
            bot.send_message(message.chat.id, 'Суббота')                            
            bot.send_message(message.chat.id, Sa2)
    elif int(t) == 5:
        if week == 1:
            bot.send_message(message.chat.id, 'Пятница')        
            bot.send_message(message.chat.id, Fr1)
        else:
            bot.send_message(message.chat.id, 'Пятница')
            bot.send_message(message.chat.id, Fr2)
    elif int(t) == 4:
        if week == 1:
            bot.send_message(message.chat.id, 'Четверг')
            bot.send_message(message.chat.id, Th1)          
        else:
            bot.send_message(message.chat.id, 'Четверг')
            bot.send_message(message.chat.id, Th2)
    elif int(t) == 3:
        if week == 1:
            bot.send_message(message.chat.id, 'Среда')
            bot.send_message(message.chat.id, We1)
        else:
            bot.send_message(message.chat.id, 'Среда')
            bot.send_message(message.chat.id, We2)
    elif int(t) == 2:                              
        bot.send_message(message.chat.id, 'Вторник')
        bot.send_message(message.chat.id, 'Выходной')
        bot.send_sticker(message.chat.id, stik2)
    elif int(t) == 0:                             
        bot.send_message(message.chat.id, 'Воскресенье')
        bot.send_message(message.chat.id, 'Выходной')
        bot.send_sticker(message.chat.id, stik2)
    elif int(t) == 1:
        if week == 1:
            bot.send_message(message.chat.id, 'Понедельник')
            bot.send_message(message.chat.id, Mo1)   
        else:
            bot.send_message(message.chat.id, 'Понедельник')
            bot.send_message(message.chat.id, Mo2)
            bot.send_sticker(message.chat.id, stik)

    bot.register_next_step_handler(message, start)  



bot.polling(none_stop=True, interval=0)



import requests
from telebot import types
from bs4 import BeautifulSoup
import random
import telebot
token = '5856646623:AAEKHoiSmxnNUqMvUAACx2AwGcddYU-oMvY'

bot = telebot.TeleBot(token)


def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='p-2 clearfix'))
    return [res.text, res.a.attrs['href']]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_txt = '''Добро пожаловать!'''
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    btn1 = telebot.types.KeyboardButton('Факт')
    btn3 = telebot.types.KeyboardButton('Кнопка 3')
    btn4 = telebot.types.KeyboardButton('Стикер')
    btn5 = telebot.types.KeyboardButton('Во что можно поиграть?')
    keyboard.add(btn1, btn3, btn4, btn5)
    bot.send_message(message.chat.id, welcome_txt, reply_markup=keyboard)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    text = get_fact()
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_in = telebot.types.InlineKeyboardButton('Перейти...', url=text[1])
    keyboard.add(button_in)
    bot.send_message(message.chat.id, text[0], reply_markup=keyboard)


@bot.message_handler(commands=['img'])
def send_img(message):
    # number_img = random.randint(1, 3)
    # # img = open(str(number_img) + '_send_photo.png', 'rb')
    # img = open(f'{number_img}_send_photo.png', 'rb')
    name_random_img = random.choice(['1_send_photo.png', '2_send_photo.png', '3_send_photo.png'])
    img = open(name_random_img, 'rb')
    bot.send_photo(message.chat.id, img)


@bot.message_handler(content_types='text')
def message_reply(message):
    if 'факт' in message.text.lower():
        send_fact(message)
    elif 'Кнопка 3' == message.text:
        bot.send_message(message.chat.id, 'Ты нажал на кнопку 3!')
    elif 'Стикер' == message.text:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG7lZjoycd83uFPwW_QCwPlSGnZ0ojLQACLQwAAkKvaQABylqlGZsif0csBA')
    elif message.text == 'Во что можно поиграть?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бесплатно')
        btn2 = types.KeyboardButton('Ранний доступ')
        btn3 = types.KeyboardButton('Гонки')
        btn4 = types.KeyboardButton('Инди')
        btn5 = types.KeyboardButton('Казуальная игра')
        btn6 = types.KeyboardButton('ММО')
        btn7 = types.KeyboardButton('Приключение')
        btn8 = types.KeyboardButton('Ролевая игра')
        btn9 = types.KeyboardButton('Симулятор')
        btn10 = types.KeyboardButton('Спортивная игра')
        btn11 = types.KeyboardButton('Стратегия')
        btn12 = types.KeyboardButton('Экшен')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
        bot.send_message(message.chat.id, text='Выберите жанр: '.format(message.from_user),  reply_markup=markup)
    elif message.text == 'Бесплатно':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в Warframe.
        https://store.steampowered.com/app/230410/Warframe/
        ''')
    elif message.text == 'Ранний доступ':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в V Rising.
        https://store.steampowered.com/app/1604030/V_Rising/
        ''')
    elif message.text == 'Гонки':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в CarX Drift Racing Online.
        https://store.steampowered.com/app/635260/CarX_Drift_Racing_Online/
        ''')
    elif message.text == 'Инди':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в Hades.
        https://store.steampowered.com/app/1145360/Hades/
        ''')
    elif message.text == 'Казуальная игра':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в Slime Rancher 2.
        https://store.steampowered.com/app/1657630/Slime_Rancher_2/
        ''')
    elif message.text == 'ММО':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в NARAKA: BLADEPOINT.
        https://store.steampowered.com/app/1203220/NARAKA_BLADEPOINT/
        ''')
    elif message.text == 'Приключение':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в ARK: Survival Evolved.
        https://store.steampowered.com/app/346110/ARK_Survival_Evolved/
        ''')
    elif message.text == 'Ролевая игра':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в ONE PIECE ODYSSEY.
        https://store.steampowered.com/app/814000/ONE_PIECE_ODYSSEY/
        ''')
    elif message.text == 'Симулятор':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в Mount & Blade II: Bannerlord.
        https://store.steampowered.com/app/261550/Mount__Blade_II_Bannerlord/
        ''')
    elif message.text == 'Спортивная игра':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в TEKKEN 7.
        https://store.steampowered.com/app/389730/TEKKEN_7/
        ''')
    elif message.text == 'Стратегия':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в Counter-Strike: Global Offensive.
        https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/
        ''')
    elif message.text == 'Экшен':
        bot.send_message(message.chat.id, text='''
        Советую поиграть вам в PAYDAY 2.
        https://store.steampowered.com/app/218620/PAYDAY_2/
        ''')
    else:
        bot.send_message(message.chat.id, message.text)
    
bot.polling()
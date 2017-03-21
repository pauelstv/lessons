# azazakek bot
import telebot # подключение библиотеки pyTelegramBotAPI
import logging # библиотека журнала
from telebot import types #подключим клавиатуры
import datetime
from datetime import datetime, timedelta
def get_currensies(dateYear, dateMonth, dateDay, currensiesName):
    """ Возвращает курсы USD и EUR на сегодняшнее число """
    from pycbrf.toolbox import ExchangeRates
    now = datetime.now()
    print("%s-%s-%s" % (now.year, now.month, now.day))
    # Запрашиваем данные на 26-е июня.
    #rates = ExchangeRates('2016-06-26')
    rates = ExchangeRates(str("%s-%s-%s" % (now.year, now.month, now.day)))
    rates.date_requested  # 2016-06-26 00:00:00
    rates.date_received  # 2016-06-25 00:00:00
    # 26-е был выходной, а курс на выходные установлен 25-го
    rates.dates_match  # False
    # Список всех курсов валют на день доступ в rates.rates.
    # Поддерживаются разные идентификаторы валют:
    #rates['USD'].name  # Доллар США
    #rates['R01235'].name  # Доллар США
    #rates['840'].name  # Доллар США
    return str(rates[currensiesName].value)
    #print("Доллар США: ", rates['USD'].value)
    #print("Евро: ", rates['EUR'].value)


print('azazakek bot started')

# для запуска скриптов
from subprocess import call

# настройки для журнала
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('/home/pauelstv/azazakekbot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# создание бота с его токеном API
bot = telebot.TeleBot("egegddddddddddddddddddddddddddddddddddddddddd")

# текст справки
help_string = []
help_string.append("Бот для несения всякой хуеты например11  \n\n")
help_string.append("/start - хая!1;\n")
help_string.append("/help - для поехавших;\n")
help_string.append("/server - чо там с серваком?")
help_string.append("/kurs - чо там с курсами?")

# --- команды

@bot.message_handler(commands=['start'])
def send_start(message):
    # отправка простого сообщения
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(name) for name in ['🚀 Server', '💻 Printers', '⚡️ VPN', '📈 MAIN']])


    bot.send_message(message.chat.id, "Вечер в хату %username%! Ито бот который несет ебаную неведомую хуйню. Швахни /help ЖИЗНЬ ВОРАМ!11", reply_markup=keyboard)
    #обработчик ответа с кнопки: keyResponse

    bot.register_next_step_handler(message, keyResponse)
    keyboard = types.ReplyKeyboardRemove()

def keyResponse(message):
    if message.text == '🚀 Server':
        print('🚀 Server')
        bot.send_message(message.chat.id,'Сервак в дауне')

    elif message.text == '💻 Printers':
        print('💻 Printers')
        bot.send_message(message.chat.id, 'Состояние принтеров')
    elif message.text == '⚡️ VPN':
        print('📈 Process')
        bot.send_message(message.chat.id,'OpenVPN: активные сессии:')
    elif message.text == '📈 MAIN':
        print('⚡️ VPN')
        bot.send_message(message.chat.id, '/start')

@bot.message_handler(commands=['help'])
def send_help(message):
    # отправка сообщения с поддержкой разметки Markdown
    bot.send_message(message.chat.id, "".join(help_string), parse_mode="Markdown")

@bot.message_handler(commands=['server'])
def send_server(message):
    try:
        # по этому пути на сервере лежит скрипт сбора информации по статусу сервера
        call(["/home/pauelstv/status.sh"])
        # читает файл с результатами выполнения скрипта
        status = open("/home/pauelstv/status.txt", "rb").read()
        bot.send_message(message.chat.id, status, parse_mode="Markdown")
    except Exception as e:
        logger.exception(str(e))
        bot.send_message(message.chat.id, "Ошибка при получении статуса сервера. Подробности в журнале.")

@bot.message_handler(commands=['kurs'])
def send_kurs(message):
#    bot.send_message(message.chat.id, "📅 Курсы валют на: " + str("%s-%s-%s" % (now.year, now.month, now.day)) + "\n USD: " + str(rates['USD'].value) + "\n EUR: "
#     + str(rates['EUR'].value))
    now = datetime.now()
    bot.send_message(message.chat.id, "📅 Курсы валют на: " + str("%s-%s-%s" % (now.year, now.month, now.day)) + "\n USD: " + get_currensies(now.year, now.month, now.day, "USD") + "\n EUR: " + get_currensies(now.year, now.month, now.day, "EUR"))

# запуск приёма сообщений
bot.polling()
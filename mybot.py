# azazakek bot
import telebot # подключение библиотеки pyTelegramBotAPI
import logging # библиотека журнала
from telebot import types #подключим клавиатуры
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
bot = telebot.TeleBot("1111111111111111111111111111")

# текст справки
help_string = []
help_string.append("Бот для несения всякой хуеты например11  \n\n")
help_string.append("/start - хая!1;\n")
help_string.append("/help - для поехавших;\n")
help_string.append("/server - чо там с серваком?")

# --- команды

@bot.message_handler(commands=['start'])
def send_start(message):
    # отправка простого сообщения
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(name) for name in ['🚀 Server', '💻 Printers', '📈 Process', '⚡️ VPN']])


    bot.send_message(message.chat.id, "Вечер в хату %username%! Ито бот который несет ебаную неведомую хуйню. Швахни /help ЖИЗНЬ ВОРАМ!11", reply_markup=keyboard)
    #обработчик ответа с кнопки: keyResponse
    bot.register_next_step_handler(message,keyResponse)

def keyResponse(message):
    if message.text == '🚀 Server':
        print('🚀 Server')
        bot.send_message(message.chat.id,'Сервак в дауне')
    elif message.text == '💻 Printers':
        print('💻 Printers')
        bot.send_message(message.chat.id, 'Состояние принтеров')
    elif message.text == '📈 Process':
        print('📈 Process')
        bot.send_message(message.chat.id,'Процессы и загрузка')
    elif message.text == '⚡️ VPN':
        print('⚡️ VPN')
        bot.send_message(message.chat.id, 'OpenVPN: активные сессии')

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

# запуск приёма сообщений
bot.polling()
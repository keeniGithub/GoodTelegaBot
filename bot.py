# Telegram bot GoodTelegaBot created by Itzkeeni
# lasted bot version: 0.5.7
# Donate: donationalerts.com/r/keenioff
# Bot url: web.telegram.org/z/#5609632846
# Bot name: @GoodTelegaBot
# Test bot: @GoodTelegaTestBot
# Discord: discord.gg/zn5usa2GAc
# Telegram channel: t.me/keenitelega

# Бот был создан для изучения Python, в боте началась разработка майнера
# Появится он не раньше 0.7.0 поскольку нужно будет настраивать БД


from urllib import response 
import telebot  #Подключаем библиотеку телеграма 
import time as t #Подключаем библиотеку для управлением временем 
import requests #Подключаем библиотеку для HTTP-Запросов
from datetime import datetime #Подключаем библиотеку узнавания времени, время будет такое же как на вашем пк, тоесть у вас будет стоять 2025 год, то показыватся будет именно такой год
bot = telebot.TeleBot('ваш токен бота') #Здесь вы пишите токен бота 

#Настройка команд
#Настройка команды /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Прив! Ты зашел в бота GoodTelegaBot!\nЭто бот от Itzkeeni, был создан для изучения Python\n Для помощи пиши /help')
#Настройка команды /kirp
@bot.message_handler(commands=["kirp"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Кирпич') #Send_message будет отправлять текст написаный в ''
#Настройка команды /sticker    
@bot.message_handler(commands=["sticker"])
def start(m, res=False):
    stick = open('stick.webp', 'rb') #Открываем файл для записи и чтения
    bot.send_sticker(m.chat.id, stick) #Отправляем стикер
#Настройка команды /help
@bot.message_handler(commands=["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Список команд:\n/kirp\n/sticker\n/bebis\n/secret\n/btc\n/time\n   \nGitHub - https://github.com/keeniGithub/GoodTelegaBot\n     \nМожешь поддержать меня рублём по ссылке ниже:\ndonationalerts.com/r/keenioff\n  \n(latest version bot: 0.5.7)')
#Настройка команды /bebis
@bot.message_handler(commands=["bebis"])
def start(m, res=False):
    photo = open('bebris.png', 'rb') #Открываем файл для записи и чтения
    bot.send_photo(m.chat.id, photo) #Отправляем фото 
#Настройка команды /secret
@bot.message_handler(commands=["secret"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Что?') 
    t.sleep(2.3) #Задержка 2.3 секунды
    bot.send_message(m.chat.id, 'Ты действительно написал эту команду...')
    t.sleep(4) #Задержка 4 секунды
    bot.send_message(m.chat.id, 'Тогда держи:')
    t.sleep(3) #Задержка 3 секунды
    bot.send_message(m.chat.id, 'https://l2l.bar/LAMBMw')  #Отправляем ссылку на фото   
#Настройка команды /btc
@bot.message_handler(commands=["btc"])
def start(m, res=False):
    #P.S. Я плохо понимаю что тут делается, так что
    req = requests.get(url="https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()  
    sell_price = response["btc_usd"]["sell"]
    bot.send_message(m.chat.id, 'На момент:')
    bot.send_message(m.chat.id, f"{datetime.now().strftime('%Y.%m.%d %H:%M')}\n   \nЦена Биткоина: {sell_price}$") #Отправляем дату и цену Биткоина на данный момент
#Настройка команды /time
@bot.message_handler(commands=["time"])
def start(m, res=False):    
    bot.send_message(m.chat.id, f"{datetime.now().strftime('%Y.%m.%d %H:%M')}") #Отправляем какое сейчас время по МСК
#Запуск бота              
bot.polling(none_stop=True, interval=0)

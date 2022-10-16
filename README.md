<p align="center">
  <img src="https://cdn.discordapp.com/attachments/863751311698165770/1031136134962622545/unknown.png">
</p>

<h1 align="center">
  <b>GoodTelegaBot</b>
</h1>

 <p align="center">   
    <a href="https://t.me/GoodTelegaBot">Clik here</a>
<h3 align="center">
  <b>Telegram bot GoodTelegaBot created by Itzkeeni

lasted bot version: 0.5.7

lasted mainer version: 0.1.1 Alpha

Bot url: web.telegram.org/z/#5609632846

Bot name: @GoodTelegaBot

Test bot: @GoodTelegaTestBot


The bot was created to learn Python, the development of the miner began in the bot
It will appear no earlier than 0.7.0 since it will be necessary to configure the database
Also, the code is posted without a miner, since it is still in development.</b>
</h3>

<h2 align="center">
</h2>

<h2 align="center">
  <b>   ⠀⠀  </b>

  <b>Libary used in code</b>
</h2>

```python
import telebot # Telegram APi
from urllib import response # Module for URL addres
import time # for delay
import requests # for HTTP-requests
from datatime import datatime # for time processing
```
<h2 align="center">
  <b>   ⠀⠀  </b>

  <b>Bot and API setup</b>
</h2>

```python
bot = telebot.TeleBot('TOKEN')
```
<h2 align="center">
  <b>   ⠀⠀  </b>

  <b>Text command</b>
</h2>

```python
@bot.message_handler(commands=["kirp"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Кирпич')
```
<h2 align="center">
  <b>   ⠀⠀  </b>

  <b>Sticker send</b>
</h2>

```python
@bot.message_handler(commands=["sticker"])
def start(m, res=False):
    stick = open('stick.webp', 'rb')
    bot.send_sticker(m.chat.id, stick) 
```

<h2 align="center">
  <b>   ⠀⠀  </b>

  <b>Image send</b>
</h2>

```python
@bot.message_handler(commands=["bebis"])
def start(m, res=False):
    photo = open('bebris.png', 'rb')
    bot.send_photo(m.chat.id, photo)
```
<h2 align="center">
  <b>   ⠀⠀  </b>

  <b>Bitcoin command</b>
</h2>

```python
@bot.message_handler(commands=["btc"])
def start(m, res=False):
    req = requests.get(url="https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()  
    sell_price = response["btc_usd"]["sell"]
    bot.send_message(m.chat.id, 'На момент:')
    bot.send_message(m.chat.id, f"{datetime.now().strftime('%Y.%m.%d %H:%M')}\n   \nЦена Биткоина: {sell_price}$")
```
<h2 align="center">
  <b>   ⠀⠀  </b>

  <b>Time command</b>
</h2>

```python 
@bot.message_handler(commands=["time"])
def start(m, res=False):    
    bot.send_message(m.chat.id, f"{datetime.now().strftime('%Y.%m.%d %H:%M')}") #Send to MSK time
```
<p align="center">
  <b>Other links: </b><br>
  <a href="https://www.youtube.com/channel/UCM6InRH22Xno8nywrZnbhLA">Youtube</a> |
  <a href="https://www.donationalerts.com/r/keenioff">Donate</a> |
  <a href="https://t.me/keenitelega">Telegram </a>|
  <a href="discord.gg/zn5usa2GAc">Discord</a>
  <br><br>
</p>
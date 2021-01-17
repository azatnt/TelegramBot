# This is a sample Telegram bot
# which will display weather in Uralsk
import telebot
import config
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://sinoptik.ua/погода-алматы')
bot = telebot.TeleBot(config.token)
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    desc = el.select('.wDescription .description')[0].text
    # print(t_min, t_max, desc)


@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, "Привет погода на сегодня:\n" +
                     t_min + ', ' + t_max + '\n' + desc)


if __name__ == '__main__':
    bot.polling(none_stop=True)
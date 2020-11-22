import telebot
import requests
import re
from bs4 import BeautifulSoup as bs


bot = telebot.TeleBot('')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        txt = "Hi! What do you want to find on Merriam-Webster"
        txt += " dictionary?"
        bot.send_message(message.from_user.id, txt)
    elif ' ' in message.text:
        txt = 'Enter only one word, pls'
        bot.send_message(message.from_user.id, txt)
    else:
        url = "https://www.merriam-webster.com/dictionary/"
        url += message.text
        r = requests.get(url)
        html = r.content
        soup = bs(html, "html.parser")
        text = 'Defenition of ' + str(message.text).capitalize() + ': '
        for meta in soup.find_all('meta'):
            prop = meta.get('property')
            if prop == 'og:description':
                text = text + str(meta.get('content'))
                text = text.replace('See the full definition', '')
                text += "\n\nExample of using in sentence:\n\n"
        for data in soup.find_all('span', class_='t has-aq'):
            text = text + ' ' + str(data) + '\n\n'
        mssg = message.from_user.id, re.sub(r'<.*?>', '', text)
        mssg = mssg.replace('</*>', '') + ' ' + url
        bot.send_message(mssg)


bot.polling(none_stop=True, interval=0)

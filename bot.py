import telebot
import requests
import re
from bs4 import BeautifulSoup as bs


bot = telebot.TeleBot('1327213027:AAGcwZpzOAqbXZCpfEnaoBwM5Ti7lEsQ86E')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
	if message.text == '/start':
		bot.send_message(message.from_user.id, "Hi! What do you want to find on Merriam-Webster dictionary?")
	elif ' ' in message.text:
		bot.send_message(message.from_user.id, 'Enter only one word, pls')
	else:
		url = "https://www.merriam-webster.com/dictionary/" + message.text
		r = requests.get(url)
		html = r.content
		soup = bs(html, "html.parser")
		for meta in soup.find_all('meta'):
			prop = meta.get('name')
			if prop == 'description':
				text = str(meta.get('content'))
		for data in soup.find_all('span', class_= 't has-aq'):
			text = text + ' ' + str(data)
		bot.send_message(message.from_user.id, re.sub(r'<.*?>','',text).replace('</*>','') + ' ' + url)

		

 
bot.polling(none_stop=True, interval=0)



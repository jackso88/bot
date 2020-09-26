import telebot

bot = telebot.TeleBot('1327213027:AAGcwZpzOAqbXZCpfEnaoBwM5Ti7lEsQ86E')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
	if message.text == '/start':
		bot.send_message(message.from_user.id, "Hi! What do you want to find on Merriam-Webster dictionary?")
	elif ' ' in message.text:
		bot.send_message(message.from_user.id, 'Enter only one word, pls')
	else:
		bot.send_message(message.from_user.id, 'https://www.merriam-webster.com/dictionary/' + message.text)

bot.polling(none_stop=True, interval=0)



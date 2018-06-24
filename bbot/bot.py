import telebot
from telebot import types
bot = telebot.TeleBot("520113254:AAGfDm2kSTwReFmqiJon4cUDe9kywdLc2D8")
@bot.message_handler(content_types=["text"])
def default_test(message):
 keyboard = types.InlineKeyboardMarkup(row_width=3)
 keyboard1 = types.InlineKeyboardMarkup(row_width=2)
 keyboard2 = types.InlineKeyboardMarkup(row_width=4)
 D=types.InlineKeyboardButton(text="Dota2 Channel", url="t.me/dota2bb")
 DD=types.InlineKeyboardButton(text="DaiSuda", url="t.me/DaiSuda")
 HS=types.InlineKeyboardButton(text="HS Channel", url="t.me/BlackBearsFireside")
 DC=types.InlineKeyboardButton(text="Dota2 Chat", url="t.me/dota2bbchat")
 IN=types.InlineKeyboardButton(text="Instagram", url="instagramm.com/DaiSuda.BB")
 HSC=types.InlineKeyboardButton(text="HS Chat", url="t.me/BlackBearsFiresideChat")
 FB=types.InlineKeyboardButton(text="FB", url="Fb.com/daisuda.bb")
 TW=types.InlineKeyboardButton(text="Twitter", url="twitter.com/daisuda_bb")
 VK=types.InlineKeyboardButton(text="VK", url="vk.com/DaiSuda_BB")
 keyboard.add(D,DD,HS,DC,HSC)
 keyboard2.add(FB,IN,TW,VK)
 if message.text == '/start':
   bot.send_message(message.chat.id, "Добрый день, Вас приветствует бот DaiSuda, выберите в меню интересующий Вас пункт и проводите время с интересом!", reply_markup=keyboard)
   bot.send_message(message.chat.id, "Мы в других социальных сетях:", reply_markup=keyboard2) 
if __name__ == '__main__':
     bot.polling(none_stop=True)

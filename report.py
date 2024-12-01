from path import hreport_key
from telebot.async_telebot import AsyncTeleBot
import asyncio
bot =  AsyncTeleBot(hreport_key)
from google_task import res
import pandas as pd
#shdlsd
from telebot import types
#global text

@bot.message_handler(commands=['start'])
async def send_welcom(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Xodimlar", callback_data='xodim'), row_width=1)
    markup.add(types.InlineKeyboardButton("Xizmat xati", callback_data='xat'), row_width=1)
    markup.add(types.InlineKeyboardButton("Buyruqlar", callback_data='buyruq'), row_width=1)
    text = "Hush kelibsiz! Ishni boshlash uchun quyidagilardan biri tanlang"
    await bot.send_message(message.chat.id, text, reply_markup=markup)



@bot.callback_query_handler(func=lambda xat: xat.data == 'xat')
async def get_xatlar(xat):
     await bot.send_message(xat.message.chat.id, "siz xizmatni kiriting... oxirgi 5 ta xarfni")


@bot.message_handler(content_types=['text'])
async def xat_message_handler(message):
    result = res[res['nomer'].str.len()>7]    
    
    text = result.loc[result['nomer'].str.endswith(message.text)]
    text = text[['nomer', 'Status','Natijasi']]
    text = text.reset_index(drop=True)
    text.index.rename('№', inplace=True)
    #result = res['nomer']
    await bot.reply_to(message, f"Sizning xizmat xatingiz: {text}")   


@bot.callback_query_handler(func=lambda call: call.data == 'xodim' )
async def callback(call):
    await bot.answer_callback_query(call.id, text="Thanks for clicked")

    xodimlar = ['Qodirov', "Nurmatov", 'Toshmatov', 'Madaminov', 'Abdusalomov','Mamarasulov']
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(xodimlar[0], callback_data="Qodirov A"))
    markup.add(types.InlineKeyboardButton(xodimlar[1], callback_data="Nurmatov E"))
    markup.add(types.InlineKeyboardButton(xodimlar[2], callback_data="Toshmatov F"))
    markup.add(types.InlineKeyboardButton(xodimlar[3], callback_data="Madaminov I"))
    markup.add(types.InlineKeyboardButton(xodimlar[4], callback_data="Abdusalomov J"))
    markup.add(types.InlineKeyboardButton(xodimlar[5], callback_data="Mamarasulov Sh"))
   
    await bot.send_message(call.message.chat.id, "xodimni tanlang",reply_markup=markup)
    #await bot.register_inline_handler(call, get_tasks)
    #get_tasks(call.message)



@bot.callback_query_handler(func= lambda call: True)
async def handle_callback_quer(call):
    xodimlar = res['javobgar'].values.tolist()
    xodimlar = list(set(xodimlar))
    xodim = call.data

    if xodim in xodimlar:    
            text = res.loc[res['javobgar'].str.contains(xodim)]
            text = text[['nomer', 'Status']]
            text = text.reset_index(drop=True)
            text.index.rename('№', inplace=True)
        
    #if call.data == 'Nurmatov E':
            await bot.send_message(call.message.chat.id, text=text)
    else:
       
       await bot.send_message(call.message.chat.id, "Bunday xodim bizda ishlamaydi.")


#@bot.callback_query_handler(func=lambda get_tasks: get_tasks.data=='Qodirov A')
#async def get_tasks(message):
    
#    await bot.send_message(message.message.chat.id, "siz qodirovni tanladiz")
    

    
    '''
    await bot.answer_callback_query(message.id, text="you selected ")
    try:
        javobgar = message.text.strip()
        
        #text = res.loc[res['javobgar'].str.contains(javobgar)]
        xodim = res['javobgar'].values.tolist()
        xodim = list(set(xodim))
        
        if javobgar in xodim:    
            text = res.loc[res['javobgar'].str.contains(javobgar)]
            text = text[['nomer', 'Status']]
            text = text.reset_index(drop=True)
            text.index.rename('№', inplace=True)
            
                            #print(text)
            await  bot.reply_to(message, text)

        else:
            await bot.send_message(message.chat.id, "Bu xodim bizda ishlamaydi")
    except: 
        javobgar = message.text.strip()
        
        #text = res.loc[res['javobgar'].str.contains(javobgar)]
        xodim = res['javobgar'].values.tolist()
        print(list(set(xodim)))
        await bot.send_message(message.chat.id, 'Qandaydir xatolik boldi !!!')
'''

#@bot.message_handler(func=lambda message: True)
#async def echo_mes(message):
 #   text = "I am echobot .\n just write something and I repeat it "
  #  await bot.reply_to(message, message.text)




asyncio.run(bot.polling())


import telebot
import config
import joi_parser
import random, re, time
import copy
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


def polling(chat_id_):
    global qest_array, SCORE, flag, urls, key, TRIGER_ASUKA, CONTENT, amvs
    try:
        key = random.choice(list(qest_array.keys()))
        random.shuffle(qest_array[key])
        items = [types.KeyboardButton(x) for x in qest_array[key]]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(*items)

        bot.send_message(chat_id_, key, parse_mode='html', reply_markup=markup)
        del qest_array[key]
    except Exception as error:
        flag = False
        key = None
        markup = types.ReplyKeyboardRemove()
        if SCORE <= len(config.question)//2:
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item3 = types.KeyboardButton("⏳ Restart")
            markup3.add(item3)
            bot.send_message(chat_id_, 'Твой результат {}/{} 👎🏻\n это мало поэтому я больше не покажу картинки  '.format(SCORE, len(config.question)), reply_markup=markup3)
            sti = open('static/fuck.webp', 'rb')
            bot.send_sticker(chat_id_, sti)
        elif SCORE == len(config.question):
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🖼 Попросить арт")
            item2 = types.KeyboardButton("🎬 Видео на YouTube")
            item3 = types.KeyboardButton("🎧 Музыка по теме")
            item4 = types.KeyboardButton("📆 Релиз Евангелион: 3.0+1.0")
            item5 = types.KeyboardButton("🎭 Про персонажей")
            item6 = types.KeyboardButton("🎶 AMV")
            item7 = types.KeyboardButton("📖 Книга")
            item8 = types.KeyboardButton("⏳ Restart")
            markup3.add(item1,item2,item3,item4,item5,item6,item7, item8)
            bot.send_message(chat_id_, 'Отличный результат {}/{}\nВижу ты разбираешься в теме'.format(SCORE, len(config.question)), reply_markup=markup3)
            sti = open('static/smile.webp', 'rb')
            bot.send_sticker(chat_id_, sti)
            urls = joi_parser.get_url()
            amvs = copy.copy(config.amv)
            CONTENT = True
        else:
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🖼 Попросить арт")
            item2 = types.KeyboardButton("🎬 Видео на YouTube")
            item3 = types.KeyboardButton("🎧 Музыка по теме")
            item4 = types.KeyboardButton("📆 Релиз Евангелион: 3.0+1.0")
            item5 = types.KeyboardButton("🎭 Про персонажей")
            item6 = types.KeyboardButton("🎶 AMV")
            item7 = types.KeyboardButton("📖 Книга")
            item8 = types.KeyboardButton("⏳ Restart")
            markup3.add(item1,item2,item3,item4,item5,item6,item7, item8)
            bot.send_message(chat_id_, 'Твой результат {}/{} \nЭтого достаточно что бы иметь возможность смотреть контент по NGE'.format(SCORE, len(config.question)), reply_markup=markup3)
            urls = joi_parser.get_url()
            amvs = copy.copy(config.amv)
            CONTENT = True
        SCORE = 0
        TRIGER_ASUKA = 0

def polling_function(chat_id_):
    global qest_array, SCORE, flag, TRIGER_ASUKA
    sti = open('static/polling.webp', 'rb')
    bot.send_sticker(chat_id_, sti)

    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(chat_id_, "Сейчас я задам тебе ряд вопросов по результатам которых\nЯ решу стоит ли продолжать общение ", reply_markup=markup)
    qest_array = copy.deepcopy(config.question)
    SCORE = 0
    TRIGER_ASUKA = 0 
    flag = True
    time.sleep(1)
    polling(chat_id_)

def hangman(chat_id_):
    global k
    k = random.choice(list(hungman_array.keys()))
    bot.send_photo(chat_id_, open(hungman_array[k][1], 'rb'))
    bot.send_message(chat_id_, "Вопрос: "+hungman_array[k][0]+'\nОтвет: '+hungman_array[k][2]+'\nЖизни: '+''.join( ['❤️' for _ in range(LIVE)] ))
    del hungman_array[k]

def hangman_function(chat_id_):
    global HANGMAN_FLAG, urls, CONTENT, amvs
    number = len(config.hungman_questions) - (len(hungman_array) - 1)
    if number <= len(config.hungman_questions):
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        item = types.InlineKeyboardButton("Показать", callback_data='yes_')
        markup1.add(item)
        bot.send_message(chat_id_, "Вопрос №{}".format(number), reply_markup=markup1)
    else:
        if LIVE == config.number_of_lives:
            sti = open('static/asuka_smile.webp', 'rb')
            bot.send_sticker(chat_id_, sti)
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🖼 Попросить арт")
            item2 = types.KeyboardButton("🎬 Видео на YouTube")
            item3 = types.KeyboardButton("🎧 Музыка по теме")
            item4 = types.KeyboardButton("📆 Релиз Евангелион: 3.0+1.0")
            item5 = types.KeyboardButton("🎭 Про персонажей")
            item6 = types.KeyboardButton("🎶 AMV")
            item7 = types.KeyboardButton("📖 Книга")
            item8 = types.KeyboardButton("⏳ Restart")
            markup3.add(item1,item2,item3,item4,item5,item6, item7, item8)
            bot.send_message(chat_id_, 'Ты сохранил все жизни 👍🏻\nЖизни : {}\nа это значит что ты ответил на все вопроси\nи похоже у тебя совсем нет личной жизни\nНу ничего, зато теперь ты можешь увидеть больше контента по NGE'.format(''.join( ['❤️' for _ in range(LIVE)] )), reply_markup=markup3 )
            HANGMAN_FLAG = False
            CONTENT = True
            urls = joi_parser.get_url()
            amvs = copy.copy(config.amv)
        else:
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🖼 Попросить арт")
            item2 = types.KeyboardButton("🎬 Видео на YouTube")
            item3 = types.KeyboardButton("🎧 Музыка по теме")
            item4 = types.KeyboardButton("📆 Релиз Евангелион: 3.0+1.0")
            item5 = types.KeyboardButton("🎭 Про персонажей")
            item6 = types.KeyboardButton("🎶 AMV")
            item7 = types.KeyboardButton("📖 Книга")
            item8 = types.KeyboardButton("⏳ Restart")
            markup3.add(item1,item2,item3,item4,item5,item6,item7, item8)
            bot.send_message(chat_id_, 'Ладно вижу ты знаком с темой\nТвои жизни: '+''.join( ['❤️' for _ in range(LIVE)] ), reply_markup=markup3)
            HANGMAN_FLAG = False
            CONTENT = True
            urls = joi_parser.get_url()
            amvs = copy.copy(config.amv)

        
#@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda msg: msg.text == '/start' or msg.text == '⏳ Restart')
def welcome(message):
    global used_art, flag, GLOBAL_FLAG, HANGMAN_FLAG, SOME_FLAG, ANOTHER_FLAG, CONTENT
    flag = False
    HANGMAN_FLAG = False
    GLOBAL_FLAG = True
    SOME_FLAG = True
    ANOTHER_FLAG = False
    CONTENT = False
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    used_art = [x for x in range(1, config.NUMBER_ART + 1)]

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎨 Попросить арт")
    item2 = types.KeyboardButton("😊 Привет, как дела?")
    item3 = types.KeyboardButton("⏳ Restart")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, лучшая девочка в аниме Neon Genesis Evangelion.\nОбращайся со мной почтительно и может быть ты заслужишь мое расположение.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text in config.content_button )
def content_button_function(message):
    global CONTENT, amvs
    if CONTENT:
        if message.chat.type == 'private':
            if message.text == "🎬 Видео на YouTube":
                markup1 = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton("Английский", callback_data='eng')
                item1 = types.InlineKeyboardButton("Русский", callback_data='rus')
                item2 = types.InlineKeyboardButton("Я понимаю оба", callback_data='both')
                markup1.add(item, item1, item2)
                bot.send_message(message.chat.id, "Отличные разборы для тех кто не понял, и тех кто думает что понял всю глубину замысла создателей Евангелиона\nВыбери язык на котором удобно смотреть", reply_markup=markup1)
            elif message.text == "🎧 Музыка по теме":
                markup1 = types.InlineKeyboardMarkup(row_width=2)
                item = types.InlineKeyboardButton("Треки", callback_data='tracks')
                item1 = types.InlineKeyboardButton("Альбомы", callback_data='album')
                markup1.add(item, item1)
                bot.send_message(message.chat.id, "Евангелион оказал значительное культурное влияние не только на Японию\nно и вышел далеко за её пределы, люди по разномы трактуют её смыслы и воплощают их в песни", reply_markup=markup1)
            elif message.text == "📆 Релиз Евангелион: 3.0+1.0":
                bot.send_message(message.chat.id, "Премьера 27.06.2020 года")
            elif message.text == "🎭 Про персонажей":
                bot.send_message(message.chat.id, "https://evangelion.fandom.com/ru/wiki/%D0%9F%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B8_(%D0%BF%D0%BE%D1%80%D1%82%D0%B0%D0%BB)")
            elif message.text == "🎶 AMV":
                try:
                    amv_ = random.choice(amvs)
                    bot.send_message(message.chat.id, amv_)
                    del amvs[amvs.index(amv_)]
                except Exception as erro:
                    bot.send_message(message.chat.id, 'Это все что я могу показать')
            elif message.text == "📖 Книга":
                bot.send_message(message.chat.id, "https://www.amazon.com/Beautiful-Fighting-Girl-Saito-Tamaki/dp/0816654514")
            else:
                sti = open('static/something_went_wrong.webp', 'rb')
                bot.send_sticker(message.chat.id, sti)
                bot.send_message(message.chat.id, "Если ты это видишь значит что-то пошло не так ")

@bot.message_handler(func=lambda msg: msg.text == 'Начать' )
def test_test(message):
    if message.chat.type == 'private':
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        item = types.InlineKeyboardButton("Хорошо", callback_data='start_')
        item1 = types.InlineKeyboardButton("Нет", callback_data=random.choice(['no','bad']))
        markup1.add(item, item1)
        bot.send_message(message.chat.id, "Сейчас мы сыграем в игру \nПравила очень простые, я задаю вопрос,\nа ты должен написать ответ за определенное время (15 сек.)\nПример: Главный герой Евангелиона - С._._.Д._._\nТы должен написать СИНДЗИ / синдзи\nЕсли не успеваешь за отведенное время\nтеряешь одну из 5 жизней ❤️".format(message.from_user), reply_markup=markup1)
        
            
@bot.message_handler(content_types=['text'])
def speak_function(message):
    global used_art, SCORE, flag, urls, key, TRIGER_ASUKA, GLOBAL_FLAG, HANGMAN_FLAG, LIVE, SOME_FLAG
    if GLOBAL_FLAG:
        if message.chat.type == 'private':
            if message.text == "🎨 Попросить арт":
                try:
                    num = random.choice(used_art)
                    used_art.remove(num)
                    if num == 5:
                        path = 'static/asuka_art/art'+str(num)+'.png'
                        art = open(path, 'rb')
                        bot.send_photo(message.chat.id, art)
                        bot.send_message(message.chat.id, "Ой 😓😌 как это сюда попало")
                    else:
                        path = 'static/asuka_art/art'+str(num)+'.png'
                        art = open(path, 'rb')
                        bot.send_photo(message.chat.id, art)
                    print(used_art)
                except IndexError:
                    sti = open('static/irritation.webp', 'rb')
                    bot.send_sticker(message.chat.id, sti)

                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True ,one_time_keyboard=True)
                    item3 = types.KeyboardButton("Как мне увидеть еще картинки?")
                    markup.add(item3)
                    bot.send_message(message.chat.id, "Хватит с тебя ", reply_markup=markup)

            elif message.text == "Как мне увидеть еще картинки?":
                markup1 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
                item2 = types.InlineKeyboardButton("Не хочу", callback_data='bad')

                markup1.add(item1, item2)

                bot.send_message(message.chat.id, "Можешь ответить на несколько вопросов", reply_markup=markup1)

            elif message.text == "😊 Привет, как дела?":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item = types.KeyboardButton("🎨 Попросить арт")
                item1 = types.KeyboardButton("Можешь рассказать больше о себе 😅")
                item3 = types.KeyboardButton("⏳ Restart")
                markup.add(item, item1, item3)
                bot.send_message(message.chat.id, "Как банально... Ну привет", reply_markup=markup)

            #elif message.text in reduce(lambda x,y: x+y, list(config.question.values())):
            elif flag:
                if message.text in config.question[key]:
                    #print (key, message.text, config.question[key][0], config.question[key])
                    if message.text == config.question[key][0]:
                        SCORE += 1
                        bot.send_message(message.chat.id, random.choice(config.good_phrase))
                    else:
                        bot.send_message(message.chat.id, '...👊🏻')
                    polling(message.chat.id)
                else:
                    bot.send_message(message.chat.id, "Я не знаю что ответить, бака 😢")

            elif flag and message.text not in config.question[key]:
                if TRIGER_ASUKA == 0:
                    bot.send_message(message.chat.id, 'Выбери ответ из представленных вариантов')
                    TRIGER_ASUKA += 1
                elif TRIGER_ASUKA == 1:
                    bot.send_message(message.chat.id, 'Слушай, ты что дурак? Используй только варианты которые я предлагаю 😠')
                    TRIGER_ASUKA += 1
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item3 = types.KeyboardButton("⏳ Restart")

                    markup.add(item3)
                    bot.send_message(message.chat.id, 'Знаешь что, раз тебе так весело писать случайный текст 😡\n так делай это и дальше но уже без меня 😤', reply_markup = markup)
                    flag = False
                    GLOBAL_FLAG = False

            elif message.text == "Можешь рассказать больше о себе 😅":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton("⏳ Restart")
                markup.add(item3)
                bot.send_message(message.chat.id, 'Я лучший пилот Евангелиона, мне нет равных.\n ', reply_markup = markup)
                    
                markup1 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Конечно", callback_data='yes')
                item2 = types.InlineKeyboardButton("Нет", callback_data='no')

                markup1.add(item1, item2)

                bot.send_message(message.chat.id, "Хочешь узнать больше? тогда докажи что ты тоже на что-то способен\n", reply_markup=markup1)


            elif HANGMAN_FLAG:
                if message.text.replace(' ', '').lower() == k:
                    bot.send_message(message.chat.id, random.choice(config.good_phrase))
                    HANGMAN_FLAG = False
                    SOME_FLAG = True
                else:
                    HANGMAN_FLAG = False
                    SOME_FLAG = True
                    LIVE -= 1
                    bot.send_message(message.chat.id, '💔')
                    
            elif message.text == "🖼 Попросить арт":
                try:
                    print (len(urls))
                    #random.shuffle(urls)
                    bot.send_message(message.chat.id, urls.pop())
                except IndexError:
                    urls = joi_parser.get_url("/"+str(config.PAGE))
                    config.PAGE -= 1
                    #random.shuffle(urls)
                    bot.send_message(message.chat.id, urls.pop())
            else:
                bot.send_message(message.chat.id, "Я не знаю что ответить, бака 😢")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и хорошо')
                polling_function(call.message.chat.id)
            elif call.data == 'bad':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item = types.KeyboardButton("🎨 Попросить арт")
                item1 = types.KeyboardButton("Можешь рассказать больше о себе 😅")
                item3 = types.KeyboardButton("⏳ Restart")
                markup.add(item, item1, item3)
                bot.send_message(call.message.chat.id, 'Как хочешь', reply_markup=markup)
            elif call.data == 'yes':
                markup1 = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton("Хорошо", callback_data='start_')
                #item1 = types.InlineKeyboardButton("Нет", callback_data=random.choice(['no','bad']))
                markup1.add(item)
                #bot.send_message(message.chat.id, "Сейчас мы сыграем в игру \nПравила очень простые, я задаю вопрос,\nа ты должен написать ответ за определенное время (15 сек.)\nПример: Главный герой Евангелиона - С._._.Д._._\nТы должен написать СИНДЗИ / синдзи\nЕсли не успеваешь за отведенное время\nтеряешь одну из 5 жизней ❤️".format(message.from_user), reply_markup=markup1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text="Сейчас мы сыграем в игру \nПравила очень простые, я задаю вопрос,\nа ты должен написать ответ за определенное время (15 сек.)\nПример: Главный герой Евангелиона - С._._.Д._._\nТы должен написать СИНДЗИ / синдзи\nЕсли не успеваешь за отведенное время\nтеряешь одну из 5 жизней ❤️".format(call.message.from_user), reply_markup=markup1)

            elif call.data == 'no':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text='Ну и ладно', reply_markup=None)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item = types.KeyboardButton("🎨 Попросить арт")
                item1 = types.KeyboardButton("Можешь рассказать больше о себе 😅")
                item3 = types.KeyboardButton("⏳ Restart")
                markup.add(item, item1, item3)
                #bot.send_message(call.message.chat.id, "Ну и Ладно", reply_markup=markup)
                sti = open('static/reaction.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti, reply_markup=markup)
            elif call.data == 'start_':
                global HANGMAN_FLAG, hungman_array, LIVE, SOME_FLAG, ANOTHER_FLAG
                for x in range(2, 0, -1):
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text=str(x), reply_markup=None)
                    time.sleep(1)

                HANGMAN_FLAG = False
                SOME_FLAG = False
                ANOTHER_FLAG = True
                LIVE = config.number_of_lives
                hungman_array = copy.copy(config.hungman_questions)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text='START', reply_markup=None)
                #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='START')
                hangman_function(call.message.chat.id)
            elif call.data == 'yes_':
                hangman(call.message.chat.id)
                HANGMAN_FLAG = True
                SOME_FLAG = False
                for x in range(15, -1, -1):
                    if SOME_FLAG:
                        break
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text='⏱ '+str(x), reply_markup=None)
                    #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=str(x))
                    time.sleep(1)
                if ANOTHER_FLAG:
                    if x == 0:
                        LIVE -= 1
                        bot.send_message(call.message.chat.id, '💔')
                        if LIVE == 0:
                            HANGMAN_FLAG = False
                            bot.send_message(call.message.chat.id, 'Game Over')
                            #bot.answer_callback_query(callback_query_id=call.message.chat.id, show_alert=False, text='Game Over')
                        else:
                            hangman_function(call.message.chat.id)
                    else:
                        hangman_function(call.message.chat.id)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text='', reply_markup=None)

            elif call.data == 'eng':
                for video in config.eva_videos_eng:
                    bot.send_message(chat_id=call.message.chat.id, text=video)
            
            elif call.data == 'rus':
                for video in config.eva_videos_rus:
                    bot.send_message(chat_id=call.message.chat.id, text=video)   
            
            elif call.data == 'both':
                for video in config.eva_videos_eng + config.eva_videos_rus:
                    bot.send_message(chat_id=call.message.chat.id, text=video)   

            elif call.data == 'tracks':
                for track in config.eva_tracks:
                    audio = open(track, 'rb')
                    bot.send_audio(call.message.chat.id, audio)

            elif call.data == 'album':
                for alb in config.albums:
                    bot.send_message(chat_id=call.message.chat.id, text=alb)
            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #    text="Можешь ответить на несколько вопросов", reply_markup=None)

            # show alert
                #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='START')
                            
    except Exception as error:
        print(repr(error))

# RUN
bot.polling(none_stop=True)


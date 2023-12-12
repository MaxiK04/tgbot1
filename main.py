import telebot
from telebot import types
from telebot.types import InputMedia

photo_url = 'https://www.ystu.ru/upload/iblock/123/13sj41of6u5r83r7aam4stp5ej7z4ad2/DSC_3320.JPG'
photo_url1 = 'https://www.ystu.ru/upload/iblock/cae/pryhh8khnyf4pua6s6qahxfijdnvibgt/xb896535a271646742c2a947855036997_1000.jpg.pagespeed.ic.Ph3OZ7X_p9.jpg'
photo = '/img/1.jpg'

bot = telebot.TeleBot('6825371641:AAH6vlXvmneuJqFfiEwzrDtn0EokwJBUJz4')

@bot.message_handler    (commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте,{message.from_user.first_name}. Рады вас видеть. '
                                      'Мы готовы провести замечательную экскурсию по '
                                      'нашему музею ЯГТУ. Ваш помощник - <em> <b>/help </b> </em>', parse_mode='html')

@bot.message_handler    (commands=['help'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="История музея",callback_data="history")
    markup.row(but_1)
    but_2 = types.InlineKeyboardButton(text="Экскурсия по музею",callback_data="exs")
    markup.row(but_2)
    but_3 = types.InlineKeyboardButton(text="Оставить отзыв",callback_data="back")
    but_4 = types.InlineKeyboardButton(text="Наша группа ВКонтакте",
                                       url='https://vk.com/public170798088')
    markup.row(but_3,but_4)
    but_5 = types.InlineKeyboardButton(text="Информация", callback_data="info")
    markup.row(but_5)
    but_6 = types.InlineKeyboardButton(text="Значимые личности ЯГТУ", callback_data="people")
    markup.row(but_6)
    key.add(but_1, but_2, but_3, but_4,but_5,but_6)
    bot.send_message(message.chat.id, "Навигация", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'history':
        bot.send_photo(callback.message.chat.id, photo=photo_url1, caption = 'В 1944 году в Ярославле был создан технологический институт резиновой промышленности.'
                                                                             ' Директором вуза тогда был назначен Евгений Васильевич Мигулин. '
                                                                             'В кратчайшие сроки были образованы первые кафедры, собрано необходимое оборудование для лабораторий и произведен ремонт. В 1946 году институт из Министерства резиновой промышленности передали в ведение высшего образования СССР.'
                                                                             'В апреле 1948 в вузе прошла первая студенческая конференция. '
                                                                             'Первый выпуск специалистов состоялся в 1949 году. В 1950 году в вузе было открыто вечернее отделение. '
                                                                             'В 1953 году вуз был преобразован в технологический.Вуз сделал значительный шаг в оснащении кафедр новым оборудованием, расширил перечень специальностей, увеличил контингент студентов. '
                                                                             )
    elif callback.data == 'back':
        bot.send_message(callback.message.chat.id, f'Пожалуйста, оставьте свой отзыв - это поможет сделать нас лучше и ещё больше людей узнают о музее ЯГТУ')
    elif callback.data == 'exs':
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)

        but_6 = types.KeyboardButton(text="Общий вид музея")

        but_7 = types.KeyboardButton(text="Секция 1")
        but_8 = types.KeyboardButton(text="Секция 2")
        but_9 = types.KeyboardButton(text="Секция 3")
        but_10 = types.KeyboardButton(text="ГЕНПЛАН Политеха")
        but_11 = types.KeyboardButton(text="Первые достижения")




        markup.add(but_6,but_7,but_8,but_9,but_10,but_11)
        bot.send_message(callback.message.chat.id, "Пожалуйста, выберите из меню(снизу) то что вы бы хотели увидеть", reply_markup=markup)
    elif callback.data == 'info':
        bot.send_photo(callback.message.chat.id, photo=photo_url, caption = f'Расписание и расположение музея \n Музей располагается по адресу Московский проспект, 88, Ярославль в А корпусе ЯГТУ. Попасть в него можно придупредив(связаться) с Поповым  Романом Игоревичем.' )
    elif callback.data == 'people':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but_12 = types.KeyboardButton(text="Значимые личности ЯГТУ(Часть 1)")
        but_13 = types.KeyboardButton(text="Значимые личности ЯГТУ(Часть 2)")
        markup.add(but_12,but_13)
        bot.send_message(callback.message.chat.id,"Пожалуйста выберите из меню",  reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Общий вид музея':
            bot.send_photo(message.chat.id, photo=open('1.jpg', 'rb'),
                       caption='Представляет вашему вниманию общий вид на экспонаты')
        elif message.text == 'Секция 1':
            bot.send_photo(message.chat.id, photo=open('1.1.jpg', 'rb'), caption='Первая секция')
        elif message.text == 'Секция 2':
            bot.send_photo(message.chat.id, photo=open('2.jpg', 'rb'), caption='Вторая секция')
        elif message.text == 'Секция 3':
            bot.send_photo(message.chat.id, photo=open('3.jpg', 'rb'), caption='Третья секция')
        elif message.text == 'ГЕНПЛАН Политеха':
            bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('4.jpg', 'rb'),caption='ГЕНПЛАН Политеха'),
                                                   telebot.types.InputMediaPhoto(open('5.jpg', 'rb'))])
        elif message.text == 'Первые достижения':
            bot.send_media_group(message.chat.id,
                                 [telebot.types.InputMediaPhoto(open('6.jpg', 'rb'), caption='Первые достижения'),
                                  telebot.types.InputMediaPhoto(open('7.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('7.jpg', 'rb'))])
        elif message.text == 'Значимые личности ЯГТУ(Часть 1)':
            bot.send_media_group(message.chat.id,
                                 [
                                  telebot.types.InputMediaPhoto(open('11.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('12.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('13.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('14.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('15.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('16.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('17.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('18.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('19.jpg', 'rb'))])
        elif message.text == 'Значимые личности ЯГТУ(Часть 2)':
            bot.send_media_group(message.chat.id,
                                 [telebot.types.InputMediaPhoto(open('10.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('21.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('22.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('23.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('24.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('25.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('26.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('27.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('28.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('29.jpg', 'rb'))])



bot.polling(none_stop=True)
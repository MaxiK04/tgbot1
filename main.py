import telebot
from telebot import types
import math
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMedia

photo_url = 'https://www.ystu.ru/upload/iblock/123/13sj41of6u5r83r7aam4stp5ej7z4ad2/DSC_3320.JPG'
photo_url1 = 'https://www.ystu.ru/upload/iblock/cae/pryhh8khnyf4pua6s6qahxfijdnvibgt/xb896535a271646742c2a947855036997_1000.jpg.pagespeed.ic.Ph3OZ7X_p9.jpg'
photo = '/img/1.jpg'


bot = telebot.TeleBot('6825371641:AAH6vlXvmneuJqFfiEwzrDtn0EokwJBUJz4')



@bot.message_handler(commands=['people'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    key = types.InlineKeyboardMarkup()
    but_6 = types.InlineKeyboardButton(text="Научный полк ЯГТУ", callback_data="people")
    markup.row(but_6)
    key.add(but_6)
    bot.send_message(message.chat.id, "Научный полк ЯГТУ", reply_markup=markup)
@bot.message_handler(commands=['help'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="История музея", callback_data="history")
    markup.row(but_1)
    but_2 = types.InlineKeyboardButton(text="Экскурсия по музею", callback_data="exs")
    markup.row(but_2)
    but_3 = types.InlineKeyboardButton(text="Оставить отзыв", callback_data="back")
    but_4 = types.InlineKeyboardButton(text="Наша группа ВКонтакте", url='https://vk.com/public170798088')
    markup.row(but_3, but_4)
    but_5 = types.InlineKeyboardButton(text="Информация", callback_data="info")
    markup.row(but_5)
    key.add(but_1, but_2, but_3, but_4, but_5)
    bot.send_message(message.chat.id, "Навигация", reply_markup=markup)

people_data  = [
{
"name": "Белозёров Николай Вячеславович(1913)",
"photo": "IMAGES/1.png",
"description": "Родился в г.Ярославле. Трудовую деятельность начал в 1930 году. В 1939г. закончил с отличием Ленинградский химико-технологический институт им.Ленсовета.В 1940г. призван в ряды Красной Армии.Принимал участие в боевых действиях на Юго-Западном фронте в должности командира взвзода, затем командира отдельной огеметной роты."
               "При выходе из окружения попал в плен. С 1946 года работал преподавателем Ярославского техникума резиновой промышленности."
              "В ЯТИ с 1960г.- старший преподаватель, доцент. Кандидат технических наук, доцент, автор более 20 научных и методических работ, в том числе учебник Технология резины"
             "Награждён оредном Отечественной войны, медалью 'За Победу над Германией', юбилейными медалями."
},
{
'name': 'Камерилова Зоя Ивановна(1924-1997)',
'photo': 'IMAGES/2.png',
'description': "Родилась в Московской области. Закончила 10 классов. затем педагогические курсы, работала в средней школе.После окончания школы связи в 1941г. учавствовала в боевых действиях на Калининградском фронте в должности связиста-телефониста. Была тяжело ранена. До 1950 года находилась на инвалидности."
               "Затем работала в Ярославской областной библиотеке старшим библиотекарем. В ЯТИ с 1956 г. лаборант, старший библиотекарь, заведующая сектором."
               "Будучи на пенсии (с 1983г.) продолжала активно участвовать в военно-патриотическом воспитании студентов. Член клуба (Прометей) ЯПИ, городского и районного Советов ветеранов."
               "Награждена медалью Ветеран труда, знаками 25 лет Советского комитета войны и Ветеран труда ЯПИ."
},
{
'name': 'Пузанов Сергей Николаевич (1914-1982)',
'photo': 'IMAGES/3.png',
'description': "Родился в крестьянской семье в 1914г. С 1936г. по 1960г. - кадровый военный. Участник ВОВ. Стрелок-радист дальней бомбардировочной авиации. "
               "Первый боевый вылет совершил 22 июня 1941г, бомбил Кенингсберг. Работал в ЯТИ до 1976 года инспектором отдела кадров. Скончался в 1982 году."
               "Награждён двумя орденами Красного Знамени, тремя ореднами Красной Звезды, орденом Отечественной войны, боевыми и юбилейными медалями."
},
{
"name" : "Жуков Михаил Петрович (1905-1984)",
"photo" : "IMAGES/4.png",
"description" : "Трудовую деятельность начал в 1924 году чертёжником на фабрике (Красный Перекоп). После окончания Ленинградского Индустриального института (1936г.) работал на"
                                                                                                "Яросласком заводе (Красный Маяк) инженером-электриком, одновременно преподавал курс электротехники в Ярославском педагогическом институте (до 1941г.)."
                                                                                                                                "В ЯТИ с 1946г. - ассистент, старший преподаватель, зав. кафедрой, доцент. Неоднократно избирался в местком института, был его первым председателем. Автор нескольких научных публикаций и методических пособий."
                                                                                                                                "Награждён двумя орденами Отечественной войны, медалями (За оборону Сталинграда), (За победу над Германией), юбилейными медалями."
},
{
"name" : "Сизов Василий Николаевич (р.1925)",
"photo" : "IMAGES/5.png",
"description" : "Родился в Вологодской области. После окончания 9 классов средней школы поступил в Аэроклуб. В 1943г. призван в ряды Советсвкой Армии, закончил полковую школу и был направлен на фронт."
                "Принимал участие в боевых действиях до сентября 1944г., затем был направлен на учёбу в военное училище. В ЯТИ работал с 1970 по 1990гг. в должностях: механика опытных установок, инженер группы КИП, инженер компрессорной установки, слесарь ОМГ."
                "Награждён орденом Отечественной войны, медалями (За Отвагу), (За Победу над Германией), юбилейными медалями."
},
{
"name" : "Калашников Сергей Сергеевич (р.1924)",
"photo" : "IMAGES/6.png",
"description" : "Закончил артиллерийское училище. Принимал участие в боевых действиях на 1-ом Прибалтийском фронте в составе отдельного истребительного противотанкового дивизиона. Командир взвода. Был тяжело ранен. Инвалид ВОВ."
                "1946-1955гг. - студент , аспирант Московского государственного экономического института. На преподавательской работе с 1955 г. В ЯТИ с 1966г., преподаватель, доцент, секретарь парткома, член бюро РК КПСС, завкафедрой политэкономии, кандидат экономических наук, доцент, автор более 50 научных работ."
                "Награждён орденом Красного Знамени, тремя орденами Отечественной войны, юоевыми и юбилейными медалями."
},
{
"name" : "Андреев Юрий Иванович (р.1922)",
"photo" : "IMAGES/7.png",
"description" : "Трудовую деятельность начал в 1938г. учеником на ст.Всполье, затем работал электромонтёром в паровозном депо ст.Ярославль. Принимал участие в боевых действиях на Украинском фронте."
                "В ЯТИ с 1958г., высококлассный специалист-слесарь, рационализатор и изобретатель. На пенсии с 1972."
                "Награждён орденом Отечественной войны, медалью (За Победу над Германией), юбилейными медалями."
},
{
"name" : "Новиков Николай Михайлович (1921-1991)",
"photo" : "IMAGES/8.png",
"description" : "Родился в Смоленской области в семье крестьянина. Кадровый военный, капитан запаса. Закончил Вольское военное авиационное  техническое училище."
                "В Советской Армии с 1940 по 1966гг. В 1952-1953гг. находился в специальной командировке в Китае. В ЯТИ с 1966 по 1991 гг. Работал заведующим лаборатории кафедры теоретической механики и сопротивления"
                "материалов, затем учебным мастером кафедры сопротивления материалов."
                "Награждён орденом Красной Звезды, двумя медалями (За боевые заслуги), (За Победу над Германией), юбилейными медалями"
},
{
"name" : "Соловьёв Валентин Самсонович (р.1918)",
"photo" : "IMAGES/9.png",
"description" : "После окончания школы работал токарем. В 1939г. призван в РККА. Принимал участие в боевых действиях в составе Особого Белорусского округа, Волховского, Ленинградского, Карельского и 1-ого Белорусского фронтов."
                "С 1958 по 1998г. до ухода на пенсию работал механиком кафедры химической технологии органических веществ ЯГТУ. "
                "Награждён орденом Отечественной войны, двумя медалями (За боевые заслуги), (За взятие Берлина), другими боевыми и юбилейными медалями."
},
{
"name": "Name",
"photo": "0.jpg",
"description": "Description"
},
{
"name": "Name",
"photo": "0.jpg",
"description": "Description"
},
]

import math

current_page = 1


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    per_page = 8  # количество элементов на странице
    global current_page  # объявление переменной как глобальной

    if callback.data == 'people':
        # код для отображения первой страницы
        markup = types.InlineKeyboardMarkup(row_width=1)
        people_buttons = []

        for person in people_data[(current_page - 1) * per_page:current_page * per_page]:
            button = types.InlineKeyboardButton(text=person['name'], callback_data=person['name'])
            people_buttons.append(button)

        markup.add(*people_buttons)

        if current_page < math.ceil(len(people_data) / per_page):
            markup.add(types.InlineKeyboardButton(text="️Следующая страница", callback_data='next_page'))

        if current_page > 1:
            markup.add(types.InlineKeyboardButton(text=" Вернуться назад", callback_data='go_back'))

        bot.send_message(callback.message.chat.id, "Выберите человека из научного полка:", reply_markup=markup)

    elif callback.data == 'next_page':
        current_page += 1

        if current_page > math.ceil(len(people_data) / per_page):
            current_page = math.ceil(len(people_data) / per_page)

        # код для отображения страницы с переключенными данными
        markup = types.InlineKeyboardMarkup(row_width=1)
        people_buttons = []

        for person in people_data[(current_page - 1) * per_page:current_page * per_page]:
            button = types.InlineKeyboardButton(text=person['name'], callback_data=person['name'])
            people_buttons.append(button)

        markup.add(*people_buttons)

        if current_page < math.ceil(len(people_data) / per_page):
            markup.add(types.InlineKeyboardButton(text="️Следующая страница", callback_data='next_page'))

        if current_page > 1:
            markup.add(types.InlineKeyboardButton(text=" Вернуться назад", callback_data='go_back'))

        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=markup)



    elif callback.data == 'go_back':
        current_page -= 1
        if current_page > math.ceil(len(people_data) / per_page):
            current_page = math.ceil(len(people_data) / per_page)

        # код для отображения страницы с переключенными данными
        markup = types.InlineKeyboardMarkup(row_width=1)
        people_buttons = []

        for person in people_data[(current_page - 1) * per_page:current_page * per_page]:
            button = types.InlineKeyboardButton(text=person['name'], callback_data=person['name'])
            people_buttons.append(button)

        markup.add(*people_buttons)

        if current_page < math.ceil(len(people_data) / per_page):
            markup.add(types.InlineKeyboardButton(text="️Следующая страница", callback_data='next_page'))

        if current_page > 1:
            markup.add(types.InlineKeyboardButton(text=" Вернуться назад", callback_data='go_back'))

        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    else:
        for person in people_data:
            if callback.data == person['name']:
                bot.send_photo(callback.message.chat.id, photo=open(person['photo'], 'rb'),
                               caption=person['description'])
                break

    if callback.data == 'history':
        bot.send_photo(callback.message.chat.id, photo=photo_url1, caption='+текст про историю музея')
    elif callback.data == 'back':
        bot.send_message(callback.message.chat.id, f'Пожалуйста, оставьте свой отзыв - это поможет сделать нас лучше и ещё больше людей узнают о музее ЯГТУ')
    elif callback.data == 'exs':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but_6 = types.KeyboardButton(text="Общий вид музея")
        but_7 = types.KeyboardButton(text="Секция 1(1945-1953)")
        but_8 = types.KeyboardButton(text="Секция 2(1953-1973)")
        but_9 = types.KeyboardButton(text="Секция 3(1973-1994)")
        but_10 = types.KeyboardButton(text="Три ГЕНПЛАНА Политеха")

        but_11 = types.KeyboardButton(text="Первые достижения")
        markup.add(but_6,but_7,but_8,but_9,but_10,but_11)
        bot.send_message(callback.message.chat.id, "Пожалуйста, выберите из меню(снизу) то что вы бы хотели увидеть", reply_markup=markup)
    elif callback.data == 'info':
        bot.send_photo(callback.message.chat.id, photo=photo_url, caption = f'Расписание и расположение музея \n Музей располагается по адресу Московский проспект, 88, Ярославль в А корпусе ЯГТУ. Попасть в него можно придупредив(связаться) с Поповым  Романом Игоревичем.' )



@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Общий вид музея':
            bot.send_photo(message.chat.id, photo=open('1.jpg', 'rb'),
                       caption='Представляет вашему вниманию общий вид на экспонаты')
        elif message.text == 'Секция 1(1945-1953)':
            bot.send_photo(message.chat.id, photo=open('1.1.jpg', 'rb'), caption='Первая секция')
        elif message.text == 'Секция 2(1953-1973)':
            bot.send_photo(message.chat.id, photo=open('2.jpg', 'rb'), caption='Вторая секция')
        elif message.text == 'Секция 3(1973-1994)':
            bot.send_photo(message.chat.id, photo=open('3.jpg', 'rb'), caption='Третья секция')
        elif message.text == 'Три ГЕНПЛАНА Политеха':
            bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('4.jpg', 'rb'),caption='ГЕНПЛАН Политеха.'),
                                                   telebot.types.InputMediaPhoto(open('5.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('10.jpg', 'rb'))])
        elif message.text == 'Первые достижения':
            bot.send_media_group(message.chat.id,
                                 [telebot.types.InputMediaPhoto(open('6.jpg', 'rb'), caption='Первые достижения'),
                                  telebot.types.InputMediaPhoto(open('7.jpg', 'rb')),
                                  telebot.types.InputMediaPhoto(open('7.jpg', 'rb'))])
bot.polling(none_stop=True)
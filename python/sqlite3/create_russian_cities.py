# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('/path/to/your/database/')
cursor = conn.cursor()
table_name = 'cart_city'

print '\n======Start creating cities======\n'

cursor.execute("INSERT INTO \
    " + table_name + " ('region_id', 'name', 'visible')\
        VALUES (4312, 'Москва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Абрамцево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Алабино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Апрелевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Архангельское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Ашитково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Байконур', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Бакшеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Балашиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Барыбино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Белоомут', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Белые Столбы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Бородино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Бронницы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Быково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Валуево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Вербилки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Верея', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Видное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Внуково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Вождь Пролетариата', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Волоколамск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Вороново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Воскресенск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Восточный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Востряково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Высоковск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Голицино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Деденево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Дедовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Джержинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Дмитров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Долгопрудный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Домодедово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Дорохово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Дрезна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Дубки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Дубна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Егорьевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Железнодорожный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Жилево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Жуковский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Загорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Загорянский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Запрудная', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Зарайск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Звенигород', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Зеленоград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Ивантеевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Икша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Ильинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Истра', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Калининград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Кашира', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Керва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Климовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Клин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Клязьма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Кожино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Кокошкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Коломна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Колюбакино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Королев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Косино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Котельники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Красково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Красноармейск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Красногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Краснозаводск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Краснознаменск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Красный Ткач', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Крюково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Кубинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Купавна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Куровское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Лесной Городок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Ликино-Дулево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Лобня', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Лопатинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Лосино-Петровский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Лотошино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Лукино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Луховицы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Лыткарино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Львовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Люберцы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Малаховка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Михайловское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Михнево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Можайск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Монино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Муханово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Мытищи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Нарофоминск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Нахабино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Некрасовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Немчиновка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Новобратцевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Новоподрезково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Ногинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Обухово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Одинцово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Ожерелье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Озеры', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Октябрьский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Опалиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Орехово-Зуево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Павловский Посад', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Первомайский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Пески', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Пироговский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Подольск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Полушкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Правдинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Привокзальный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Пролетарский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Протвино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Пушкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Пущино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Радовицкий', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Раменское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Реутов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Решетниково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Родники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Рошаль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Рублево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Руза', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Салтыковка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Северный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Сергиев Посад', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Серебряные Пруды', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Серпухов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Солнечногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Солнцево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Софрино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Старая Купавна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Старбеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Ступино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Сходня', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Талдом', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Текстильщик', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Темпы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Тишково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Томилино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Троицк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Туголесский Бор', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Тучково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Уваровка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Удельная', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Успенское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Фирсановка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Фосфоритный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Фрязино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Фряново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Химки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Хорлово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Хотьково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Черкизово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Черноголовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Черусти', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Чехов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Шарапово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Шатура', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Шатурторф', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Шаховская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Шереметьевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Щелково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Щербинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Электрогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Электросталь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Электроугли', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4312, 'Яхрома', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Санкт-Петербург', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Александровская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Бокситогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Большая Ижора', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Будогощь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Вознесенье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Волосово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Волхов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Всеволожск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Выборг', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Вырица', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Высоцк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Гатчина', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Дружная Горка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Дубровка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Ефимовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Зеленогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Ивангород', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Каменногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Кикерино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Кингисепп', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Кириши', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Кировск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Кобринское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Колпино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Коммунар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Кронштадт', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Лисий Нос', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Лодейное Поле', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Ломоносов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Луга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Павловск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Парголово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Петродворец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Пикалёво', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Подпорожье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Приозерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Пушкин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Сестрорецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Сланцы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Сосновый Бор', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Тихвин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Тосно', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4925, 'Шлиссельбург', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (1998532, 'Адыгейск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (1998532, 'Майкоп', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Акташ', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Акутиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Алейск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Алтайский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Баево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Барнаул', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Белово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Белокуриха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Белоярск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Бийск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Благовещенск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Боровлянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Бурла', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Бурсоль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Волчиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Горно-Алтайск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Горняк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Ельцовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Залесово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Заринск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Заток', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Змеиногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Камень-на-Оби', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Ключи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Кош-Агач', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Красногорское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Краснощеково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Кулунда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Кытманово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Мамонтово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Новичиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Новоалтайск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Онгудай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Павловск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Петропавловское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Поспелиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Ребриха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Родино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Рубцовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Славгород', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Смоленское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Солонешное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Солтон', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Староаллейское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Табуны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Тальменка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Топчиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Троицкое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Турочак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Тюменцево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Угловское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Усть-Калманка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Усть-Кан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Усть-Кокса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Усть-Улаган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Усть-Чарышская Пристань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Хабары', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Целинное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Чарышское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Шебалино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Шелаболиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3160, 'Шипуново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Айгунь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Архара', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Белогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Благовещенск (Амурская обл.)', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Бурея', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Возжаевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Екатеринославка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Ерофей Павлович', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Завитинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Зея', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Златоустовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Ивановка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Коболдо', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Магдагачи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Новобурейский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Поярково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Райчихинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Ромны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Свободный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Серышево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Сковородино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Стойба', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Тамбовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Тында', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Шимановск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Экимчан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3223, 'Ядрино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Амдерма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Архангельск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Березник', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Вельск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Верхняя Тойма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Волошка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Вычегодский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Емца', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Илеза', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Ильинско-Подомское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Каргополь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Карпогоры', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Кодино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Коноша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Коряжма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Котлас', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Красноборск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Лешуконское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Мезень', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Мирный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Нарьян-Мар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Новодвинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Няндома', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Онега', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Пинега', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Плесецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Северодвинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Сольвычегодск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Холмогоры', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Шенкурск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3251, 'Яренск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Астрахань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Ахтубинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Верхний Баскунчак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Володарский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Енотаевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Икряное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Камызяк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Капустин Яр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Красный Яр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Лиман', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Началово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Харабали', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3282, 'Черный Яр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Аксаково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Амзя', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Аскино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Баймак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Бакалы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Белебей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Белорецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Бижбуляк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Бирск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Благовещенск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Большеустьикинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Бураево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Верхнеяркеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Верхние Киги', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Верхние Татышлы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Верхний Авзян', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Давлеканово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Дуван', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Дюртюли', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Ермекеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Ермолаево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Зилаир', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Зирган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Иглино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Инзер', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Исянгулово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Ишимбай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Кананикольское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Кандры', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Караидель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Караидельский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Киргиз-Мияки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Красноусольский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Кумертау', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Кушнаренково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Малояз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Мелеуз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Месягутово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Мраково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Нефтекамск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Октябрьский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Раевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Салават', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Сибай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Старобалтачево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Старосубхангулово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Стерлибашево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Стерлитамак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Туймазы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Уфа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Учалы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Федоровка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Чекмагуш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Чишмы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Шаран', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3296, 'Янаул', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Алексеевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Белгород', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Борисовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Валуйки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Вейделевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Волоконовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Грайворон', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Губкин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Ивня', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Короча', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Красногвардейское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Новый Оскол', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Ракитное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Ровеньки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Старый Оскол', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Строитель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Чернянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3352, 'Шебекино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Алтухово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Белая Березка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Белые Берега', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Большое Полпино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Брянск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Бытошь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Выгоничи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Вышков', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Гордеевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Дубровка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Дятьково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Жирятино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Жуковка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Злынка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Ивот', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Карачев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Клетня', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Климово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Клинцы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Кокаревка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Комаричи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Красная Гора', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Локоть', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Мглин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Навля', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Новозыбков', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Погар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Почеп', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Ржаница', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Рогнедино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Севск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Стародуб', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Суземка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Сураж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Трубчевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3371, 'Унеча', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Бабушкин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Багдарин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Баргузин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Баянгол', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Бичура', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Выдрино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Гусиное Озеро', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Гусиноозерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Заиграево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Закаменск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Иволгинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Илька', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Кабанск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Каменск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Кижинга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Курумкан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Кырен', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Кяхта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Монды', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Мухоршибирь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Нижнеангарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Орлик', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Петропавловка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Романовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Северобайкальск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Селенгинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Сосново-Озерское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Таксимо', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Турунтаево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Улан-Удэ', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3407, 'Хоринск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Александров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Андреево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Анопино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Бавлены', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Балакирево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Боголюбово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Великодворский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Вербовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Владимир', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Вязники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Городищи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Гороховец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Гусевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Гусь Хрустальный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Золотково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Иванищи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Камешково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Карабаново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Киржач', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Ковров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Кольчугино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Красная Горбатка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Меленки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Муром', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Петушки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Покров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Собинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Судогда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Суздаль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3437, 'Юрьев-Польский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Алексеевская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Алущевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Быково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Волгоград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Волжский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Городище', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Дубовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Елань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Жирновск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Иловля', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Калач-на-Дону', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Камышин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Кириллов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Клетский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Котельниково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Котово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Кумылженская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Ленинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Михайловка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Нехаевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Николаевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Новоаннинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Новониколаевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Ольховка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Палласовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Рудня', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Светлый Яр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Серафимович', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Средняя Ахтуба', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Сталинград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Старая Полтавка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Суровикино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Урюпинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Фролово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3468, 'Чернышковский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Бабаево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Белозерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Великий Устюг', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Верховажье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Вожега', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Вологда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Вохтога', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Вытегра', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Грязовец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Кадников', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Кадуй', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Кичменгский Городок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Липин Бор', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Никольск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Нюксеница', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Сокол', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Сямжа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Тарногский Городок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Тотьма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Устюжна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Харовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Чагода', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Череповец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Шексна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3503, 'Шуйское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Анна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Бобров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Богучар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Борисоглебск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Бутурлиновка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Верхний Мамон', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Верхняя Хава', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Воробьевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Воронеж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Грибановский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Давыдовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Елань-Коленовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Калач', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Кантемировка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Лиски', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Нижнедевицк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Новая Усмань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Новохоперск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Ольховатка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Острогожск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Павловск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Панино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Петропавловка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Поворино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Подгоренский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Рамонь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Репьевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Россошь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Семилуки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Таловая', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Терновка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Хохольский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'Эртиль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3529, 'нововоронеж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Агвали', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Акуша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Ахты', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Ачису', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Бабаюрт', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Бежта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Ботлих', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Буйнакск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Вачи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Гергебиль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Гуниб', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Дагестанские Огни', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Дербент', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Дылым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Ершовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Избербаш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Карабудахкент', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Карата', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Каспийск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Касумкент', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Кизилюрт', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Кизляр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Кочубей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Кумух', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Курах', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Магарамкент', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Маджалис', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Махачкала', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Мехельта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Новолакское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Рутул', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Советское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Тарумовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Терекли-Мектеб', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Тлярата', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Тпиг', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Уркарах', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Хасавюрт', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Хив', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Хунзах', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Цуриб', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3630, 'Южно-Сухокумск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3673, 'Биробиджан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Архиповка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Верхний Ландех', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Вичуга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Гаврилов Посад', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Долматовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Дуляпино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Заволжск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Заречный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Иваново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Иваньковский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Ильинское-Хованское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Каминский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Кинешма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Комсомольск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Кохма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Лух', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Палех', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Пестяки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Приволжск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Пучеж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Родники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Савино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Сокольское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Тейково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Фурманов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Шуя', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Южа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3675, 'Юрьевец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Алексеевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Алзамай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Алыгжер', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Ангарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Артемовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Атагай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Байкал', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Байкальск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Балаганск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Баяндай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Бирюсинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Бодайбо', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Большая Речка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Большой Луг', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Бохан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Братск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Видим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Витимский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Вихоревка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Еланцы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Ербогачен', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Железногорск-Илимский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Жигалово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Забитуй', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Залари', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Звездный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Зима', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Иркутск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Казачинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Качуг', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Квиток', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Киренск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Куйтун', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Култук', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Кутулик', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Мама', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Нижнеудинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Оса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Саянск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Слюдянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Тайшет', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Тулун', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Усолье-Сибирское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Усть-Илимск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Усть-Кут', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Усть-Ордынский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Усть-Уда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Черемхово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Чунский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3703, 'Шелехов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Баксан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Майский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Нальчик', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Нарткала', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Прохладный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Советское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Терек', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Тырныауз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3751, 'Чегем-Первый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Багратионовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Балтийск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Гвардейск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Гурьевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Гусев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Железнодорожный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Зеленоградск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Знаменск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Кёнигсберг', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Калининград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Кенисберг', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Краснознаменск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Мамоново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Неман', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Нестеров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Озерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Полесск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Правдинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Светлогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Светлый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Славск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Советск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3761, 'Черняховск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Аршань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Каспийский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Комсомольский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Малые Дербеты', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Приютное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Советское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Троицкое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Утта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Цаган-Аман', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Элиста', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Юста', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Яшалта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3827, 'Яшкуль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Бабынино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Балабаново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Барятино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Белоусово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Бетлица', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Боровск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Дугна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Дудоровский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Думиничи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Еленский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Жиздра', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Износки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Калуга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Киров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Козельск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Кондрово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Людиново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Малоярославец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Медынь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Мещовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Мосальск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Обнинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Перемышль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Спас-Деменск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Сухиничи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Таруса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Ульяново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Ферзиково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Хвастовичи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3841, 'Юхнов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Атласово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Аянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Большерецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Вилючинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Елизово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Ильпырский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Каменское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Кировский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Ключи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Крапивная', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Мильково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Никольское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Озерновский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Оссора', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Палана', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Парень', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Пахачи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Петропавловск-Камчатский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Тигиль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Тиличики', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Усть-Большерецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3872, 'Усть-Камчатск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Амбарный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Беломорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Валаам', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Вирандозеро', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Гирвас', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Деревянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Идель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Ильинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Импалахти', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Калевала', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Кемь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Кестеньга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Кондопога', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Костомукша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Лахденпохья', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Лоухи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Медвежьегорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Муезерский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Олонец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Петрозаводск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Питкяранта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Повенец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Пряжа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Пудож', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Сегежа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Сортавала', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Софпорог', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3892, 'Суоярви', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Анжеро-Судженск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Барзас', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Белово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Белогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Березовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Грамотеино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Гурьевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Ижморский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Итатский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Калтан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Кедровка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Кемерово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Киселевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Крапивинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Ленинск-Кузнецкий', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Мариинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Междуреченск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Мыски', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Новокузнецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Осинники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Прокопьевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Промышленная', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Тайга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Таштагол', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Тисуль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Топки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Тяжинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Юрга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Яшкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3921, 'Яя', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Арбаж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Аркуль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Белая Холуница', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Богородское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Боровой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Верхошижемье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Вятские Поляны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Зуевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Каринторф', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Кикнур', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Кильмезь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Киров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Кирово-Чепецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Кирс', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Кобра', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Котельнич', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Кумены', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Ленинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Луза', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Малмыж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Мураши', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Нагорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Нема', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Нововятск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Нолинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Омутнинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Опарино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Оричи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Пижанка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Подосиновец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Санчурск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Свеча', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Слободской', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Советск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Суна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Тужа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Уни', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Уржум', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Фаленки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Халтурин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Юрья', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3952, 'Яранск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Абезь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Айкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Верхняя Инта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Визинга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Водный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Вожаель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Воркута', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Вуктыл', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Гешарт', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Елецкий', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Емва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Заполярный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Ижма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Инта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Ираель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Каджером', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Кажым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Кожым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Койгородок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Корткерос', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Кослан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Объячево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Печора', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Сосногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Сыктывкар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Троицко-Печерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Усинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Усогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Усть-Кулом', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Усть-Цильма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3994, 'Ухта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Антропово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Боговарово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Буй', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Волгореченск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Галич', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Горчуха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Зебляки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Кадый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Кологрив', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Кострома', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Красное-на-Волге', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Макарьев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Мантурово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Нерехта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Нея', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Островское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Павино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Парфентьево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Поназырево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Солигалич', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Судиславль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Сусанино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Чухлома', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Шарья', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4026, 'Шемятино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Абинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Абрау-Дюрсо', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Анапа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Апшеронск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Армавир', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Архипо-Осиповка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Афипский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Ахтырский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Ачуево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Белореченск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Верхнебаканский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Выселки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Геленджик', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Гиагинская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Горячий Ключ', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Джубга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Динская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Ейск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Ильский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Кабардинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Калинино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Калининская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Каменномостский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Каневская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Кореновск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Красноармейская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Краснодар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Кропоткин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Крыловская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Крымск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Курганинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Кущевская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Лабинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Лениградская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Майкоп', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Мостовской', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Новороссийск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Отрадная', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Павловская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Приморско-Ахтарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Северская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Славянск-на-Кубани', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Сочи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Староминская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Старощербиновская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Тбилисская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Темрюк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Тимашевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Тихорецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Туапсе', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Тульский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Усть-Лабинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4052, 'Шовгеновский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, ' Железногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Абаза', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Абакан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Абан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Агинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Артемовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Аскиз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Ачинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Байкит', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Балахта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Балыкса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Белый Яр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Бельтырский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Бея', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Бискамжа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Боготол', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Боград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Богучаны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Большая Мурта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Большой Улуй', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Бородино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Ванавара', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Верхнеимбатск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Горячегорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Дзержинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Дивногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Диксон', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Дудинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Емельяново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Енисейск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Ермаковское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Заозерный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Зеленогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Игарка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Идринское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Иланский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Ирбейское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Казачинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Канск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Каратузское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Караул', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Кежма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Кодинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Козулька', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Копьево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Краснотуранск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Красноярск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Курагино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Лесосибирск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Минусинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Мотыгино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Назарово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Нижний Ингаш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Новоселово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Норильск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Партизанское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Пировское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Саяногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Северо-Енисейский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Сосновоборск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Тасеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Таштып', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Тура', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Туруханск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Тюхтет', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Ужур', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Усть-Авам', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Уяр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Хатанга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Черемушки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Черногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Шалинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Шарыпово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Шира', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4105, 'Шушенское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Варгаши', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Глядянское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Далматово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Каргаполье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Катайск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Кетово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Курган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Куртамыш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Лебяжье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Макушино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Мишкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Мокроусово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Петухово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Половинное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Сафакулево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Целинное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Шадринск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Шатрово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Шумиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Щучье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4176, 'Юргамыш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Альменево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Белая', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Большое Солдатское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Глушково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Горшечное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Дмитриев-Льговский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Железногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Золотухино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Касторное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Конышевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Коренево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Курск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Курчатов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Кшенский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Льгов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Мантурово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Медвенка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Обоянь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Поныри', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Пристень', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Прямицыно', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Рыльск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Суджа', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Тим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Фатеж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Хомутовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Черемисиново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4198, 'Щигры', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Грязи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Данхов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Доброе', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Долгоруково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Елец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Задонск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Измалково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Казинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Лебедянь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Лев Толстой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Липецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Тербуны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Усмань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Хлевное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4227, 'Чаплыгин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Анадырь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Атка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Балыгычан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Беринговский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Билибино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Большевик', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Ванкарем', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Иульитин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Кадыкчан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Лаврентия', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Магадан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Мыс Шмидта', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Ола', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Омонск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Омсукчан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Палатка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Певек', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Провидения', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Сеймчан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Синегорье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Сусуман', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Усть-Белая', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Усть-Омчуг', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Эвенск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Эгвекинот', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4243, 'Ягодное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Волжск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Дубовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Звенигово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Йошкар-Ола', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Килемары', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Козьмодемьянск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Куженер', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Мари-Турек', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Медведево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Морки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Новый Торьял', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Оршанка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Параньга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Сернур', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Советский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4270, 'Юрино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Ардатов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Атюрьево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Атяшево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Большие Березники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Большое Игнатово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Выша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Ельники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Зубова Поляна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Инсар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Кадошкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Кемля', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Ковылкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Комсомольский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Кочкурово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Краснослободск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Лямбирь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Ромоданово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Рузаевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Саранск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Старое Шайгово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Темников', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Теньгушево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Торбеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4287, 'Чамзинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Апатиты', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Африканда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Верхнетуломский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Заозерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Заполярный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Зареченск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Зашеек', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Зеленоборский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Кандалакша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Кильдинстрой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Кировск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Ковдор', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Кола', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Конда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Мончегорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Мурманск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Мурмаши', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Никель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Оленегорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Полярные Зори', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Полярный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Североморск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Снежногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4481, 'Умба', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Ардатов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Арзамас', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Арья', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Балахна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Богородск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Большереченск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Большое Болдино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Большое Козино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Большое Мурашкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Большое Пикино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Бор', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Бутурлино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Вад', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Варнавино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Васильсурск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Вахтан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Вача', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Велетьма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Ветлуга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Виля', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Вознесенское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Володарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Воротынец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Ворсма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Воскресенское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Выездное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Выкса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Гагино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Гидроторф', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Горбатов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Горбатовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Городец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Горький', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Дальнее Константиново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Дзержинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Дивеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Досчатое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Заволжье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Катунки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Керженец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Княгинино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Ковернино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Красные Баки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Кстово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Кулебаки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Лукоянов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Лысково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Навашино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Нижний Новгород', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Павлово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Первомайск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Перевоз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Пильна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Починки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Саров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Сергач', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Сеченово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Сосновское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Спасское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Тонкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Тоншаево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Уразовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Урень', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Чкаловск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Шаранга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Шатки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3563, 'Шахунья', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Анциферово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Батецкий', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Большая Вишера', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Боровичи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Валдай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Волот', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Деманск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Зарубино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Кресцы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Любытино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Малая Вишера', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Марево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Мошенское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Новгород', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Окуловка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Парфино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Пестово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Поддорье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Сольцы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Старая Русса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Хвойное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Холм', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Чудово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4503, 'Шимск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Баган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Барабинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Бердск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Биаза', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Болотное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Венгерово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Довольное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Завьялово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Искитим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Карасук', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Каргат', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Колывань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Краснозерское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Крутиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Куйбышев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Купино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Кыштовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Маслянино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Михайловский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Мошково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Новосибирск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Ордынское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Северное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Сузун', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Татарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Тогучин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Убинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Усть-Тарка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Чаны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Черепаново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Чистоозерное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4528, 'Чулым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Береговой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Большеречье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Большие Уки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Горьковское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Знаменское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Исилькуль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Калачинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Колосовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Кормиловка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Крутинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Любинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Марьяновка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Муромцево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Называевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Нижняя Омка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Нововаршавка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Одесское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Оконешниково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Омск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Павлоградка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Полтавка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Русская Поляна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Саргатское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Седельниково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Таврическое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Тара', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Тевриз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Тюкалинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Усть-Ишим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Черлак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4561, 'Шербакуль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Абдулино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Адамовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Айдырлинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Акбулак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Аккермановка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Асекеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Беляевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Бугуруслан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Бузулук', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Гай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Грачевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Домбаровский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Дубенский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Илек', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Ириклинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Кувандык', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Курманаевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Матвеевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Медногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Новоорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Новосергиевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Новотроицк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Октябрьское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Оренбург', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Орск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Первомайский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Переволоцкий', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Пономаревка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Саракташ', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Светлый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Северное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Соль-Илецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Сорочинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Ташла', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Тоцкое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Тюльган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Шарлык', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Энергетик', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4593, 'Ясный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Болхов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Верховье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Глазуновка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Дмитровск-Орловский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Долгое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Залегощь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Змиевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Знаменское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Колпны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Красная Заря', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Кромы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Ливны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Малоархангельск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Мценск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Нарышкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Новосиль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Орел', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Покровское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Сосково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Тросна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Хомутово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Хотынец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4633, 'Шаблыкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Башмаково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Беднодемьяновск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Беково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Белинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Бессоновка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Вадинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Верхозим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Городище', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Евлашево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Земетчино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Золотаревка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Исса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Каменка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Колышлей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Кондоль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Кузнецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Лопатино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Малая Сердоба', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Мокшан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Наровчат', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Неверкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Нижний Ломов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Никольск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Пачелма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Пенза', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Русский Камешкир', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Сердобск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Сосновоборск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Сура', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Тамала', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4657, 'Шемышейка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Барда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Березники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Большая Соснова', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Верещагино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Гайны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Горнозаводск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Гремячинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Губаха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Добрянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Елово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Зюкайка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Ильинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Карагай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Керчевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Кизел', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Коса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Кочево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Красновишерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Краснокамск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Кудымкар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Куеда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Кунгур', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Лысьва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Ныроб', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Нытва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Октябрьский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Орда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Оса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Оханск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Очер', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Пермь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Соликамск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Суксун', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Уинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Усолье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Усть-Кишерть', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Чайковский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Частые', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Чердынь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Чернореченский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Чернушка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Чусовой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Юрла', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4689, 'Юсьва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Анучино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Арсеньев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Артем', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Артемовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Большой Камень', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Валентин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Владивосток', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Высокогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Горные Ключи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Горный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Дальнегорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Дальнереченск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Зарубино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Кавалерово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Каменка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Камень-Рыболов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Кировский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Лазо', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Лесозаводск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Лучегорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Михайловка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Находка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Новопокровка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Ольга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Партизанск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Пограничный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Покровка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Русский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Самарга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Славянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Спасск-Дальний', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Терней', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Уссурийск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Фокино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Хасан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Хороль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Черниговка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Чугуевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4734, 'Яковлевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Бежаницы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Великие Луки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Гдов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Дедовичи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Дно', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Заплюсье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Идрица', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Красногородское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Кунья', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Локня', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Невель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Новоржев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Новосокольники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Опочка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Остров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Палкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Печоры', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Плюсса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Порхов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Псков', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Пустошка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Пушкинские Горы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Пыталово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Себеж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Струги-Красные', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4773, 'Усвяты', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Азов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Аксай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Алмазный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Аютинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Багаевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Батайск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Белая Калитва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Боковская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Большая Мартыновка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Вешенская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Волгодонск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Восход', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Гигант', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Горняцкий', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Гуково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Донецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Донской', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Дубовское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Егорлыкская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Жирнов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Заветное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Заводской', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Зверево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Зерноград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Зимовники', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Кагальницкая', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Казанская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Каменоломни', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Каменск-Шахтинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Кашары', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Коксовый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Константиновск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Красный Сулин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Куйбышево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Матвеев Курган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Мигулинская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Миллерово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Милютинская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Морозовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Новочеркасск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Новошахтинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Обливская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Орловский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Песчанокопское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Покровское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Пролетарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Ремонтное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Родионово-Несветайская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Ростов-на-Дону', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Сальск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Семикаракорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Таганрог', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Тарасовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Тацинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Усть-Донецкий', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Целина', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Цимлянск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Чалтырь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Чертково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Шахты', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4800, 'Шолоховский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Александро-Невский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Горняк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Гусь Железный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Елатьма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Ермишь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Заречный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Захарово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Кадом', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Касимов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Кораблино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Милославское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Михайлов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Пителино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Пронск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Путятино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Рыбное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Ряжск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Рязань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Сапожок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Сараи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Сасово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Скопин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Спас-Клепики', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Спасск-Рязанский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Старожилово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Ухолово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Чучково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Шацк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4861, 'Шилово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Алексеевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Безенчук', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Богатое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Богатырь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Большая Глущица', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Большая Черниговка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Борское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Волжский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Жигулевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Зольное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Исаклы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Камышла', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Кинель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Кинель-Черкасы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Клявлино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Кошки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Красноармейское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Красный Яр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Куйбышев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Нефтегорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Новокуйбышевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Октябрьск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Отрадный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Пестравка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Похвистнево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Приволжье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Самара', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Сургут (Самарская обл.)', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Сызрань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Тольятти', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Хворостянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Чапаевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Челно-Вершины', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Шентала', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4891, 'Шигоны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Александров Гай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Аркадак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Аткарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Базарный Карабулак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Балаково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Балашов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Балтай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Возрождение', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Вольск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Воскресенское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Горный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Дергачи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Духовницкое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Екатериновка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Ершов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Заречный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Ивантеевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Калининск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Каменский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Красноармейск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Красный Кут', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Лысые Горы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Маркс', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Мокроус', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Новоузенск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Новые Бурасы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Озинки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Перелюб', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Петровск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Питерка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Пугачев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Ровное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Романовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Ртищево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Самойловка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Саратов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Степное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Татищево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Турки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Хвалынск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (4969, 'Энгельс', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Абый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Алдан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Амга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Батагай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Бердигестях', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Беркакит', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Бестях', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Борогонцы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Верхневилюйск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Верхнеколымск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Верхоянск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Вилюйск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Витим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Власово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Жиганск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Зырянка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Кангалассы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Канкунский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Ленск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Майя', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Менкеря', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Мирный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Нерюнгри', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Нычалах', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Нюрба', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Олекминск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Покровск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Сангар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Саскылах', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Среднеколымск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Сунтар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Тикси', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Усть-Мая', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Усть-Нера', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Хандыга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Хонуу', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Черский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Чокурдах', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Чурапча', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5011, 'Якутск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Александровск-Сахалинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Анбэцу', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Анива', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Бошняково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Быков', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Вахрушев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Взморье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Гастелло', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Горнозаводск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Долинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Ильинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Катангли', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Корсаков', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Курильск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Макаров', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Невельск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Ноглики', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Оха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Поронайск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Северо-Курильск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Смирных', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Томари', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Тымовское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Углегорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Холмск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Шахтерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Южно-Курильск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5052, 'Южно-Сахалинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Алапаевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Алтынай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Арамиль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Артемовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Арти', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Асбест', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Ачит', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Байкалово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Басьяновский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Белоярский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Березовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Богданович', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Буланаш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Верхний Тагил', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Верхняя Пышма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Верхняя Салда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Верхняя Синячиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Верхняя Сысерть', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Верхняя Тура', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Верхотурье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Висим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Волчанск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Воронцовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Гари', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Дегтярск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Екатеринбург', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Ертарский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Заводоуспенское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Зыряновский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Зюзельский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Ивдель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Изумруд', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Ирбит', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Ис', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Каменск-Уральский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Камышлов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Карпинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Карпунинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Качканар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Кировград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Краснотурьинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Красноуральск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Красноуфимск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Кушва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Лесной', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Михайловск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Невьянск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Нижние Серги', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Нижний Тагил', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Нижняя Салда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Нижняя Тура', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Новая Ляля', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Новоуральск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Оус', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Первоуральск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Полевской', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Пышма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Ревда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Реж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Свердловск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Североуральск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Серов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Сосьва', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Среднеуральск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Сухой Лог', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Сысерть', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Таборы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Тавда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Талица', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Тугулым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Туринск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5080, 'Туринская Слобода', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Алагир', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Ардон', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Беслан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Бурон', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Владикавказ', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Дигора', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Моздок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Орджоникидзе', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5151, 'Чикола', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Велиж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Верхнеднепровский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Ворга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Вязьма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Гагарин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Глинка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Голынки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Демидов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Десногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Дорогобуж', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Духовщина', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Екимовичи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Ельня', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Ершичи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Издешково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Кардымово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Красный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Монастырщина', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Новодугино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Починок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Рославль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Рудня', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Сафоново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Смоленск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Сычевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Угра', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Хиславичи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Холм-Жирковский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Шумячи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5161, 'Ярцево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Александровское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Арзгир', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Благодарный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Буденновск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Георгиевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Дивное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Домбай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Донское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Ессентуки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Железноводск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Зеленокумск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Изобильный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Иноземцево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Ипатово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Карачаевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Кисловодск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Кочубеевское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Красногвардейское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Курсавка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Левокумское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Минеральные Воды', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Невинномысск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Нефтекумск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Новоалександровск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Новоалександровская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Новопавловск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Новоселицкое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Преградная', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Пятигорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Светлоград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Солнечнодольск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Ставрополь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Степное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Теберда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Усть-Джегута', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Хабез', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5191, 'Черкесск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Бондари', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Гавриловка Вторая', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Жердевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Знаменка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Инжавино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Кирсанов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Котовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Мичуринск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Мордово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Моршанск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Мучкапский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Первомайский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Петровское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Пичаево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Рассказово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Ржакса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Староюрьево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Тамбов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Токаревка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Уварово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5225, 'Умет', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Агрыз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Азнакаево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Аксубаево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Актюбинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Алексеевское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Альметьевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Альметьевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Апастово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Арск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Бавлы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Базарные Матаки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Балтаси', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Богатые Сабы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Брежнев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Бугульма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Буинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Васильево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Верхний Услон', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Высокая Гора', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Дербешкинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Елабуга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Заинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Зеленодольск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Казань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Камское Устье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Карабаш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Куйбышев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Кукмод', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Кукмор', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Лаишево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Лениногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Мамадыш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Менделеевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Мензелинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Муслюмово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Набережные Челны', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Нижнекамск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Новошешминск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Нурлат', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Пестрецы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Рыбная Слобода', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Сарманово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Старое Дрожжаное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Тетюши', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5246, 'Чистополь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Андреаполь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Бежецк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Белый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Белый Городок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Березайка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Бологое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Васильевский Мох', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Выползово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Вышний Волочек', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Жарковский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Западная Двина', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Заречье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Зубцов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Изоплит', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Калашниково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Калинин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Калязин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Кашин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Кесова Гора', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Кимры', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Конаково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Красный Холм', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Кувшиново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Лесное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Лихославль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Максатиха', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Молоково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Нелидово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Оленино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Осташков', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Пено', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Рамешки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Ржев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Сандово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Селижарово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Сонково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Спирово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Старица', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Тверь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Торжок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Торопец', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Удомля', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (3784, 'Фирово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Александровское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Асино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Бакчар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Батурино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Белый Яр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Зырянское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Итатка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Каргасок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Катайга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Кожевниково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Колпашево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Кривошеино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Мельниково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Молчаново', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Парабель', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Первомайское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Подгорное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Северск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Стрежевой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Томск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5291, 'Тымск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Ак-Довурак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Бай Хаак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Кызыл', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Самагалтай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Сарыг-Сеп', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Суть-Холь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Тоора-Хем', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Туран', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Тээли', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Хову-Аксы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Чадан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Шагонар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5312, 'Эрзин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Агеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Алексин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Арсеньево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Барсуки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Бегичевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Белев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Богородицк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Болохово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Велегож', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Венев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Волово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Горелки', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Донской', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Дубна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Епифань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Ефремов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Заокский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Казановка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Кимовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Киреевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Куркино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Ленинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Новомосковск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Одоев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Плавск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Суворов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Тула', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Узловая', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Щекино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5326, 'Ясногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Абатский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Аксарка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Армизонское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Аромашево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Белоярский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Бердюжье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Большое Сорокино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Вагай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Викулово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Винзили', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Голышманово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Губкинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Заводопетровский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Заводоуковск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Излучинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Исетское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Ишим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Казанское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Казым-Мыс', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Когалым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Кондинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Красноселькуп', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Лабытнанги', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Ларьяк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Мегион', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Мужи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Муравленко', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Надым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Находка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Нефтеюганск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Нижневартовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Нижняя Тавда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Новый Уренгой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Ноябрьск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Нягань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Октябрьское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Омутинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Радужный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Салехард', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Сладково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Советский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Сургут', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Тазовский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Тарко-Сале', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Тобольск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Тюмень', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Уват', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Унъюган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Упорово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Урай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Ханты-Мансийск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Юрибей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Ялуторовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Яр-Сале', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5356, 'Ярково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Алнаши', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Балезино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Вавож', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Воткинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Глазов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Грахово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Дебесы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Завьялово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Игра', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Ижевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Кама', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Камбарка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Каракулино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Кез', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Кизнер', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Киясово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Красногорское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Можга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Сарапул', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Селты', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Сюмси', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Ува', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Устинов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Шаркан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Юкаменское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Якшур-Бодья', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5404, 'Яр', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Базарный Сызган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Барыш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Большое Нагаткино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Вешкайма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Глотовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Димитровград', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Игнатовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Измайлово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Инза', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Ишеевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Канадей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Карсун', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Кузоватово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Майна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Новая Малыкла', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Новоспасское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Павловка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Радищево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Сенгилей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Старая Кулатка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Старая Майна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Сурское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Тереньга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Ульяновск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5432, 'Чердаклы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Аксай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Дарьинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Деркул', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Джамбейты', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Джаныбек', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Казталовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Калмыково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Каратобе', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Переметное', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Сайхин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Уральск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Федоровка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Фурманово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5458, 'Чапаев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Амурск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Аян', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Березовый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Бикин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Бира', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Биракан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Богородское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Болонь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Ванино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Волочаевка Вторая', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Высокогорный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Вяземский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Горный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Гурское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Дормидонтовка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Заветы Ильича', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Известковый', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Иннокентьевка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Комсомольск-на-Амуре', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Ленинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Нелькан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Николаевск-на-Амуре', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Облучье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Охотск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Переяславка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Смидович', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Советская Гавань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Софийск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Троицкое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Тугур', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Хабаровск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Чегдомын', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5473, 'Чумикан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2316497, 'Абакан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2316497, 'Саяногорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Аган', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Игрим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Излучинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Лангепас', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Лянтор', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Мегион', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Нефтеюганск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Нижневартовск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Нягань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Покачи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Приобье', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Пыть-Ях', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Радужный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Сургут', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Урай', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Ханты-Мансийск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2499002, 'Югорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Агаповка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Аргаяш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Аша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Бакал', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Бреды', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Варна', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Верхнеуральск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Верхний Уфалей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Еманжелинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Златоуст', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Карабаш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Карталы', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Касли', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Катав-Ивановск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Копейск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Коркино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Кунашак', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Куса', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Кыштым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Магнитогорск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Миасс', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Озерск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Октябрьское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Пласт', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Сатка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Сим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Снежинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Трехгорный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Троицк', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Увельский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Уйское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Усть-Катав', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Фершампенуаз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Чебаркуль', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Челябинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Чесма', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Южно-Уральск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5507, 'Юрюзань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Аргун', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Грозный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Гудермез', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Малгобек', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Назрань', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Наурская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Ножай-Юрт', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Орджоникидзевская', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Советское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Урус-Мартан', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5543, 'Шали', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Агинское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Аксеново-Зиловское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Акша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Александровский Завод', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Амазар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Арбагар', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Атамановка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Балей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Борзя', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Букачача', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Газимурский Завод', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Давенда', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Дарасун', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Дровяная', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Дульдурга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Жиндо', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Забайкальск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Итака', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Калга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Карымское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Кличка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Ключевский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Кокуй', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Краснокаменск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Красный Чикой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Кыра', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Моготуй', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Могоча', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Нерчинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Нерчинский Завод', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Нижний Часучей', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Оловянная', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Первомайский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Петровск-Забайкальский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Приаргунск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Сретенск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Тупик', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Улеты', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Хилок', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Чара', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Чернышевск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Чита', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Шелопугино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5555, 'Шилка', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Алатырь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Аликово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Батырева', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Буинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Вурнары', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Ибреси', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Канаш', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Киря', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Комсомольское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Красноармейское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Красные Четаи', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Кугеси', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Мариинский Посад', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Моргауши', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Новочебоксарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Порецкое', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Урмары', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Цивильск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Чебоксары', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Шемурша', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Шумерля', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Ядрин', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Яльчики', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5600, 'Янтиково', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2415585, 'Анадырь', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (2415585, 'Билибино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Губкинский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Заполярный', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Муравленко', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Надым', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Новый Уренгой', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Ноябрьск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Пуровск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Салехард', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5019394, 'Тарко', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Андропов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Берендеево', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Большое Село', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Борисоглебский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Брейтово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Бурмакино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Варегово', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Волга', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Гаврилов Ям', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Данилов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Любим', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Мышкино', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Некрасовское', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Новый Некоуз', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Переславль-Залесский', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Пошехонье-Володарск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Ростов', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Рыбинск', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Тутаев', 1)")
cursor.execute("INSERT INTO \
" + table_name + " ('region_id', 'name', 'visible')\
VALUES (5625, 'Углич', 1)")
cursor.execute("INSERT INTO \
    " + table_name + " ('region_id', 'name', 'visible')\
        VALUES (5625, 'Ярославль', 1)")

conn.commit()
print '\n======All cities created======\n'
conn.close()

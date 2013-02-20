# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('/path/to/your/database/')
cursor = conn.cursor()
table_name = 'cart_region'

print '\n======Start creating regions======\n'
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES ('4312', 'Москва и Московская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4925, 'Санкт-Петербург и область', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (1998532, 'Адыгея', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3160, 'Алтайский край', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3223, 'Амурская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3251, 'Архангельская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3282, 'Астраханская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3296, 'Башкортостан(Башкирия)', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3352, 'Белгородская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3371, 'Брянская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3407, 'Бурятия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3437, 'Владимирская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3468, 'Волгоградская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3503, 'Вологодская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3529, 'Воронежская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3630, 'Дагестан', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3673, 'Еврейская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3675, 'Ивановская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3703, 'Иркутская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3751, 'Кабардино-Балкария', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3761, 'Калининградская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3827, 'Калмыкия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3841, 'Калужская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3872, 'Камчатская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3892, 'Карелия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3921, 'Кемеровская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3952, 'Кировская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3994, 'Коми', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4026, 'Костромская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4052, 'Краснодарский край', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4105, 'Красноярский край', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4176, 'Курганская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4198, 'Курская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4227, 'Липецкая обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4243, 'Магаданская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4270, 'Марий Эл', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4287, 'Мордовия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4481, 'Мурманская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3563, 'Нижегородская (Горьковская)', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4503, 'Новгородская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4528, 'Новосибирская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4561, 'Омская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4593, 'Оренбургская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4633, 'Орловская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4657, 'Пензенская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4689, 'Пермская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4734, 'Приморский край', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4773, 'Псковская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4800, 'Ростовская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4861, 'Рязанская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4891, 'Самарская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (4969, 'Саратовская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5011, 'Саха (Якутия)', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5052, 'Сахалин', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5080, 'Свердловская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5151, 'Северная Осетия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5161, 'Смоленская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5191, 'Ставропольский край', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5225, 'Тамбовская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5246, 'Татарстан', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (3784, 'Тверская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5291, 'Томская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5312, 'Тува (Тувинская Респ.)', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5326, 'Тульская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5356, 'Тюменская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5404, 'Удмуртия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5432, 'Ульяновская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5458, 'Уральская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5473, 'Хабаровский край', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (2316497, 'Хакасия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (2499002, 'Ханты-Мансийский АО', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5507, 'Челябинская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5543, 'Чечено-Ингушетия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5555, 'Читинская обл.', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5600, 'Чувашия', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (2415585, 'Чукотский АО', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5019394, 'Ямало-Ненецкий АО', 1)")
cursor.execute("INSERT INTO " + table_name + " ('id', 'name', 'visible')\
    VALUES (5625, 'Ярославская обл.', 1)")

conn.commit()
print '\n======All regions created======\n'
conn.close()

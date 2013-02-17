--
-- Структура таблицы `country`
--

CREATE TABLE `country` (
  `country_id` int(11) unsigned NOT NULL auto_increment,
  `city_id` int(11) NOT NULL default '0',
  `name` varchar(128) NOT NULL default '',
  PRIMARY KEY  (`country_id`),
  KEY `city_id` (`city_id`)
) TYPE=MyISAM;

--
-- Дамп данных таблицы `country`
--

INSERT INTO `country` VALUES (3159, 0, 'Россия');
INSERT INTO `country` VALUES (4, 0, 'Австралия');
INSERT INTO `country` VALUES (63, 0, 'Австрия');
INSERT INTO `country` VALUES (81, 0, 'Азербайджан');
INSERT INTO `country` VALUES (173, 0, 'Ангуилья');
INSERT INTO `country` VALUES (177, 0, 'Аргентина');
INSERT INTO `country` VALUES (245, 0, 'Армения');
INSERT INTO `country` VALUES (7716093, 0, 'Арулько');
INSERT INTO `country` VALUES (248, 0, 'Беларусь');
INSERT INTO `country` VALUES (401, 0, 'Белиз');
INSERT INTO `country` VALUES (404, 0, 'Бельгия');
INSERT INTO `country` VALUES (425, 0, 'Бермуды');
INSERT INTO `country` VALUES (428, 0, 'Болгария');
INSERT INTO `country` VALUES (467, 0, 'Бразилия');
INSERT INTO `country` VALUES (616, 0, 'Великобритания');
INSERT INTO `country` VALUES (924, 0, 'Венгрия');
INSERT INTO `country` VALUES (971, 0, 'Вьетнам');
INSERT INTO `country` VALUES (994, 0, 'Гаити');
INSERT INTO `country` VALUES (1007, 0, 'Гваделупа');
INSERT INTO `country` VALUES (1012, 0, 'Германия');
INSERT INTO `country` VALUES (1206, 0, 'Голландия');
INSERT INTO `country` VALUES (2567393, 0, 'Гондурас');
INSERT INTO `country` VALUES (277557, 0, 'Гонконг');
INSERT INTO `country` VALUES (1258, 0, 'Греция');
INSERT INTO `country` VALUES (1280, 0, 'Грузия');
INSERT INTO `country` VALUES (1366, 0, 'Дания');
INSERT INTO `country` VALUES (2577958, 0, 'Доминиканская республика');
INSERT INTO `country` VALUES (1380, 0, 'Египет');
INSERT INTO `country` VALUES (1393, 0, 'Израиль');
INSERT INTO `country` VALUES (1451, 0, 'Индия');
INSERT INTO `country` VALUES (277559, 0, 'Индонезия');
INSERT INTO `country` VALUES (277561, 0, 'Иордания');
INSERT INTO `country` VALUES (3410238, 0, 'Ирак');
INSERT INTO `country` VALUES (1663, 0, 'Иран');
INSERT INTO `country` VALUES (1696, 0, 'Ирландия');
INSERT INTO `country` VALUES (1707, 0, 'Испания');
INSERT INTO `country` VALUES (1786, 0, 'Италия');
INSERT INTO `country` VALUES (1894, 0, 'Казахстан');
INSERT INTO `country` VALUES (2163, 0, 'Камерун');
INSERT INTO `country` VALUES (2172, 0, 'Канада');
INSERT INTO `country` VALUES (582029, 0, 'Карибы');
INSERT INTO `country` VALUES (2297, 0, 'Кипр');
INSERT INTO `country` VALUES (2303, 0, 'Киргызстан');
INSERT INTO `country` VALUES (2374, 0, 'Китай');
INSERT INTO `country` VALUES (582040, 0, 'Корея');
INSERT INTO `country` VALUES (2430, 0, 'Коста-Рика');
INSERT INTO `country` VALUES (582077, 0, 'Куба');
INSERT INTO `country` VALUES (2443, 0, 'Кувейт');
INSERT INTO `country` VALUES (2448, 0, 'Латвия');
INSERT INTO `country` VALUES (2505884, 0, 'Ливан');
INSERT INTO `country` VALUES (582060, 0, 'Ливан');
INSERT INTO `country` VALUES (2509, 0, 'Ливия');
INSERT INTO `country` VALUES (2514, 0, 'Литва');
INSERT INTO `country` VALUES (2614, 0, 'Люксембург');
INSERT INTO `country` VALUES (582041, 0, 'Македония');
INSERT INTO `country` VALUES (277563, 0, 'Малайзия');
INSERT INTO `country` VALUES (582043, 0, 'Мальта');
INSERT INTO `country` VALUES (2617, 0, 'Мексика');
INSERT INTO `country` VALUES (582082, 0, 'Мозамбик');
INSERT INTO `country` VALUES (2788, 0, 'Молдова');
INSERT INTO `country` VALUES (2833, 0, 'Монако');
INSERT INTO `country` VALUES (2687701, 0, 'Монголия');
INSERT INTO `country` VALUES (582065, 0, 'Морокко');
INSERT INTO `country` VALUES (277551, 0, 'Нидерланды');
INSERT INTO `country` VALUES (2837, 0, 'Новая Зеландия');
INSERT INTO `country` VALUES (2880, 0, 'Норвегия');
INSERT INTO `country` VALUES (582051, 0, 'О.А.Э.');
INSERT INTO `country` VALUES (582105, 0, 'Остров Мэн');
INSERT INTO `country` VALUES (582044, 0, 'Пакистан');
INSERT INTO `country` VALUES (582046, 0, 'Перу');
INSERT INTO `country` VALUES (2897, 0, 'Польша');
INSERT INTO `country` VALUES (3141, 0, 'Португалия');
INSERT INTO `country` VALUES (3156, 0, 'Реюньон');
INSERT INTO `country` VALUES (277555, 0, 'Румыния');
INSERT INTO `country` VALUES (5681, 0, 'США');
INSERT INTO `country` VALUES (5647, 0, 'Сальвадор');
INSERT INTO `country` VALUES (277565, 0, 'Сингапур');
INSERT INTO `country` VALUES (582067, 0, 'Сирия');
INSERT INTO `country` VALUES (5666, 0, 'Словакия');
INSERT INTO `country` VALUES (5673, 0, 'Словения');
INSERT INTO `country` VALUES (5678, 0, 'Суринам');
INSERT INTO `country` VALUES (9575, 0, 'Таджикистан');
INSERT INTO `country` VALUES (277567, 0, 'Тайвань');
INSERT INTO `country` VALUES (582050, 0, 'Тайланд');
INSERT INTO `country` VALUES (582090, 0, 'Тунис');
INSERT INTO `country` VALUES (9638, 0, 'Туркменистан');
INSERT INTO `country` VALUES (277569, 0, 'Туркмения');
INSERT INTO `country` VALUES (9701, 0, 'Туркс и Кейкос');
INSERT INTO `country` VALUES (9705, 0, 'Турция');
INSERT INTO `country` VALUES (9782, 0, 'Уганда');
INSERT INTO `country` VALUES (9787, 0, 'Узбекистан');
INSERT INTO `country` VALUES (9908, 0, 'Украина');
INSERT INTO `country` VALUES (10648, 0, 'Финляндия');
INSERT INTO `country` VALUES (10668, 0, 'Франция');
INSERT INTO `country` VALUES (277553, 0, 'Хорватия');
INSERT INTO `country` VALUES (10874, 0, 'Чехия');
INSERT INTO `country` VALUES (582031, 0, 'Чили');
INSERT INTO `country` VALUES (10904, 0, 'Швейцария');
INSERT INTO `country` VALUES (10933, 0, 'Швеция');
INSERT INTO `country` VALUES (582064, 0, 'Эквадор');
INSERT INTO `country` VALUES (10968, 0, 'Эстония');
INSERT INTO `country` VALUES (3661568, 0, 'ЮАР');
INSERT INTO `country` VALUES (11002, 0, 'Югославия');
INSERT INTO `country` VALUES (11014, 0, 'Южная Корея');
INSERT INTO `country` VALUES (582106, 0, 'Ямайка');
INSERT INTO `country` VALUES (11060, 0, 'Япония');
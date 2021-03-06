from django import forms

BUILDING_TYPE = (
    ('NotSpecified', 'Не важно'),
    (' кирпичный ', 'Кирпичный'),
    (' панельный ', 'Панельный'),
    (' блочный ', 'Блочный'),
    (' монолитный ', 'Монолитный'),
    (' деревянный ', 'Деревянный'),
)

ROOMS = (
    ('NotSpecified', 'Не важно'),
    (' студии ', 'Студия'),
    (' своб. планировка ', 'Свободная планировка'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('>9', '>9'),
)

CITIES = (
    ('NotSpecified', 'Не важно'),
    ('mahachkala', 'Махачкала'),
    ('moskva', 'Москва'),
    ('sankt-peterburg', 'Санкт-Петербург'),

)

MOSCOW_STATIONS = (
    ('NotSpecified', 'Не важно'),
    ('Парк Победы', 'Парк Победы'),
    ('Выхино', 'Выхино'),
    ('Киевская', 'Киевская'),
    ('Новокузнецкая', 'Новокузнецкая'),
    ('Крестьянская Застава', 'Крестьянская Застава'),
    ('Выставочная', 'Выставочная'),
    ('Университет', 'Университет'),
    ('Проспект Вернадского', 'Проспект Вернадского'),
    ('ЮгоЗападная', 'ЮгоЗападная'),
    ('Тропарёво', 'Тропарёво'),
    ('Румянцево', 'Румянцево'),
    ('Саларьево', 'Саларьево'),
    ('Филатов Луг', 'Филатов Луг'),
    ('Прокшино', 'Прокшино'),
    ('Ольховая', 'Ольховая'),
    ('Коммунарка', 'Коммунарка'),
    ('Ленинский проспект', 'Ленинский проспект'),
    ('Профсоюзная', 'Профсоюзная'),
    ('Новые Черёмушки', 'Новые Черёмушки'),
    ('Калужская', 'Калужская'),
    ('Беляево', 'Беляево'),
    ('Коньково', 'Коньково'),
    ('Тёплый стан', 'Тёплый стан'),
    ('Ясенево', 'Ясенево'),
    ('Новоясеневская', 'Новоясеневская'),
    ('Войковская', 'Войковская'),
    ('Сокол', 'Сокол'),
    ('Аэропорт', 'Аэропорт'),
    ('Динамо', 'Динамо'),
    ('Белорусская', 'Белорусская'),
    ('Текстильщики', 'Текстильщики'),
    ('Кожуховская', 'Кожуховская'),
    ('Печатники', 'Печатники'),
    ('Волжская', 'Волжская'),
    ('Люблино', 'Люблино'),
    ('Братиславская', 'Братиславская'),
    ('Марьино', 'Марьино'),
    ('Борисово', 'Борисово'),
    ('Шипиловская', 'Шипиловская'),
    ('Зябликово', 'Зябликово'),
    ('Тульская', 'Тульская'),
    ('Нагатинская', 'Нагатинская'),
    ('Нагорная', 'Нагорная'),
    ('Нахимовский проспект', 'Нахимовский проспект'),
    ('Чертановская', 'Чертановская'),
    ('Южная', 'Южная'),
    ('Пражская', 'Пражская'),
    ('Ул Академика Янгеля', 'Ул Академика Янгеля'),
    ('Бульвар Дмитрия Донского', 'Бульвар Дмитрия Донского'),
    ('Ул Старокачаловская', 'Ул Старокачаловская'),
    ('Лесопарковая', 'Лесопарковая'),
    ('Битцевский парк', 'Битцевский парк'),
    ('Бульвар Адмирала Ушакова', 'Бульвар Адмирала Ушакова'),
    ('Адмирала Ушакова', 'Адмирала Ушакова'),
    ('Ул Горчакова', 'Ул Горчакова'),
    ('Бунинская аллея', 'Бунинская аллея'),
    ('Ул Скобелевская', 'Ул Скобелевская'),
    ('Аннино', 'Аннино'),
    ('Севастопольская', 'Севастопольская'),
    ('Орехово', 'Орехово'),
    ('АлмаАтинская', 'АлмаАтинская'),
    ('Коломенская', 'Коломенская'),
    ('Кантемировская', 'Кантемировская'),
    ('Царицыно', 'Царицыно'),
    ('Домодедовская', 'Домодедовская'),
    ('Каширская', 'Каширская'),
    ('Красногвардейская', 'Красногвардейская'),
    ('Технопарк', 'Технопарк'),
    ('Новогиреево', 'Новогиреево'),
    ('Перово', 'Перово'),
    ('Новокосино', 'Новокосино'),
    ('Каховская', 'Каховская'),
    ('Варшавская', 'Варшавская'),
    ('Пл Гагарина', 'Пл Гагарина'),
    ('Гагарина', 'Гагарина'),
    ('Китай город', 'Китай город'),
    ('Цветной бульвар', 'Цветной бульвар'),
    ('Трубная', 'Трубная'),
    ('Маяковская', 'Маяковская'),
    ('Кузнецкий Мост', 'Кузнецкий Мост'),
    ('Мост', 'Мост'),
    ('Тургеневская', 'Тургеневская'),
    ('Краснопресненская', 'Краснопресненская'),
    ('Баррикадная', 'Баррикадная'),
    ('Пушкинская', 'Пушкинская'),
    ('Тверская', 'Тверская'),
    ('Чеховская', 'Чеховская'),
    ('Лубянка', 'Лубянка'),
    ('Третьяковская', 'Третьяковская'),
    ('Чистые пруды', 'Чистые пруды'),
    ('пруды', 'пруды'),
    ('Сретенский бульвар', 'Сретенский бульвар'),
    ('бульвар', 'бульвар'),
    ('Чкаловская', 'Чкаловская'),
    ('Таганская', 'Таганская'),
    ('Марксистская', 'Марксистская'),
    ('Пролетарская', 'Пролетарская'),
    ('Комсомольская', 'Комсомольская'),
    ('Красносельская', 'Красносельская'),
    ('Красные Ворота', 'Красные Ворота'),
    ('Ворота', 'Ворота'),
    ('Сокольники', 'Сокольники'),
    ('Преображенская площадь', 'Преображенская площадь'),
    ('площадь', 'площадь'),
    ('Парк культуры', 'Парк культуры'),
    ('культуры', 'культуры'),
    ('Проспект Мира', 'Проспект Мира'),
    ('Мира', 'Мира'),
    ('Международная', 'Международная'),
    ('Менделеевская', 'Менделеевская'),
    ('Новослободская', 'Новослободская'),
    ('ПетровскоРазумовская', 'ПетровскоРазумовская'),
    ('Академическая', 'Академическая'),
    ('Курская', 'Курская'),
    ('Черкизовская', 'Черкизовская'),
    ('Бульвар Рокоссовского', 'Бульвар Рокоссовского'),
    ('Рокоссовского', 'Рокоссовского'),
    ('Локомотив', 'Локомотив'),
    ('Волгоградский проспект', 'Волгоградский проспект'),
    ('проспект', 'проспект'),
    ('Шоссе Энтузиастов', 'Шоссе Энтузиастов'),
    ('Энтузиастов', 'Энтузиастов'),
    ('Авиамоторная', 'Авиамоторная'),
    ('Новохохловская', 'Новохохловская'),
    ('Угрешская', 'Угрешская'),
    ('Нижегородская', 'Нижегородская'),
    ('Андроновка', 'Андроновка'),
    ('Измайлово', 'Измайлово'),
    ('Соколиная Гора', 'Соколиная Гора'),
    ('Гора', 'Гора'),
    ('Верхние Котлы', 'Верхние Котлы'),
    ('Котлы', 'Котлы'),
    ('Крымская', 'Крымская'),
    ('ЗИЛ', 'ЗИЛ'),
    ('Автозаводская', 'Автозаводская'),
    ('Дубровка', 'Дубровка'),
    ('Кунцевская', 'Кунцевская'),
    ('Молодёжная', 'Молодёжная'),
    ('Крылатское', 'Крылатское'),
    ('Строгино', 'Строгино'),
    ('Волоколамская', 'Волоколамская'),
    ('Митино', 'Митино'),
    ('Пятницкое шоссе', 'Пятницкое шоссе'),
    ('шоссе', 'шоссе'),
    ('Мякинино', 'Мякинино'),
    ('Пионерская', 'Пионерская'),
    ('Филёвский парк', 'Филёвский парк'),
    ('парк', 'парк'),
    ('Багратионовская', 'Багратионовская'),
    ('Фили', 'Фили'),
    ('Славянский бульвар', 'Славянский бульвар'),
    ('бульвар', 'бульвар'),
    ('Кутузовская', 'Кутузовская'),
    ('Деловой', 'Деловой'),
    ('центр', 'центр'),
    ('Щукинская', 'Щукинская'),
    ('Спартак', 'Спартак'),
    ('Тушинская', 'Тушинская'),
    ('Сходненская', 'Сходненская'),
    ('Планерная', 'Планерная'),
    ('Арбатская', 'Арбатская'),
    ('Боровицкая', 'Боровицкая'),
    ('Пл Революции', 'Пл Революции'),
    ('Революции', 'Революции'),
    ('Александровский сад', 'Александровский сад'),
    ('сад', 'сад'),
    ('Библиотека им Ленина', 'Библиотека им Ленина'),
    ('им Ленина', 'им Ленина'),
    ('Ленина', 'Ленина'),
    ('Кропоткинская', 'Кропоткинская'),
    ('Театральная', 'Театральная'),
    ('Охотный Ряд', 'Охотный Ряд'),
    ('Ряд', 'Ряд'),
    ('Смоленская', 'Смоленская'),
    ('Полянка', 'Полянка'),
    ('Октябрьская', 'Октябрьская'),
    ('Добрынинская', 'Добрынинская'),
    ('Серпуховская', 'Серпуховская'),
    ('Павелецкая', 'Павелецкая'),
    ('Сухаревская', 'Сухаревская'),
    ('Рижская', 'Рижская'),
    ('ВДНХ', 'ВДНХ'),
    ('Алексеевская', 'Алексеевская'),
    ('Савёловская', 'Савёловская'),
    ('Дмитровская', 'Дмитровская'),
    ('Достоевская', 'Достоевская'),
    ('Марьина Роща', 'Марьина Роща'),
    ('Роща', 'Роща'),
    ('Бутырская', 'Бутырская'),
    ('Тимирязевская', 'Тимирязевская'),
    ('Фонвизинская', 'Фонвизинская'),
    ('Владыкино', 'Владыкино'),
    ('Отрадное', 'Отрадное'),
    ('Бибирево', 'Бибирево'),
    ('Алтуфьево', 'Алтуфьево'),
    ('Лихоборы', 'Лихоборы'),
    ('Коптево', 'Коптево'),
    ('Балтийская', 'Балтийская'),
    ('Стрешнево', 'Стрешнево'),
    ('Панфиловская', 'Панфиловская'),
    ('Полежаевская', 'Полежаевская'),
    ('Беговая', 'Беговая'),
    ('Улица', 'Улица'),
    ('года', 'года'),
    ('Октябрьское Поле', 'Октябрьское Поле'),
    ('Поле', 'Поле'),
    ('Зорге', 'Зорге'),
    ('Хорошёво', 'Хорошёво'),
    ('Шелепиха', 'Шелепиха'),
    ('Студенческая', 'Студенческая'),
    ('Спортивная', 'Спортивная'),
    ('Фрунзенская', 'Фрунзенская'),
    ('Лужники', 'Лужники'),
    ('Воробьёвы горы', 'Воробьёвы горы'),
    ('горы', 'горы'),
    ('Шаболовская', 'Шаболовская'),
    ('Водный стадион', 'Водный стадион'),
    ('стадион', 'стадион'),
    ('Речной вокзал', 'Речной вокзал'),
    ('вокзал', 'вокзал'),
    ('Беломорская', 'Беломорская'),
    ('Медведково', 'Медведково'),
    ('Бабушкинская', 'Бабушкинская'),
    ('Свиблово', 'Свиблово'),
    ('Ботанический сад', 'Ботанический сад'),
    ('сад', 'сад'),
    ('Бауманская', 'Бауманская'),
    ('Электрозаводская', 'Электрозаводская'),
    ('Семёновская', 'Семёновская'),
    ('Измайловская', 'Измайловская'),
    ('Первомайская', 'Первомайская'),
    ('Щёлковская', 'Щёлковская'),
    ('Партизанская', 'Партизанская'),
    ('Римская', 'Римская'),
    ('Площадь Ильича', 'Площадь Ильича'),
    ('Ильича', 'Ильича'),
    ('Лермонтовский проспект', 'Лермонтовский проспект'),
    ('проспект', 'проспект'),
    ('Рязанский проспект', 'Рязанский проспект'),
    ('проспект', 'проспект'),
    ('Кузьминки', 'Кузьминки'),
    ('Жулебино', 'Жулебино'),
    ('Котельники', 'Котельники'),
    ('Ростокино', 'Ростокино'),
    ('Белокаменная', 'Белокаменная'),
    ('Ломоносовский проспект', 'Ломоносовский проспект'),
    ('проспект', 'проспект'),
    ('Минская', 'Минская'),
    ('Ховрино', 'Ховрино'),
    ('ЦСКА', 'ЦСКА'),
    ('Хорошёвская', 'Хорошёвская'),
    ('Петровский', 'Петровский'),
    ('парк', 'парк'),
    ('Верхние', 'Верхние'),
    ('Лихоборы', 'Лихоборы'),
    ('Селигерская', 'Селигерская'),
    ('Окружная', 'Окружная'),
    ('Деловой', 'Деловой'),
    ('Центр МЦК', 'Центр МЦК'),
    ('МЦК', 'МЦК'),
    ('Раменки', 'Раменки'),
    ('Мичуринский проспект', 'Мичуринский проспект'),
    ('проспект', 'проспект'),
    ('Озёрная', 'Озёрная'),
    ('Говорово', 'Говорово'),
    ('Солнцево', 'Солнцево'),
    ('Боровское шоссе', 'Боровское шоссе'),
    ('шоссе', 'шоссе'),
    ('Новопеределкино', 'Новопеределкино'),
    ('Рассказовка', 'Рассказовка'),
    ('Косино', 'Косино'),
    ('Улица', 'Улица'),
    ('Дмитриевского', 'Дмитриевского'),
    ('Лухмановская', 'Лухмановская'),
    ('Некрасовка', 'Некрасовка'),
)

SPB_STATIONS = (
    ('NotSpecified', 'Не важно'),
    ('Звен,игородская', 'Звенигородская'),
    ('Обводный канал', 'Обводный канал'),
    ('Волковская', 'Волковская'),
    ('Бухарестская', 'Бухарестская'),
    ('Международная', 'Международная'),
    ('Сенная площадь', 'Сенная площадь'),
    ('Фрунзенская', 'Фрунзенская'),
    ('Московские ворота', 'Московские ворота'),
    ('Электросила', 'Электросила'),
    ('Парк Победы', 'Парк Победы'),
    ('Московская', 'Московская'),
    ('Звёздная', 'Звёздная'),
    ('Купчино', 'Купчино'),
    ('Девяткино', 'Девяткино'),
    ('Гражданский проспект', 'Гражданский проспект'),
    ('Академическая', 'Академическая'),
    ('Политехническая', 'Политехническая'),
    ('Площадь Мужества', 'Площадь Мужества'),
    ('Лесная', 'Лесная'),
    ('Выборгская', 'Выборгская'),
    ('Площадь Ленина', 'Площадь Ленина'),
    ('Чернышевская', 'Чернышевская'),
    ('Площадь Восстания', 'Площадь Восстания'),
    ('Владимирская', 'Владимирская'),
    ('Пушкинская', 'Пушкинская'),
    ('Балтийская', 'Балтийская'),
    ('институт', 'институт'),
    ('Нарвская', 'Нарвская'),
    ('Кировский завод', 'Кировский завод'),
    ('Автово', 'Автово'),
    ('Ленинский проспект', 'Ленинский проспект'),
    ('Проспект Ветеранов', 'Проспект Ветеранов'),
    ('Достоевская', 'Достоевская'),
    ('проспект', 'проспект'),
    ('Невского', 'Невского'),
    ('Новочеркасская', 'Новочеркасская'),
    ('Ладожская', 'Ладожская'),
    ('Большевиков', 'Большевиков'),
    ('Улица Дыбенко', 'Улица Дыбенко'),
    ('Парнас', 'Парнас'),
    ('Проспект Просвещения', 'Проспект Просвещения'),
    ('Озерки', 'Озерки'),
    ('Удельная', 'Удельная'),
    ('Пионерская', 'Пионерская'),
    ('Чёрная речка', 'Чёрная речка'),
    ('Петроградская', 'Петроградская'),
    ('Горьковская', 'Горьковская'),
    ('Спасская', 'Спасская'),
    ('Невский проспект', 'Невский проспект'),
    ('Новокрестовская', 'Новокрестовская'),
    ('Беговая', 'Беговая'),
)

MAKHACHKALA_DISTRICTS = (
    ('NotSpecified', 'Не важно'),
    ('р-н Кировский', 'р-н Кировский'),
    ('р-н Советский', 'р-н Советский'),
    ('р-н Ленинский', 'р-н Ленинский'),
)


class FilterForm(forms.Form):
    region = forms.ChoiceField(choices=CITIES, required=False, label='Город')
    building_type = forms.ChoiceField(choices=BUILDING_TYPE, required=False, label='Тип здания')
    rooms = forms.ChoiceField(choices=ROOMS, required=False, label='Количество комнат')
    floor = forms.CharField(max_length=3, required=False, label='Этаж')
    floors_amount = forms.CharField(max_length=3, required=False, label='Этажей в здании')
    district = forms.ChoiceField(choices=MAKHACHKALA_DISTRICTS, required=False, label='Район')
    moscow_stations = forms.ChoiceField(choices=MOSCOW_STATIONS, required=False, label='Станция Метро')
    spb_stations = forms.ChoiceField(choices=SPB_STATIONS, required=False, label='Станция Метро')
    square_min = forms.CharField(required=False, label='')
    square_max = forms.CharField(required=False, label='')

    coors = forms.CharField(max_length=300, required=False, label='Координаты')

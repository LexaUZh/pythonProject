#-*- coding: cp1251 -*-
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 450)

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.toolbar import MDToolbar
from kivy.clock import Clock
from kivy.uix.switch import Switch
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.toast import toast
from kivy.core.audio import SoundLoader
import random
container7 = '''
BoxLayout:
    orientation: "vertical"
    MDToolbar:
        left_action_items: [["arrow-left-bold",lambda x: app.mediator4.d5()]]
        md_bg_color: 1,0.5,0,1
        size_hint_y: 0.06
    Button:
        text: "start"
        on_press: app.mediator4.notify("d6",self)
'''
container6 = '''
BoxLayout:
    orientation : "vertical"
    Mytextinput:
        hint_text: "Введите количество примеров: "
        on_text:  app.mediator4.notify("d3",self.text)
    Button:
        text: "Режим: +3"
        on_press: app.mediator4.notify("d2",self)
    Button:
        text: "ok"
        on_press: app.mediator4.notify("d4")        
'''
container5 = '''
BoxLayout:
    orientation: "vertical"
    BoxLayout:
        size_hint_y : 0.5
        orientation: "horizontal"
        Label:
            text: "Количество слов: "
        Mytextinput:
            hint_text: "По умолчанию 10"
            on_text: app.mediator3.notify("c9",self)
    BoxLayout:
        orientation: "horizontal"
        Label:
            text: "На время: "
        Switch:
            on_active: app.mediator3.notify("c2",self.active,self.parent.parent)
    BoxLayout:
        size_hint_y: 0.6
        orientation: "horizontal"
        Label:
            text: "Числа: "
        Spinner:
            text: "нет"
            values: ("нет","до 100","до 1000","до 10000")
            on_text: app.mediator3.main_parameters.update({'numbers': self.text[3:]})
    Button:
        size_hint_y: 0.7
        text: "ok"
        on_press: app.mediator3.notify("c3")
'''
container4 = '''
GridLayout:
    cols:1
    size_hint_y: 0.65
    BoxLayout:
        Label:
            text: "Сложение: "
        CheckBox:
            id: cb1
            on_active: app.mediator2.main_parameters.update({'addition': self.active})
            active:  True
    BoxLayout:
        Label:
            text: "Вычитание: "
        CheckBox:
            on_active: app.mediator2.main_parameters.update({'subtraction': self.active})
            active:  True
            id: cb2
    BoxLayout:
        Label:
            text: "Деление: "
        CheckBox:
            on_active: app.mediator2.main_parameters.update({'multiplication': self.active})
            active:  True
            id: cb3 
    BoxLayout:
        Label:
            text: "Умножение: "
        CheckBox:
            on_active: app.mediator2.main_parameters.update({'division': self.active})
            active:  True
            id: cb4
'''
container3 = '''
ScrollView:
    BoxLayout:
        id: box
        adaptive_height: True
        orientation: "vertical"
        BoxLayout:
            size_hint_y: 0.3
            Label:
                text: "Область чисел"
            Spinner:
                text: "до 100"
                values: ("до 10","до 100","до 1000","до 10000")
                on_text: app.mediator2.main_parameters.update({'area_num': self.text[3:]})
        BoxLayout:
            size_hint_y: 0.3
            Label:
                text: "Дробные числа: "
            Spinner:
                text: "нет"
                values: ("нет","до 0.1","до 0.01","до 0.001")
                on_text: app.mediator2.main_parameters.update({'fraction': self.text[3:]})
        BoxLayout:
            size_hint_y: 0.2
            Label:
                text: "В столбик: "
            Switch:
                on_active: app.mediator2.main_parameters.update({'colm': self.active})
        Button:
            size_hint_y: 0.2
            text: "OK"
            on_press: app.mediator2.notify("a2")
'''
container2 = '''
BoxLayout:
    orientation: 'vertical'
    Label:
        text: "Время вышло!"
    Button:
        size_hint_y: 0.2
        text:"ок"
        on_press: app.popups["popup2"].dismiss()
'''
container1 = '''
BoxLayout:
    orientation: "vertical"
    Spinner:
        text: "Размер таблицы"
        values: ("25","50","75","81")
        on_text: app.mediator.main_parameters["tablesize"] = self.text
    Spinner:
        id: spin1
        text: "Введите время"
        values: ("Не ограниченно","ограниченно")
        on_text: app.mediator.notify("b4",self.text,self.parent)
    Label:
        size_hint_y: 0.1
    Button:
        text:"OK"
        on_press: app.mediator.notify("b2")
'''
container = ('''
ScreenManager:
    Screen:
        name: "main"
        BoxLayout:
            orientation: "vertical"
            Button:
                text: 'Тренажёр Шульте.'
                on_press: app.mediator.notify("b1")
            Button:
                text: 'Счёт.'
                on_press: app.mediator2.notify("a1")
            Button:
                text: 'запоминание.'
                on_press: app.mediator3.notify("c1")
            Button:
                text: '+3 / +1'
                on_press: app.mediator4.notify("d1")         
    Screen:
        name: "notmain1"
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                id:toolbar2
                md_bg_color: 1,0.5,0,1
                left_action_items:[["arrow-left-bold",lambda x: app.mediator.notify("b3","stop_clock")]]
                size_hint_y: 0.06
            GridLayout:
                rows: 5
                cols: 5   
''')
LIST3 = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место', 'вопрос', 'лицо', 'глаз', 'страна', 'друг', 'сторона', 'дом', 'случай', 'ребенок', 'голова',
         'система', 'вид', 'конец', 'отношение', 'город', 'часть', 'женщина', 'проблема', 'земля', 'решение', 'власть', 'машина', 'закон', 'час', 'образ', 'отец', 'история', 'нога', 'вода',
         'война', 'возможность', 'компания', 'результат', 'дверь', 'рог', 'народ', 'область', 'число', 'голос', 'развитие', 'группа', 'жена', 'процесс', 'условие', 'книга', 'ночь', 'суд',
         'деньга', 'уровень', 'начало', 'государство', 'стол', 'средство', 'связь', 'имя', 'президент', 'форма', 'путь', 'организация', 'качество', 'действие', 'статья', 'общество',
         'ситуация', 'деятельность', 'школа', 'душа', 'дорога', 'язык', 'взгляд', 'момент', 'минута', 'месяц', 'порядок', 'цель', 'программа', 'муж', 'помощь', 'мысль', 'вечер', 'орган',
         'правительство', 'рынок', 'предприятие', 'партия', 'роль', 'смысл', 'мама', 'мера', 'улица', 'состояние', 'задача', 'информация', 'театр', 'внимание', 'производство', 'квартира',
         'труд', 'тело', 'письмо', 'центр', 'утро', 'мать', 'комната', 'семья', 'сын', 'смерть', 'положение', 'интерес', 'федерация', 'век', 'идея', 'управление', 'автор', 'окно', 'ответ',
         'совет', 'разговор', 'мужчина', 'ряд', 'счет', 'мнение', 'цена', 'точка', 'план', 'проект', 'глава', 'материал', 'основа', 'причина', 'движение', 'культура', 'сердце', 'рубль',
         'наука', 'документ', 'неделя', 'вещь', 'чувство', 'правило', 'служба', 'газета', 'срок', 'институт', 'змея', 'ход', 'стена', 'директор', 'плечо', 'опыт', 'встреча', 'принцип',
         'событие', 'структура', 'количество', 'товарищ', 'создание', 'значение', 'объект', 'гражданин', 'очередь', 'период', 'образование', 'состав', 'пример', 'лес', 'исследование',
         'девушка', 'данные', 'палец', 'судьба', 'тип', 'метод', 'политика', 'армия', 'брат', 'представитель', 'борьба', 'использование', 'шаг', 'игра', 'участие',
         'территория', 'край', 'размер', 'номер', 'район', 'население', 'банк', 'начальник', 'класс', 'зал', 'изменение', 'большинство', 'характер', 'кровь', 'направление', 'позиция',
         'герой', 'течение', 'девочка', 'искусство', 'гость', 'воздух', 'мальчик', 'фильм', 'договор', 'регион', 'выбор', 'свобода', 'врач', 'экономика', 'небо', 'факт',
         'церковь', 'завод', 'фирма', 'бизнес', 'союз', 'деньги', 'специалист', 'род', 'команда', 'руководитель', 'спина', 'дух', 'музыка', 'способ', 'хозяин', 'поле', 'доллар',
         'память', 'природа', 'дерево', 'оценка', 'объем', 'картина', 'процент', 'требование', 'писатель', 'сцена', 'анализ', 'основание', 'повод', 'вариант', 'берег', 'модель',
         'степень', 'самолет', 'телефон', 'граница', 'песня', 'половина', 'министр', 'угол', 'зрение', 'предмет', 'литература', 'операция', 'двор', 'спектакль', 'руководство',
         'солнце', 'автомобиль', 'родитель', 'участник', 'журнал', 'база', 'пространство', 'защита', 'название', 'стих', 'ум', 'море', 'удар', 'знание', 'солдат', 'миллион',
         'строительство', 'технология', 'председатель', 'сон', 'сознание', 'бумага', 'реформа', 'оружие', 'линия', 'текст', 'выход', 'ребята', 'магазин', 'соответствие', 'участок',
         'услуга', 'поэт', 'предложение', 'желание', 'пара', 'успех', 'среда', 'возраст', 'комплекс', 'бюджет', 'представление', 'площадь', 'генерал', 'господин', 'дочь', 'понятие',
         'кабинет', 'безопасность', 'фонд', 'сфера', 'папа', 'сотрудник', 'продукция', 'будущее', 'продукт', 'содержание', 'художник', 'республика', 'сумма', 'контроль', 'парень',
         'ветер', 'хозяйство', 'помочь', 'курс', 'губа', 'река', 'грудь', 'огонь', 'нос', 'волос', 'ухо', 'отсутствие', 'радость', 'сад', 'подготовка', 'необходимость', 'доктор', 'лето',
         'камень', 'здание', 'капитан', 'собака', 'итог', 'рис', 'техника', 'элемент', 'источник', 'деревня', 'депутат', 'проведение', 'рот', 'масса', 'комиссия', 'цвет', 'рассказ',
         'функция', 'определение', 'мужик', 'обеспечение', 'обстоятельство', 'работник', 'разработка', 'лист', 'звезда', 'гора', 'применение', 'победа', 'товар', 'воля', 'зона', 'предел',
         'целое', 'личность', 'офицер', 'влияние', 'поддержка', 'ответственность', 'цветок', 'праздник', 'немец', 'бой', 'сестра', 'господь', 'учитель', 'многое', 'рамка',
         'практика', 'показатель', 'метр', 'войско', 'частность', 'особенность', 'снег', 'комитет', 'налог', 'акт', 'отдел', 'карман', 'вывод', 'норма', 'читатель', 'этап',
         'сравнение', 'прошлое', 'фамилия', 'кухня', 'заявление', 'доля', 'пункт', 'студент', 'учет', 'впечатление', 'доход', 'вирус', 'клетка', 'удовольствие', 'теория', 'враг', 'собрание',
         'бутылка', 'расчет', 'го', 'режим', 'множество', 'клуб', 'попытка', 'зуб', 'сеть', 'семь', 'министерство', 'прием', 'боль', 'сожаление', 'кожа', 'субъект', 'знак', 'актер', 'ресурс',
         'акция', 'газ', 'журналист', 'звук', 'передача', 'здоровье', 'администрация', 'болезнь', 'детство', 'мастер', 'выборы', 'зима', 'подход', 'поиск', 'механизм', 'выражение', 'скорость',
         'ощущение', 'стоимость', 'коридор', 'ошибка', 'лидер', 'карта', 'заседание', 'глубина', 'хлеб', 'поверхность', 'энергия', 'нарушение', 'реализация', 'революция', 'поведение', 'профессор',
         'исполнение', 'заместитель', 'суть', 'станция', 'реакция', 'десяток', 'столица', 'формирование', 'поколение', 'дума', 'существование', 'продажа', 'список', 'способность',
         'противник', 'схема', 'долг', 'режиссер', 'отличие', 'колено', 'дед', 'свойство', 'этаж', 'секунда', 'фактор', 'житель', 'явление', 'высота', 'сосед', 'усилие', 'рождение',
         'расход', 'остров', 'фигура', 'наличие', 'дядя', 'милиция', 'растение', 'существо', 'черт', 'бабушка', 'законодательство', 'собственность', 'отрасль', 'слеза', 'волна', 'стекло',
         'традиция', 'январь', 'оборудование', 'зависимость', 'фраза', 'декабрь', 'сведение', 'трубка', 'сентябрь', 'университет', 'командир', 'храм', 'повышение', 'стиль', 'артист',
         'больница', 'одежда', 'охрана', 'водка', 'кодекс', 'имущество', 'птица', 'переход', 'красота', 'клиент', 'толпа', 'адрес', 'отделение', 'октябрь', 'чудо', 'счастие', 'улыбка',
         'ужас', 'аппарат', 'корабль', 'родина', 'животное', 'черта', 'известие', 'понимание', 'тень', 'апрель', 'коллега', 'преступление', 'рыба', 'кресло', 'запах', 'выставка', 'князь',
         'фотография', 'весна', 'помещение', 'эпоха', 'занятие', 'произведение', 'концерт', 'ладонь', 'дама', 'сомнение', 'американец', 'середина', 'зарплата', 'тайна', 'запад', 'июнь',
         'беседа', 'фронт', 'поезд', 'должность', 'баба', 'промышленность', 'музей', 'судья', 'получение', 'полковник', 'зритель', 'секретарь', 'установка', 'поток', 'ценность', 'образец',
         'страница', 'перспектива', 'трава', 'чиновник', 'мозг', 'сотня', 'лагерь', 'выступление', 'оборона', 'постановление', 'честь', 'настроение', 'кровать', 'характеристика',
         'обязанность', 'шея', 'крыша', 'появление', 'учреждение', 'признак', 'труба', 'жертва', 'беда', 'фон', 'организм', 'ученик', 'заключение', 'выполнение', 'канал', 'исключение',
         'дача', 'соглашение', 'осень', 'польза', 'стул', 'июль', 'дождь', 'сутки', 'еврей', 'конкурс', 'открытие', 'телевизор', 'лошадь', 'температура', 'приказ', 'лестница', 'реклама',
         'спор', 'подруга', 'угроза', 'конфликт', 'изучение', 'вино', 'концепция', 'достижение', 'сообщение', 'объединение', 'обстановка', 'костюм', 'ключ', 'ресторан', 'назначение',
         'царь', 'воспоминание', 'увеличение', 'вкус', 'мероприятие', 'лоб', 'слой', 'восток', 'последствие', 'принятие', 'сотрудничество', 'нефть', 'слух', 'бок', 'переговоры', 'тюрьма',
         'кандидат', 'просьба', 'реальность', 'подарок', 'категория', 'потребность', 'быль', 'редакция', 'очко', 'километр', 'губернатор', 'новость', 'инструмент', 'потеря',
         'взаимодействие', 'звонок', 'кусок', 'капитал', 'крыса', 'перевод', 'партнер', 'ноябрь', 'молодежь', 'тишина', 'творчество', 'книжка', 'мясо', 'масло', 'деталь', 'инженер',
         'оплата', 'эксперт', 'кремль', 'февраль', 'следствие', 'пьеса', 'билет', 'урок', 'коллектив', 'устройство', 'палата', 'площадка', 'опасность', 'пропасть', 'воздействие', 'разница',
         'родственник', 'сезон', 'издание', 'человечество', 'снижение', 'запас', 'крик', 'публика', 'вещество', 'экран', 'эффект', 'ящик', 'ракета', 'водитель', 'пакет', 'зеркало', 'вес',
         'дно', 'вагон', 'убийство', 'тон', 'щека', 'дурак', 'длина', 'давление', 'двигатель', 'камера', 'обращение', 'формула', 'запись', 'крыло', 'поездка', 'гостиница', 'колесо',
         'разрешение', 'торговля', 'академия', 'доклад', 'общение', 'присутствие', 'процедура', 'испытание', 'нож', 'проверка', 'коммунист', 'цифра', 'полет', 'стакан', 'эффективность', 'обучение', 'портрет', 'достоинство', 'рассмотрение', 'владелец', 'жилье', 'компьютер', 'корень', 'смена', 'доказательство', 'кадр', 'лейтенант', 'признание', 'темнота', 'пистолет', 'наблюдение', 'мост', 'ремонт', 'истина', 'вход', 'политик', 'живот', 'кредит', 'шум', 'обед', 'недостаток', 'памятник', 'вершина', 'серия', 'эксперимент', 'сущность', 'транспорт', 'инициатива', 'активность', 'конференция', 'кулак', 'доска', 'ожидание', 'платье', 'смех', 'отказ', 'сбор', 'пенсия', 'буква', 'порог', 'автобус', 'воспитание', 'производитель', 'полоса', 'риск', 'пиво', 'корпус', 'штаб', 'кольцо', 'постель', 'выпуск', 'дворец', 'брак', 'прокурор', 'печать', 'окончание', 'автомат', 'тенденция', 'следователь', 'штат', 'куст', 'старуха', 'описание', 'психология', 'шутка', 'съезд', 'ставка', 'забота', 'величина', 'версия', 'мешок', 'конструкция', 'контакт', 'шанс', 'лодка', 'редактор', 'заказ', 'кофе', 'рубеж', 'статус', 'спорт', 'покой', 'кризис', 'взрыв', 'профессия', 'дым', 'металл', 'сапог', 'диван', 'интернет', 'почва', 'лед', 'подразделение', 'минимум', 'конь', 'дружба', 'вина', 'замок', 'мечта', 'сигнал', 'талант', 'мгновение', 'столик', 'затрата', 'золото', 'миг', 'плата', 'подъезд', 'масштаб', 'обсуждение', 'сделка', 'обязательство', 'расстояние', 'отдых', 'телевидение', 'тетя', 'яблоко', 'свидетель', 'монастырь', 'чтение', 'параметр', 'кампания', 'помощник', 'полк', 'мощность', 'сюжет', 'потолок', 'регистрация', 'майор', 'эксплуатация', 'озеро', 'новое', 'атмосфера', 'премия', 'совесть', 'предприниматель', 'мальчишка', 'дочка', 'приятель', 'начальство', 'препарат', 'село', 'обработка', 'танк', 'милиционер', 'ручка', 'возвращение', 'прокуратура', 'ворота', 'молоко', 'еда', 'сказка', 'краска', 'хвост', 'сигарета', 'введение', 'покупатель', 'поворот', 'москвич', 'ограничение', 'инвестиция', 'нация', 'набор', 'поселок', 'дыхание', 'адвокат', 'сумка', 'пресса', 'корреспондент', 'песок', 'удивление', 'потребитель', 'указание', 'изображение', 'счастье', 'мэр', 'согласие', 'действительность', 'планета', 'агентство', 'танец', 'библиотека', 'финансирование', 'объяснение', 'распределение', 'конституция', 'таблица', 'поэзия', 'термин', 'прибыль', 'стандарт', 'восторг', 'гибель', 'изделие', 'темп', 'вооружение',
         'осуществление', 'уход', 'чемпионат', 'яблоко', 'контракт', 'философия', 'горло', 'малина', 'кость', 'ведомство', 'преимущество', 'мина', 'полномочие']
#метод для создания таблицы Шульте
def generate1(row,col,a):
    gl = Mediator1._root.screens[1].children[0].children[0]
    gl.rows = row
    gl.cols = col
    lst = [str(x) for x in range(1, a)]
    random.shuffle(lst)
    for x in range(1, a):
        k = lst.pop()
        gl.add_widget(Button(background_color=(0,0,0,1),text = k))
    return None
def generate2(quan):
    lst = []
    for i in range(quan):
        lst.append(random.randint(1000,9998))
    return lst
class MyLabel(Label):
   def on_size(self, *args):
      self.text_size = self.size
# TextInput which can  only contain integer
class Mytextinput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if substring.isdigit() == True:
            return super().insert_text(substring, from_undo=from_undo)
class Image2Builder:
    instruction = None
    @staticmethod
    def update_instruction(parameters):
        Image2Builder.instruction = parameters
    def create_basescreen(self):
        screen = Baseimagescreen2()#
        Mediator2._root.add_widget(screen)#
        scr = Mediator2._root.get_screen("img2")
        Mediator1._root.transition.direction = "left"
        return scr
    def get_exm(self,scr):# для получения самого примера и работы с ним
        label,example,txt = self.generate_exm(Image2Builder.instruction)
        if len(scr.children[0].children[-1].children) != 2:
            scr.children[0].children[-1].add_widget(label)
        else:
            scr.children[0].children[-1].children[0].text = txt
        Mediator2.current_exm = example
        return None
    @staticmethod
    def generate_exm(instruction): # метод для создания примера с учётом инструкций
        inst = instruction
        symbols = ['+','-','/','*']
        i = 0
        index_on_del = []
        for k in list(inst.values())[3:]:
            if k == False:
                index_on_del.append(i)
            i += 1
        index_on_del = list(reversed(index_on_del))#чтоб удалять индексы с конца,чтоб длина списка и число индекса вместе уменьшались
        if len(index_on_del) == 4:
            index_on_del.pop(-1)
        if instruction["fraction"] == 'нет':
            number1 = random.randint(1,int(instruction["area_num"]))
            number2 = random.randint(1,int(instruction["area_num"]))
        else:
            number1 = random.randint(1, int(instruction["area_num"])) + round(random.random(),int(len(instruction['fraction']))-2)
            number2 = random.randint(1, int(instruction["area_num"])) + round(random.random(),int(len(instruction['fraction']))-2)
        for  i in index_on_del:
            symbols.pop(i)
        func =random.choice(symbols)
        example = str(number1) + " " + func + " " + str(number2)
        if instruction['colm'] == False:
            text ="[size=35]" + example
        else:
            text = "[size=35]" + str(number1) +"\n"+ func + "\n" + str(number2)
        exm = Label(text=text,color =(0,0,0,1), halign= 'right',markup = True, pos_hint={'x':0, 'y':0.1})
        return exm,example,text
class Baseimagescreen2(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name ="img2"
        root = BoxLayout(orientation="vertical")
        fllay = FloatLayout()
        root.add_widget(fllay)
        self.ti = TextInput(hint_text = "Ответ: ", size_hint_y=0.08)
        b1 = Button(text="ок", on_press = lambda x: MainApp.mediator2.notify("a5",self))
        boxlay = BoxLayout(size_hint_y=0.2)
        boxlay.add_widget(b1)
        b3 = Button(text="<--", pos_hint={'x':0, 'y':0.93},size_hint=(0.07,0.07),on_press = lambda x: MainApp.mediator2.notify("a4",self))
        fllay.add_widget(b3)
        root.add_widget(self.ti)
        root.add_widget(boxlay)
        self.add_widget(root)
class Mediator():
    main_parameters = {}
    activators = {}
    _root = None
    def notify(self,id, *args):
        self.activators[id].__func__(*args)
        return None
class Mediator2(Mediator):
    main_parameters = {'area_num': '100','fraction': 'нет','colm': False,'addition': True,'subtraction': True,'multiplication' : True,'division' : True}# строго нежелательно менять последовательность ключей и значений
    status_of_exm = "question"
    extra_widgets = {"button_next" : Button(text = "NEXT"),'answer_input' : TextInput(text ="Правильный ответ: ",size_hint_y = 0.1)}
    current_exm = None
    imagebuilder =Image2Builder()
    @staticmethod
    def a1():
        MainApp.show_popup3()
        return None
    @staticmethod
    def a2():
        MainApp.popups["popup3"].dismiss()
        Mediator2.imagebuilder.update_instruction(Mediator2.main_parameters)
        if not(r"<Screen name='img2'>") in [str(x) for x in Mediator2._root.screens]:
            scr = Mediator2.imagebuilder.create_basescreen() # создаём общий вид окна
        else:
            scr = Mediator2._root.get_screen("img2")
            Mediator1._root.transition.direction = "left"
        Mediator2._root.current = "img2"
        Mediator2.imagebuilder.get_exm(scr)# добавляем туда label с примером или просто меняем текст label
        return None
    @staticmethod
    def a4(scr):
        Mediator2._root.current = "main"
        Mediator2._root.transition.direction = "right"
        Mediator2._a6(scr)
        scr.children[0].children[-1].remove_widget(scr.children[0].children[-1].children[0])
        #Mediator2._root.screens[-1].children[0].children[-1].children[0].text = ""
        return None
    @staticmethod
    def a5(scr):  #для добавления виджетов с правильным ответом
        Mediator2.status_of_exm = "question" if  Mediator2.status_of_exm == "answer" else  "answer"
        if Mediator2.status_of_exm == "answer":
            Mediator2.extra_widgets["button_next"].bind(on_press = lambda x: Mediator2.notify(Mediator2,"a7",scr))
            scr.children[0].children[0].add_widget(Mediator2.extra_widgets["button_next"])
            round_num = (len(Mediator2.main_parameters["fraction"])-2) if Mediator2.main_parameters["fraction"] != 'нет' else 2
            Mediator2.extra_widgets["answer_input"].text += str(round(eval(Mediator2.current_exm),round_num))
            scr.children[0].add_widget(Mediator2.extra_widgets["answer_input"],-2)
        else:
            Mediator2._a6(scr)
        return None
    @staticmethod
    def a7(scr): #метод, перелистывающий на следующий пример
        Mediator2._a6(scr)
        Mediator2.imagebuilder.get_exm(scr)
        scr.children[0].children[1].text =""
        return None
    activators = {"a1" : a1,"a2" : a2,"a4" : a4,"a5" : a5,"a7" : a7}
    @staticmethod
    def _a6(scr):
        Mediator2.status_of_exm = "question"
        Mediator2.extra_widgets["answer_input"].text = "Правильный ответ: "
        scr.children[0].children[0].remove_widget(Mediator2.extra_widgets["button_next"])
        scr.children[0].remove_widget(Mediator2.extra_widgets["answer_input"])
        return None
class Mediator1(Mediator):
    main_parameters = {"tablesize": "25", "istime": False}
    time = 0
    clockevent = None
    #вывод таблицы Шульте на экран
    @staticmethod
    def create_window1(*args):
        if MainApp.mediator.main_parameters["tablesize"] == "25":
            generate1(5, 5, 26)
        elif MainApp.mediator.main_parameters["tablesize"] == "50":
            generate1(10, 5, 51)
        elif MainApp.mediator.main_parameters["tablesize"] == "75":
            generate1(15, 5, 76)
        elif MainApp.mediator.main_parameters["tablesize"] == "81":
            generate1(9, 9, 82)
        Mediator1._root.transition.direction = "left"
        Mediator1._root.current = "notmain1"
        if MainApp.mediator.main_parameters["istime"] == True:
            Mediator1.clockevent = Clock.schedule_once(MainApp.show_popup2,*args)
        return None
    #метод для установки времени Таблицы шульте
    @staticmethod
    def set_time(*args):
        Mediator1.time = int(args[1])
        return None
    @staticmethod
    def b1():
        MainApp.show_popup1()
        return None
    # метод для включения таблиц Шульте в зависимости от выбора режима
    @staticmethod
    def b2():
        MainApp.popups["popup1"].dismiss()
        if MainApp.mediator.main_parameters["istime"] == False:
            Mediator1.create_window1()
        else:
            Mediator1.create_window1(Mediator1.time)
            Mediator1.time = 1
        return None
    # метод для возвращения на главный экран
    @staticmethod
    def b3(*args):
        if Mediator1.main_parameters["istime"] == True:
            Mediator1.main_parameters["istime"] = False
            Clock.unschedule(Mediator1.clockevent)
        Mediator1._root.current = "main"
        Mediator1._root.transition.direction = "right"
        Mediator1._root.screens[1].children[0].children[0].clear_widgets()
        return None
    #метод, динамически вызывающийся при настройки таблицы Шульте
    @staticmethod
    def b4(word,bl):
        l = Mytextinput(hint_text="Введите время: ",multiline = False)
        l.bind(text = Mediator1.set_time)
        if word == "Не ограниченно":
            MainApp.mediator.main_parameters["istime"] = False
            #проверка чтоб не убрать чего нужного
            if str(type(bl.children[1])) != "<class 'kivy.uix.label.Label'>":
                #убирать доп строку настройки
                bl.remove_widget(bl.children[1])
            return None
        else:
            MainApp.mediator.main_parameters["istime"] = True
            bl.add_widget(l,1)
            return None
    activators = {"b1": b1, "b2": b2, "b3": b3, "b4": b4}
class Basetaskscreen3(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name ="words3"
        self.scroll = ScrollView(size_hint=(1,1))
        root = BoxLayout(orientation="vertical")
        boxlay = BoxLayout(size_hint_y=0.2)
        b3 = Button(text="<--", on_press=lambda x: MainApp.mediator3.notify("c4"))
        boxlay.add_widget(b3)
        b1 = Button(text="проверка", on_press = lambda x:MainApp.mediator3.notify("c5"))
        boxlay.add_widget(b1)
        root.add_widget(self.scroll)
        root.add_widget(boxlay)
        self.add_widget(root)
class Notbasetaskscreen3(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "checkword3"
        root = BoxLayout(orientation = "vertical")
        self.scroll = ScrollView(size_hint=(1, 1),do_scroll_y= True)
        self.scroll2 = ScrollView(size_hint=(1, 1), do_scroll_y=True)
        ti = TextInput(hint_text = "Введите слова по памяти: ")
        bl0 = BoxLayout(orientation = "vertical")
        bl0.add_widget(ti)
        self.scroll.add_widget(bl0)
        root.add_widget(self.scroll)
        self.bl = BoxLayout(size_hint_y = 0.2)
        b = Button(text = "Проверить",on_press = lambda x:MainApp.mediator3.notify("c6"))
        self.bl.add_widget(b)
        root.add_widget(self.bl)
        self.add_widget(root)
class Task3Builder:
    instruction = None
    @staticmethod
    def update_instruction(parameters):
        pr = parameters
        if pr["quan"] > len(LIST3):
            pr["quan"] = len(LIST3)
        Task3Builder.instruction = pr
    def create_basescrean(self):
        screen = Basetaskscreen3()
        Mediator3._root.add_widget(screen)
        scr = Mediator3._root.get_screen("words3")
        Mediator1._root.transition.direction = "left"
        return scr
    def get_exm(self,scr):
        text = Task3Builder.generate_txt(Task3Builder.instruction)
        Mediator3.current_text = text
        ti = TextInput(text = text, readonly =True,size_hint_y = None)
        ti.height = ti.minimum_height
        if len(scr.scroll.children) != 1:
            scr.scroll.add_widget(ti)
        else:
            scr.scroll.children[0].text = text
        return None
    @staticmethod
    def generate_txt(instruction):
        txt = ""
        if instruction["numbers"] == "":
            pass
        else:
            counter =  0
            for i in range(instruction["quan"]):
                number = str(random.randint(1, int(instruction["numbers"])))
                LIST3.append(number)
                counter += 1
        lst = random.choices(LIST3, k = instruction["quan"])
        for i in lst:
            txt += i +", "
        txt = txt[0:-2]
        if instruction["numbers"] != "":
            del LIST3[len(LIST3)-counter:]
        return(txt)
class Mediator3(Mediator):
    main_parameters = {"quan": 10,  "istime": False,"time": 5,"numbers": ''}
    taskbuilder = Task3Builder()
    current_text = ""
    extra_widgets = {"textinput": TextInput(text="",size_hint_y = None),"button": Button(text = "<--")}
    clockevent = None
    @staticmethod
    def c1():
        MainApp.show_popup4()
        return None
    @staticmethod
    def c2(act,bl):
        Mediator3.main_parameters["istime"] = act
        l = Mytextinput(hint_text="Введите время: ", multiline=False,size_hint_y = 0.5)
        l.bind(text = Mediator3.c8)
        if str(l)[10:21] in [str(x)[10:21] for x in bl.children]: #должен быть только 1  mytextinput
            index = [str(x)[10:21] for x in bl.children].index(str(l)[10:21])
            bl.remove_widget(bl.children[index])
        else:
            bl.add_widget(l,2)
        return None
    @staticmethod
    def c3():
        MainApp.popups["popup4"].dismiss()
        Mediator3.taskbuilder.update_instruction(Mediator3.main_parameters)
        if not (r"<Screen name='words3'>") in [str(x) for x in Mediator3._root.screens]:
            scr = Mediator3.taskbuilder.create_basescrean()
        else:
            scr = Mediator3._root.get_screen("words3")
            Mediator3._root.transition.direction = "left"
        if Mediator3.main_parameters["istime"] == True:
            print(2)
            Mediator3.clockevent = Clock.schedule_once(lambda x:Mediator3.c7(),Mediator3.main_parameters["time"])
        Mediator3._root.current = "words3"
        Mediator3.taskbuilder.get_exm(scr)
        return None
    @staticmethod
    def c4():
        Mediator3.main_parameters["istime"] = False
        if Mediator3.clockevent != None:
            Clock.unschedule(Mediator3.clockevent)
        try:
            scr = Mediator3._root.get_screen("checkword3")
            scr.scroll.children[0].remove_widget(scr.scroll2)
            scr.scroll2.remove_widget(Mediator3.extra_widgets["textinput"])
        except:
            pass
        Mediator3._root.current = "main"
        Mediator3._root.transition.direction = "right"
        return None
    @staticmethod
    def c5():
        if "<Screen name='checkword3'>" not in [str(x) for x in Mediator3._root.screens]:
            scr = Notbasetaskscreen3()
            Mediator3._root.add_widget(scr)
        Mediator3._root.current = "checkword3"
        return None
    @staticmethod
    def c6():
        scr = Mediator3._root.get_screen("checkword3")
        if scr.bl.children[0].text == "Проверить":
            Mediator3.extra_widgets["textinput"].text = Mediator3.current_text
            Mediator3.extra_widgets["textinput"].height = Mediator3.extra_widgets["textinput"].minimum_height
            scr.scroll2.add_widget(Mediator3.extra_widgets["textinput"])
            scr.scroll.children[0].add_widget(scr.scroll2)
            scr.bl.children[0].text = "<--"
        else:
            Mediator3.extra_widgets["textinput"].text = ""
            scr.scroll.children[0].remove_widget(Mediator3.extra_widgets["textinput"])
            scr.bl.children[0].text = "Проверить"
            Mediator3.c4()
        return None
    @staticmethod
    def c7(*args):
        if str(Mediator3._root.current) != "words3":
            return None
        MainApp.show_popup5()
        Mediator3.c5()

    @staticmethod
    def c8(*args):
        text = int(args[1])
        if text >= 60000:
            text = 60000
        Mediator3.main_parameters["time"] = text
        return None
    @staticmethod
    def c9(*args):
        text = int(args[0].text)
        if text >= 1000:
            text = 1000
        Mediator3.main_parameters["quan"] = text
    activators = {"c1": c1, "c2": c2, "c3": c3, "c4": c4, "c5": c5, "c6": c6, "c7": c7, "c9": c9}
class Basescreen4(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        s = Builder.load_string(container7)
        self.add_widget(s)
        self.name ="task4"
class Mediator4(Mediator):
    main_parameters = {"mode": 0,"quan": 10,"mode1": "+3"}
    sound = SoundLoader.load('test.mp3')
    impotant_lst= []
    i = 0
    @staticmethod
    def d1():
        MainApp.show_popup6()
    @staticmethod
    def d2(b):
        if b.text == "Режим: +3":
            Mediator4.main_parameters["mode1"]="+1"
            b.text = "Режим: +1"
        else:
            Mediator4.main_parameters["mode1"] = "+3"
            b.text = "Режим: +3"
    @staticmethod
    def d3(text):
        text = int(text)
        if text >= 100:
            text = 100
        Mediator4.main_parameters["quan"] = text
    @staticmethod
    def d4():
        MainApp.popups["popup6"].dismiss()
        Mediator4.impotant_lst = generate2(Mediator4.main_parameters["quan"])
        if not (r"<Screen name='task4'>") in [str(x) for x in Mediator4._root.screens]:
            screen = Basescreen4()
            Mediator4._root.add_widget(screen)
            Mediator1._root.transition.direction = "left"
        else:
            s = Mediator4._root.get_screen("task4")
            Mediator4._root.remove_widget(s)
            screen = Basescreen4()
            Mediator4._root.add_widget(screen)
            Mediator3._root.transition.direction = "left"
        Mediator4._root.current = "task4"
        Mediator4.sound.play()
        return None
    @staticmethod
    def d5():
        if Mediator4._root.current == "task4":
            Mediator4.i = 0
            Mediator4.main_parameters["mode"] = 0
        Mediator4.sound.stop()
        Mediator4._root.current = "main"
        Mediator4._root.transition.direction = "right"
        return None
    @staticmethod
    def d6(b):
        if Mediator4.i == Mediator4.main_parameters["quan"] and Mediator4.main_parameters["mode"] == 0:
            Mediator4.i = 0
            Mediator4.impotant_lst = generate2(Mediator4.main_parameters["quan"])
            ans = list(str(Mediator4.impotant_lst[-1]))
            for k in range(len(ans)):
                ans[k] = str(int(ans[k]) + 1) if ans[k] != "9" else "0"
            toast_text = "".join(ans)
            toast(toast_text)
            MainApp.show_popup7()
            Mediator4.d5()
            return None
        if Mediator4.main_parameters["mode"] == 0:
            b.text = str(Mediator4.impotant_lst[Mediator4.i])
            Mediator4.main_parameters["mode"] = 1
            if Mediator4.main_parameters["mode1"] =="+1":
                ans = list(str(Mediator4.impotant_lst[Mediator4.i - 1]))
                for k in range(len(ans)):
                    ans[k] = str(int(ans[k]) + 1) if ans[k] != "9" else "0"
                if Mediator4.i != 0:
                    toast_text = "".join(ans)
                    toast(toast_text)
            else:
                ans = list(str(Mediator4.impotant_lst[Mediator4.i-1]))
                for k in range(len(ans)):
                    ans[k] = str(int(ans[k]) + 3) if int(ans[k]) < 7 else str(int(ans[k])+3)[-1]
                if Mediator4.i != 0:
                    toast_text = "".join(ans)
                    toast(toast_text)
            Mediator4.i += 1
        else:
            b.text ="..."
            Mediator4.main_parameters["mode"] = 0
    activators = {"d1": d1,"d2": d2,"d3": d3,"d4": d4,"d5": d5,"d6": d6}
    #Запоминание SCROLL не работает, один заработал
class MainApp(MDApp):
    popups={"popup1":None,"popup2":None,"popup3":None,"popup4":None,"popup6": None,"popup7": None}
    tablesize = None
    mediator = Mediator1()
    mediator2 = Mediator2()
    mediator3 = Mediator3()
    mediator4 = Mediator4()
    def on_start(self):
        Mediator._root =self.rootwidget
    def build(self):
        self.rootwidget = Builder.load_string(container)
        return self.rootwidget
    @staticmethod
    def show_popup1():
        container = Builder.load_string(container1)
        MainApp.popups["popup1"] = Popup(content = container, auto_dismiss=False,title = "",size_hint_y=0.37)
        MainApp.popups["popup1"].open()
        return None
    @staticmethod
    def show_popup2(*args):
        if MainApp.mediator.main_parameters["istime"] == "False":
            return None
        container = Builder.load_string(container2)
        MainApp.popups["popup2"] = Popup(content=container, auto_dismiss=False, title="", size_hint_y=0.37)
        MainApp.popups["popup2"].open()
        return None
    @staticmethod
    def show_popup3():
        container = Builder.load_string(container3)
        MainApp.popups["popup3"] = Popup(content=container, auto_dismiss=False, title="", size_hint_y=0.65)
        panel =MDExpansionPanel(
        content=Builder.load_string(container4),
        panel_cls=MDExpansionPanelOneLine(text="Выберете функции: ")  # panel class
    )
        MainApp.popups["popup3"].content.ids.box.add_widget(panel,1)
        i = 1
        lst = list(Mediator2.main_parameters.values())[3:]#
        for bool in lst:                                  #
            panel.content.ids[f"cb{i}"].active = bool     #checkkbox on_active работает некоректно, костыльный фикс
            i+=1
        MainApp.popups["popup3"].open()
        return None
    @staticmethod
    def show_popup4():
        container = Builder.load_string(container5)
        MainApp.popups["popup4"] = Popup(content=container, auto_dismiss=False, title="", size_hint_y=0.65)
        MainApp.popups["popup4"].open()
        return None
    @staticmethod
    def show_popup5():
        container = Builder.load_string(container2)
        MainApp.popups["popup2"] = Popup(content=container, auto_dismiss=False, title="", size_hint_y=0.37)
        MainApp.popups["popup2"].open()
    @staticmethod
    def show_popup6():
        container = Builder.load_string(container6)
        MainApp.popups["popup6"] = Popup(content=container, auto_dismiss=False, title="", size_hint_y=0.37)
        MainApp.popups["popup6"].open()
    @staticmethod
    def show_popup7():
        container = Label(text = "Упражнение завершено.")
        MainApp.popups["popup7"] = Popup(content=container, auto_dismiss=True, title="", size_hint_y=0.37)
        MainApp.popups["popup7"].open()
if __name__ == "__main__":
    MainApp().run()
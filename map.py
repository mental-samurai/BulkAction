from tkinter import Tk, Entry, Button  # подключаем элементы tkinter (PYQt5) UI DEsiGn
from tkinter import filedialog  # для выбора картинки
from PIL import Image, ImageTk, ImageFilter, ImageEnhance,   # для обработки изображений
from datetime import datetime
import os

def __init__(self):
    self.window = Tk()  # создали окно
    self.window.title('Обработка картинки')  # заголовок окна
    self.window.geometry('800x600')  # размер окна
    self.window.resizable(False, False)  # запрет на изменение размера окна
    self.window.iconphoto(False, PhotoImage(file='icon_dog.png'))
    self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
    self.name = 'СПб, Можайская, 2 '
    self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey=&geocode={self.apikey}&format=json'
    self.label = Label(text='Map Space', background='Magenta', foreground='blue',
                       font=('Georgia', 16))
    self.label.pack(fill=X, pady=5)
    self.load = Button(text='Найти', command='add')
    self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
    self.place = Entry(width=60, font=('Verdana', 16))
    self.place.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
    self.cwd=os.getcwd()
    self.image = None
    self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
    self.window.mainloop()
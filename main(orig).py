# подключаем элементы tkinter (PyQt5)
import os
from datetime import datetime
from tkinter import CENTER, LEFT, NW, N, X
from tkinter import Tk, PhotoImage, Label, Canvas, Button, Entry
from tkinter import filedialog  # для выбора картинки
from PIL import Image, ImageTk, ImageFilter, ImageEnhance  # для обработки изображений


class App():
    def __init__(self):
        self.window = Tk()  # создали окно
        self.window.title('Поиск по карте')
        self.window.geometry('800x600')
        self.window.resizable(False, False)
        self.window.iconphoto(False, PhotoImage(file='pencil.png'))
        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.name = 'СПб, Можайская, 2'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={self.apikey}&geocode={self.name}&kind=metro&format=json'
        self.label = Label(text='Поиск по карте',
                           background='#ffff00', foreground='red',
                           font=('Verdana', 16))
        self.label.pack(fill=X, pady=5)
        self.canvas = Canvas(bg='white', width=600, height=450)
        self.canvas.pack(anchor=CENTER, pady=20)
        self.load = Button(text='Найти', command=self.open)
        self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.place = Entry(width=60, font=('Verdana', 16))
        self.place.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.cwd = os.getcwd()
        self.image = None  # заглушка
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        self.window.mainloop()  # ожидание

    def open(self):
        try:
            fullpath = filedialog.askopenfilename(title='Выбор картинки',
                                                  initialdir=self.cwd,
                                                  filetypes=(
                                                      ('GIF', '*.gif'),
                                                      ('PNG', '*.png'),
                                                      ('JPG', '*.jpg')
                                                  )
                                                  )
            self.orig = Image.open(fullpath)
            self.w, self.h = self.orig.size
            mode = self.orig.mode
            if mode == 'P':  # Если 256 color indexed image
                self.orig = self.orig.convert('RGB')
            if self.w > 600:
                ratio = self.w / 600
                self.orig = self.orig.resize((600, int(self.h / ratio)))
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        except AttributeError:
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def blur(self):
        blur_image = self.orig.filter(ImageFilter.BLUR)
        self.image = ImageTk.PhotoImage(blur_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.orig)
        sharp_img = sharper.enhance(5.0)
        self.image = ImageTk.PhotoImage(sharp_img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)



if __name__ == '__main(orig)__':
    app = App()

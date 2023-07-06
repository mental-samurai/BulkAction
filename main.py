from tkinter import *  # подключаем элементы tkinter (PYQt5) UI DEsiGn
from tkinter import filedialog  # для выбора картинки
from PIL import Image, ImageTk, ImageFilter, ImageEnhance  # для обработки изображений
from datetime import datetime
import os


class App():

    def __init__(self):
        self.window = Tk()  # создали окно
        self.window.title('Обработка картинки')  # заголовок окна
        self.window.geometry('800x600')  # размер окна
        self.window.resizable(False, False)  # запрет на изменение размера окна
        self.window.iconphoto(False, PhotoImage(file='icon_dog.png'))
        self.label = Label(text='Обработка изображений',
                           background='Magenta', foreground='blue',
                           font=('Georgia', 16))
        self.label.pack()
        self.canvas = Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=5)
        self.load = Button(text='Открыть в', command='add')
        self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.blur = Button(text='Размыть')
        self.sharp = Button(text='Резкость')
        self.sharp.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        cwd = os.getcwd()
        self.cwd = os.getcwd()
        self.image = None
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        self.window.mainloop()  # ожидание цикл

        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey=&geocode=Город&format=json'
    def add(self):
        try:
            fullpath = filedialog.askopenfilename(title='Выбор картинки',
                                                  initialdir=self.cwd,
                                                  filetypes=(
                                                      ('GIF', '*gif'),
                                                      ('PNG', '*png'),
                                                      ('JPG', "*jpg")
                                                  )
                                                  )

            self.orig = Image.open(fullpath)
            self.w, self.h = self.orig.size
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
self.sharp.pack(anchor=N)
        self.dtime = Label(background='#ffffff')
        self.dtime.place(x=310, y=530)
        self.cwd=os.getcwd()
        self.image = None
        self.image = Image.new('RGB', (600, 400), (255, 255, 255))
        self.show_time()
        self.window.mainloop()

    def show_time(self):
        self.time_to_show = datetime.time(datetime.now()).strftime("%H:%M:%S")
        self.dtime['text'] = self.time_to_show
        self.dtime.after(1000, self.show_time)


if __name__ == '__main__':
    app = App()

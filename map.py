import os
from tkinter import Tk, Entry, Button, Label, Canvas, CENTER, X, LEFT, N, PhotoImage, \
    NW  # подключаем элементы tkinter (PYQt5) UI DEsiGn
from tkinter import filedialog  # для выбора картинки
from io import BytesIO
import requests
from PIL import Image, ImageTk, ImageFilter, ImageEnhance


class App:
    def __init__(self):
        self.window = Tk()  # создали окно
        self.window.title('поиск по картинке')  # заголовок окна
        self.window.geometry('800x600')  # размер окна
        self.window.resizable(False, False)  # запрет на изменение размера окна
        self.window.iconphoto(False, PhotoImage(file='icon_dog.png'))
        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.name = 'СПб, Можайская, 2 '
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey=&geocode={self.apikey}&kind=metro&format' \
                                f'=json'
        self.label = Label(text='Поиск по картинке', background='#ffff00', foreground='red',
                           font=('Georgia', 16))
        self.label.pack(fill=X, pady=5)
        self.canvas = Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=5)
        self.load = Button(text='Найти', command='add')
        self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.place = Entry(width=60, font=('Verdana', 16))
        self.place.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.cwd = os.getcwd()
        self.image = None
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        self.window.mainloop()

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

    # def blur(self):
    #         blur_image = self.orig.filter(ImageFilter.BLUR)
    #         self.image = ImageTk.PhotoImage(blur_image)
    #         self.canvas.create_image(0, 0, anchor=NW, image=self.image)
    #
    # def sharp(self):
    #         sharper = ImageEnhance.Sharpness(self.orig)
    #         sharp_img = sharper.enhance(5.0)
    #         self.image = ImageTk.PhotoImage(sharp_img)
    #         self.canvas.create_image(0, 0, anchor=NW, image=self.image)

if __name__ == '__map__':
        app = App()


    def open(self):
        response = requests.get(self.geocoder_request)
        info = response.json()
        coords = (info['response']['GeoObject']['featureMember']['GeoObject']['Point']['pos'])
        coords = ', '.join(coords.split())
        delta = '0.0005,0.0005'
        map_param = {
            'll': 'coords',
            'spn': 'delta',
            'l': 'map'
        }
        api_server = 'http://static-maps.yandex.ru/1.x/'
        image_map = requests.get(api_server, params=map_param)
        pict_to_show = Image.open(BytesIO(image_map.content))
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)



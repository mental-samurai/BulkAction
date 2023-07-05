from tkinter import *  # подключаем элементы tkinter
from tkinter import filedialog  # для выбора картинки
from PIL import Image, ImageTk, ImageFilter  # для обработки изображений
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
        self.canvas.create_image(0, 0, anchor=NW, image=blur.image)


if __name__ == '__main__':
    app = App()

import tkinter as tk
# tk = __import__("tkinter")

class Window(tk.Tk):
    def __init__(self, title="gui", x=0, y=0, width=480, height=320):
        super().__init__()
        self.title = title
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.__x, self.__y, self.__width, self.__height = x, y, width, height
        self.screensize = (self.winfo_screenwidth(), self.winfo_screenheight())
        self.bind("<Configure>", self.__onConfig)

    def init(self):
        self.mainloop()

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, value):
        self.__title = value
        super().title(self.__title)

    @property
    def x(self): return self.__x
    @x.setter
    def x(self, value):
       self.__x = value
       self.geometry(f"+{self.__x}+{self.__y}")

    @property
    def y(self): return self.__y
    @y.setter
    def y(self, value):
       self.__y = value
       self.geometry(f"+{self.__x}+{self.__y}")

    @property
    def width(self): return self.__width
    @width.setter
    def width(self, value):
       self.__width = value
       self.geometry(f"{self.__width}x{self.__height}")

    @property
    def height(self): return self.__height
    @height.setter
    def height(self, value):
       self.__height = value
       self.geometry(f"{self.__width}x{self.__height}")

    def center(self):
        self.x, self.y = self.screensize[0]//2-self.width//2, self.screensize[1]//2-self.height//2
        self.geometry(f"+{self.__x}+{self.__y}")

    def __onConfig(self, event):
        self.__x = event.x
        self.__y = event.y
        self.__width = event.width
        self.__height = event.height

    def __getattribute__(self, __name):
        try:
            return super().__getattribute__(__name)
        except AttributeError as e:
            print(f"AttributeError: '{self.__class__}' has no attribute '{__name}'")


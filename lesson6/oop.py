class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Ошибка: Значение должно быть больше 0!")
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            print("Ошибка: Значение должно быть больше 0!")
    def __str__(self) -> str:
        # Срабатывает при: print(v)
        return f"Прямоугольник {self.width}x{self.height}"
    def __add__(self, other: 'Rectangle' ):
        # Срабатывает при: v1 + v2
        return self.width*self.height + other.height*other.width

rect1 = Rectangle(5, 4)
rect2 = Rectangle(10, 2)
print(rect1)
print(rect1 + rect2)
rect1.width = -5
from  accessify import private, protected

class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y


    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    def get_coord(self):
        return self.__x, self.__y

pt = Point(1, 2)
pt.set_coord(10, 20.1)
pt.check_value(5)
print(pt.get_coord())
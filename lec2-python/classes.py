class Point:
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

    def __str__(self) -> str:
        return str(self.__dict__)


p = Point(2, 3)
print(p)

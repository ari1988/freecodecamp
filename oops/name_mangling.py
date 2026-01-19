class Example:
    def __init__(self):
        self._internal = "I can be accessed"
        self.__private = "I can't"
    
    def expose(self):
        return self.__private

c1 = Example()
print(c1._internal)
print(c1.expose())
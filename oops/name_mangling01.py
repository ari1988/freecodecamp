class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}

"""
You can see that both the Parent class and the Child that inherits from it have their 
separate _class__data attributes. This is made possible with name mangling. 
Otherwise, the Child would have overwritten the Parent data by accident.
"""
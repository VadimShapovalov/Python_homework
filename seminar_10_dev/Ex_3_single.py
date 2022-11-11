
class AlwaysSame(type):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.Only = None

    def __call__(self, *args, **kwargs):
        if self.Only is None:
            self.Only = super(AlwaysSame, self).__call__(*args, **kwargs)
            return self.Only
        else:
            return self.Only

class Single(metaclass=AlwaysSame):
    pass
obj_1 = Single()
obj_2 = Single()
obj_3 = Single()

print(obj_1 is obj_3) 
print(obj_2 is obj_3) 

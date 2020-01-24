class Test:
    def __init__(self, value):
        self.value = value
        print('Initialized')

    def create_new_object(self, value):
        return Test(value)
    
    def print_value(self):
        print(self.value)

item1 = Test(10)
item2 = item1.create_new_object(200)
print(item1 == item2)
print(item1.value, item2.value)

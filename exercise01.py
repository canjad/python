class CommodityIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration()
        self.index += 1
        return self.data[self.index]

class CommodityController:
    def __init__(self):
        self.list_commodity = []

    def add_commodity(self, cmd):
        self.list_commodity.append(cmd)

    def __iter__(self):
        return CommodityIterator(self.list_commodity)

controller = CommodityController()
controller.add_commodity('apple')
controller.add_commodity('banana')
iterator = controller.__iter__()

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
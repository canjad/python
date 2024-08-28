from dtl import EpidemicModel


class EpidemicDao:

    def __init__(self):
        self.list_target = self.load()

    def save(self):
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write(self.list_target.__repr__())

    def load(self):
        try:
            with open("data.txt", "r", encoding="utf-8") as file:
                return eval(file.read())
        except FileNotFoundError:
            return []

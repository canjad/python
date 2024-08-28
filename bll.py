from dal import *
from dtl import EpidemicModel


class EpidemicController:
    def __init__(self):
        # self.list_table = []  # type:list[EpidemicModel]
        self.__dao = EpidemicDao()
        self.list_table = self.__dao.list_target

    def add_epidemic(self, new):
        """添加疫情信息"""
        self.list_table.append(new)
        self.__dao.save()

    def delete_epidemic(self, name):
        try:
            self.list_table.remove(name)
            self.__dao.save()
            return True
        except:
            return False

    def modify_epidemic(self, model: EpidemicModel):
        for item in self.list_table:
            if item.name == model.name:
                item.__dict__ = model.__dict__
                self.__dao.save()
                return True
        return False

from bll import EpidemicController
from dtl import EpidemicModel


class EpidemicView:
    def __init__(self):
        self.__controller = EpidemicController()

    def __display_menu(self):
        """显示菜单"""
        print("输入1键录入疫情信息")
        print("输入2键显示疫情信息")
        print("输入3键删除疫情信息")
        print("输入4键修改疫情信息")
        print("输入5键退出程序")

    def __select_menu(self):
        number = input("请输入选项:")
        if number == "1":
            self.__input_epidemic()
        elif number == "2":
            self.__display_epidemic()
        elif number == "3":
            self.__remove_epidemic()
        elif number == "4":
            self.__update_epidemic()
        elif number == "5":
            exit()

    def __get_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                pass

    def __input_epidemic(self):
        """输入疫情信息"""
        model = EpidemicModel(
            name=input("请输入疫情名称:"),
            # now=int(input("请输入现有人数:")),
            new=self.__get_number("请输入新增人数:"),
            now=self.__get_number("请输入现有人数:")
        )
        self.__controller.add_epidemic(model)

    def __display_epidemic(self):
        for item in self.__controller.list_table:
            # print("%s地区新增人数:%d,现有人数:%d" % (item.name, item.new, item.now))
            print(item)  # print(item.__str__())

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __remove_epidemic(self):
        while True:
            name = input("请输入需要删除的地区名:")
            if self.__controller.delete_epidemic(name):
                print("亲~橙啦，该地区疫情信息已删除")
                break
            else:
                print("亲~no，该地区疫情信息不存在")

    def __update_epidemic(self):
        while True:
            model = EpidemicModel(
                name=input("请输入需要修改的疫情名称:"),
                new=self.__get_number("请输入新增人数:"),
                now=self.__get_number("请输入现有人数:")
            )
            if self.__controller.modify_epidemic(model):
                print("亲~orange，疫情信息已修改")
                break
            else:
                print("亲~no，该地区疫情信息不存在")

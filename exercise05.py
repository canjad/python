class StudentCotroller:
    def __init__(self):
        self.list_student=[]
    def __iter__(self):
        index=-1
        index+=1
        '''
        1.将yield 以前的代码定义在 next_函数当中
        2.将yield 以后的代码定义在 next_函数返回值
        3.最后发送 stopInteration
        '''
        yield self.list_student[index]
        yield self.list_student[index]
        yield self.list_student[index]
controller = StudentCotroller()
controller.list_student.append("八戒")
iterator = controller.__iter__()

while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break





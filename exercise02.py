class MyrangeIterator:
    def __init__(self,end):
        self.number=-1 #存储当前数据，，释放之前数据
        self.end=end
#循环一次 计算一次 返回一次
#没有教数据存储到内存中
    def __next__(self):
        if self.number ==self.end-1:
            raise StopIteration()
        self.number+=1
        return self.number


class Myrange:
    def __init__(self,stop):
        self.stop=stop
    def __iter__(self):
        return MyrangeIterator(self.stop)

obj = Myrange(5)
iterator=obj.__iter__()

while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break

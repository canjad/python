def My_range(stop):
    numbers = 0
    while numbers < stop:
        yield numbers
        numbers += 1

# Creating an object of My_range and iterating through it
obj = My_range(5)
iterator = obj.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
list01=[34,54,54,56,7]
iterator=list01.__iter__()

while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break


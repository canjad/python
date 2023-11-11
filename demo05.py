list01=[43,54,56,65,76,7,8]
#定义容器，存储所有结果
# def get_number_gt_50():
#     list_result=[]
#     for item in list01:
#         if item>50:
#             list_result.append(item)
#     return list_result
# data =get_number_gt_50()
# for item in data:
#     print(item)

#生成器代码
# def get_number_gt_50():
#     for item in list01:
#         if item>50:
#             yield item
# data =get_number_gt_50()
# for item in data:
#     print(item)


list01 = [43, 43, 54, 56, 76, 87, 98]

def find_all_even(list_target):
    for item in list_target:
        if item%2==0:
            yield item
    print(item)
for item in find_all_even(list01):
    print(item)
list02=[43,"悟空"]
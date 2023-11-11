'''
内置生成器 zip
'''

list_name=['jaden','canai','wang']

list_room=[101,102,103]

dict_res={}
# for i in range(len(list_name)):
#     key =list_name[i]
#     value=list_room[i]
#     dict_res[key]=value
# print(dict_res)
print(dict(zip(list_name,list_room)))
print(dict([('jaden',10001),('canai',1003)]))


map=[
    [2,0,0,2],
    [2,2,0,4],
    [2,0,2,2],
    [2,0,2,0],
    [2,2,3,4],

]
# new=[]
# for item in zip(map[0],map[1],map[2],map[3]):
#     print(list(item))
# print(new)
new=[]
for item in zip(*map): #序列实参
    print(list(item))
print(new)


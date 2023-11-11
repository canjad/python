'''
内置函数

'''

list01=[4,5,6,7,8,8]
for item in list01:
    print(item)
#

for i in range(len(list01)):
    if list01[i]>10:
        list01[i]=10
#第三种

# for item in enumerate(list01):
#     print(item)

for i,item in enumerate(list01):
    if item>10:
        list01[i]=10
#     for 循环快借钱
# for item in list01:
# for i,  in enumerate(list01):
for i,  item in enumerate(list01):
  if item % 2!=0:
    list01[i]=None
print(list01)
for i, item in enumerate(list01):
    if item % 2 ==0:
        list01[i]+=1
print(list01)




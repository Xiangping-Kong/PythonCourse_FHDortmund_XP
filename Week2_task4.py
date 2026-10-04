# Original list of strings
str_list = ['Red', 'Green', 'Black']
print("Original list of strings:")
print(str_list)

# map(函数, 可迭代对象)，list()把map对象转成列表
#result = list(map(list, str_list))
#use lambda：
result = list(map(lambda s: list(s), str_list))

print("\nConvert the said list of strings into list of lists:")
print(result)

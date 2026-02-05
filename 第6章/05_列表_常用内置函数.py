# 1.使用内置的sorted函数，返回一个排序后的新容器（不改变元容器，默认顺序：从小到大）
# 1.1若列容器中的元素：都是数字，则按照数字的大小顺序进行排序
nums = [23, 11, 32, 30, 17]
result = sorted(nums, reverse=True)
print(nums)
print(result)

# 1.2若列容器中的元素：既有数字，又有字符串，那就会报错
# nums = [23, 11, 32, 30, 17,'尚硅谷']
# sorted(nums)

# 1.3若列容器中的元素：都是字符串，则按照字符串的Unicode编码大小进行排序
msg_list = ['北京', '尚硅谷', '你好']
result = sorted(msg_list)
print(msg_list)
print(result)

# 2.使用内置的len函数，获取容器中元素的总数量，返回值是：元素总数量
nums = [10, 20, 10, 30, 10, 40, [50, 60, 70]]
result = len(nums)
print(result)

# 3.使用内置的max函数，获取容器中的最大值，返回值是：最大值
# 3.1如果容器中的元素：都是数字，那max返回的是最大的数
nums = [23, 11, 32, 30, 17]
result = max(nums)
print(nums)
print(result)

# 3.2如果容器中的元素：既有数字又有字符串，那max会报错
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# max(nums)

# 3.3如果容器中的元素：都是字符串，那max会返回：Unicode编码最大的字符
msg_list = ['北京', '尚硅谷', '你好']
result = max(msg_list)
print(result)

# 3.4max函数也可以接收多个值，并筛选出最大值
result = max(33, 45, 12, 78, 99)
print(result)

# 4.使用内置的min函数，获取容器中的最小值，返回值是：最小值
# 备注：min函数的使用方式于注意点与max函数一样，只不过min函数返回的是最小值
nums = [23, 11, 32, 30, 17]
result = min(nums)
print(result)

# 5.使用内置的sum函数，对容器中的数据进行求和（元素只能是数值）
nums = [10, 20, 30, 40, 50]
result = sum(nums)
print(result)

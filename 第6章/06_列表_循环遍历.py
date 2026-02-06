# 定义个成绩列表
score_list = [62, 50, 60, 48, 80, 20, 95]

# 使用while循环遍历列表
index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1

# 使用for循环遍历列表
# 写法一
for item in score_list:
    print(item)

# 写法二（通过range函数和len函数按照索引遍历）
for index in range(len(score_list)):
    print(score_list[index])

# 写法三（通过enumerate函数，同时获取下标（索引值）和元素）
# 备注：遍历的时候，start修改的只是循环时的编号，而不是列表中元素的真实索引
for index, item in enumerate(score_list, start=5):
    print(index, item,score_list[0])
print('最后打印',score_list[0])

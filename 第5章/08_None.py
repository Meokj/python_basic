# None是一个特殊的字面量，它表示：空值 / 无值 / 无意义
msg = None

# None的类型是NoneType
print(type(msg))

# None转为布尔值是False
print(bool(msg))
if not msg:
    print('你好')


# None不能参与数学运算，也不能与字符串拼接
# result1 = msg + 1
# result2 = msg + 'hello'

# None不给函数设置返回值，函数会默认返回None
def add(n1, n2):
    print(f'我收到了：{n1},{n2},二者相加是：{n1 + n2}')
    print('add函数执行完毕了')


print(add(100, 200))

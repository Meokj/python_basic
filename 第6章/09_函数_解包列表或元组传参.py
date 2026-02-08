def test1(data):
    print(f'我是test1函数，我收到的参数时：{data}')


list1 = [100, 200, 300, 400]
tuple1 = ('你好', '北京', '尚硅谷')

# 函数调用时，正常传递：列表 或 元组
test1(list1)
test1(tuple1)

# 定义函数时，使用*args（变量不一定非要用args，比如写：*data也可以）
def test2(*args):
    print(f'我是test2函数，我收到的参数时：{args}，参数类型是：{type(args)}')

# 函数调用时，使用*对：列表 或 元组进行解包后，再传递参数，将收到的多个参数，打包成一个元组
test2(*list1)  # 此种写法相当于：test(100,200,300,400)
test2(*tuple1)  # 此种写法相当于：test('你好', '北京', '尚硅谷')

# and用于判断其两侧的值，是否都为True，如果是则结果为True
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# and具备“逻辑短路”能力
print(False and 3 / 0)

# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则：and会先看左边，如果左边是“假”，就直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
print(2 - 2 and True)  # 0
print('' and True)  # ''
print(True and 8 / 2)  # 4.0
print(3 + 3 and 3 * 4)  # 12

# or用于判断其两侧，是否至少有一个为True(只要有一个是True，那就返回True)
print(True or True)
print(True or False)
print(False or False)
print(False or True)

# or同样具备“逻辑短路”的能力
print(True or 3 / 0)

# or返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则：or会先看左边，如果左边是“真”，就直接返回左边，否则返回右边
# 备注：若参与or运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
print(7 - 2 or False)  # 5
print('你好' or '再见')  # 你好
print(False or 8 / 2)  # 4.0
print(2 - 2 or 3 * 4)  # 12

# not用于取反
# 备注：若参与not运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
print(not True)  # False
print(not False)  # True
print(not 3 > 2)  # False
print(not 3 < 2)  # True

# not返回的值，一定是布尔值
print(not 0)
print(not 3 > 2)

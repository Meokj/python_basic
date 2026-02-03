text = input('请输入要加密的文字：')
secret = ''
for t in text:
    secret += chr(ord(t) + 1)
print(f'经过加密后的内容为：{secret}')

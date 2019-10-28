from io import BytesIO

byte_io = BytesIO()
# 向内存中写入数据
byte_io.write('哈哈'.encode('utf-8'))
# 读取数据，获取写入到内存中的全部数据
result = byte_io.getvalue()
print(result.decode())

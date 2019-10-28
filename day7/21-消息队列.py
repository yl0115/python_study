import multiprocessing

# 创建消息队列
queue = multiprocessing.Queue(3)

# 往队列添加数据
queue.put(1)
queue.put(2)
queue.put(3)

# 从队列中获取数据
result = queue.get()
print(result)
result = queue.get()
print(result)
result = queue.get()
print(result)
result = queue.get()
print(result)



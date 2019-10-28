# try:
#     print('try...')
#     r = 10 // 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

try:
    print('try...')
    r = 10//int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
else:
    print('no Error')
finally:
    print('finally...')
print('END')



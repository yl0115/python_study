class Hello(object):
    def hello(self, name='word'):
        print('hello .%s' % name)


h = Hello()
h.hello()
print(type(Hello))
print(type(h))
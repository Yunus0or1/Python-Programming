class A():
    def m(self):
        print('A')


class B(A):
    def m(self):
        print('B')


class C(A):
    def m(self):
        print('C')


class D(B,C):
    def m(self):
        print('D')


myDict= {
    1: 'hello',
    2: 'mello'
}

str ='abcdef'

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

def test ():
    return lambda a: a


x = test()
print(x(3))
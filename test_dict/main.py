
from collections import  defaultdict





def  testDefaultDict():
    my_dict = {}
    # 使用int作为defaultdict的default_factory
    # 将key不存在时，将会返回int()函数的返回值
    my_defaultdict = defaultdict(lambda :111)
    print(my_defaultdict['a'])  # 0
    #print(my_dict['a'])  # KeyError


def test2():
    d = {'a': 1, 'b': [], 'c': []}
    a = 111
    default_d = defaultdict(a.__int__, d)
    print(default_d)
    print(default_d['a'])
    print(default_d['absd'])


#dict keys 这个东西可以直接用&做交集，和集合差不多
def test_key_intersect():
    d1 = {'a':1,'b':2}
    d2 = {'b':2, 'c':3}
    print(d1.keys()&d2.keys())

if __name__ == "__main__":
    test_key_intersect()
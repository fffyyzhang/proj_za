from collections import defaultdict






def  testDefaultDict():
    my_dict = {}
    # 使用int作为defaultdict的default_factory
    # 将key不存在时，将会返回int()函数的返回值
    my_defaultdict = defaultdict(lambda :111)
    print(my_defaultdict['a'])  # 0
    #print(my_dict['a'])  # KeyError





if __name__ == "__main__":
    testDefaultDict()
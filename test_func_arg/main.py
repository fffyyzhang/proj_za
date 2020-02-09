









def func1(**kwargs):
    n = kwargs['name']
    print(n)



def test():
    arg = {'name':"zhangsan"}
    func1(arg)



if __name__ == "__main__":
    test()

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")



#
@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")




def test1():
    a_function_requiring_decoration()


if __name__ == "__main__":
    test1()
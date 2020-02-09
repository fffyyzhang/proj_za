
import time


def test_strptime():
    str = '2018/11/28'
    r = time.strptime(str, '%Y/%m/%d')
    d=1


if __name__ == "__main__":
    test_strptime()
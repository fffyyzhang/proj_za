import codecs





def main():
    with open('./prec.txt') as f_in:
        lines_prec = f_in.readlines()

    with open('./rec.txt') as f_in:
        lines_rec = f_in.readlines()

    d1 = {}
    d2 = {}

    for l in lines_prec:
        key, val = l.strip('\n').split(' ')
        d1[key] = float(val)

    for l in lines_rec:
        key, val = l.strip('\n').split(' ')
        d2[key] = float(val)

    assert d1.keys()==d2.keys()

    print('%14s:    %5s %5s'%('key', 'precision', 'recall'))
    for k in d1.keys():
        #print('{%.2s}:'.format(k))

        print('%14s:    %10f %10f'  %(k, d1[k], d2[k]))

    d = 1














if __name__ == "__main__":
    main()
import codecs

fname_raw = r"G:\data\DBpedia\baike_triples.txt"
fname_sample = r"G:\data\DBpedia\sample.txt"
len_sample = 100000



if __name__ == "__main__":
    buf = []

    with open(fname_raw, 'r', encoding='utf8') as fin:
        for i in range(len_sample):
            buf.append(fin.readline())
            if(i%100 == 0):
                print(i)
    fin.close()

    with open(fname_sample, 'w', encoding='utf8') as fout:
        fout.writelines(buf)
    fout.close()
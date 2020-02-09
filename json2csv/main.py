import json







# def main():
#     with open('files_raw/1.json',encoding='utf8') as f_in:
#         dtmp = json.load(f_in)
#         ltmp = dtmp['result']['resultData']
#         l_texts = [i['text'] for i in ltmp]
#         #print(l_texts)
#         for t in l_texts:
#             print(t.replace('（', '(').replace('）', ')'))
#
#         d=1



def main():
    #with open('files_raw/工行大额赔偿错例10-10.xlsx', encoding='utf8') as f_in:
    fname = 'files_raw/工行大额赔偿错例10-10.xlsx'
    fout = 'files_raw/工行大额赔偿错例10_10_去重.xlsx'
    import  pandas as pd
    df = pd.read_excel(fname)
    ds = df['案号'].unique()
    df2 = pd.DataFrame(ds)
    df2.to_excel(fout)
    d=1


if __name__ == "__main__":
    main()
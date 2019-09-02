import pandas as pd





def doMain():
    fname = r"G:\data\last_fm\usersha1-artmbid-artname-plays.tsv"
    df = pd.read_csv(fname, sep='\t', engine='c' ,usecols=[0,2,3], names=['user', 'atrist', 'plays'])

    d=1
    df_sample = df.sample(50)
    df_sample.to_csv(r'G:\data\last_fm\sample.csv', header=True ,index=False)



def doMain2():
    df = pd.read_csv(r'G:\data\last_fm\sample.csv')
    # pandas的astype可以直接实现编号功能
    df['user'] =  df['user'].astype('category')
    d=1












if __name__ == "__main__":
    doMain2()
import urllib.request


def main():
    urllib.request.urlretrieve('http://files.grouplens.org/datasets/movielens/ml-100k.zip', './download_data/ml100k.zip')




if __name__ == "__main__":
    main()
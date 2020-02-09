import time
from tqdm import tqdm
from tqdm._tqdm import trange


if __name__ == "__main__":
    with tqdm(total=100) as pbar:
        for i in range(10):
            pbar.update(10)
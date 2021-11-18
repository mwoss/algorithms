"""
Having a dataset with random objects inside return a chunk of that dataset.
Chunk should be of size "f * len(dataset)". Each element should have equal probability to be included into this chunk.

Example:
    dataset = [1, 2, 3]; f=2/3
    chunk = [1, 2] or [2, 3] or [1, 3]

Constraints:
* f is between (0, 1)
* dataset contains random objects, size is unknown but can be fit into memory
"""
import random
from typing import List


def split_dataset(dataset: List[object], f: float) -> List[object]:
    # optimal if f <= 0.5
    # see: https://stackoverflow.com/questions/6947612/generating-m-distinct-random-numbers-in-the-range-0-n-1
    split_chunk_size = int(len(dataset) * f)
    chunk, visited_idx = [], set([])

    while split_chunk_size != 0:
        idx = random.randint(0, len(dataset) - 1)
        if idx not in visited_idx:
            chunk.append(dataset[idx])
            visited_idx.add(idx)
            split_chunk_size -= 1

    return chunk


def split_dataset_2(dataset: List[object], f: float) -> List[object]:
    # optimal if f > 0.5
    split_chunk_size = int(len(dataset) * f)
    random.shuffle(dataset)
    return dataset[:split_chunk_size]


def split_dataset_reservoir_sampling(dataset: List[object], f: float) -> List[object]:
    # If dataset is just a stream of data and we don't know how much elements the stream contains
    # we can use reservoir sampling algorithm to chose k equally probable (distinct) elements from the stream
    # see: https://en.wikipedia.org/wiki/Reservoir_sampling
    pass


if __name__ == '__main__':
    dataset = list(range(1000))
    chunk = split_dataset_2(dataset, 0.9)
    print(chunk)
    print(len(set(chunk)))

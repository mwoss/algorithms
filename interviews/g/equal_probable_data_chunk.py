"""
README: TODO
"""
import random
from typing import List


def split_dataset(dataset: List[object], f: float) -> List[object]:
    split_chunk_size = int(len(dataset) * f)
    chunk, visited_idx = [], set([])

    while split_chunk_size != 0:
        idx = random.randint(0, len(dataset) - 1)
        if idx not in visited_idx:
            chunk.append(dataset[idx])
            visited_idx.add(idx)
            split_chunk_size -= 1

    return chunk


if __name__ == '__main__':
    dataset = list(range(1000))
    chunk = split_dataset(dataset, 0.9)
    print(chunk)
    print(len(set(chunk)))

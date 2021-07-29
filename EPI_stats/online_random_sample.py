# 5.13 sample online data

import random
import itertools

def online_random_sample(it, k):
    sampling_results = list(itertools.islice(it, k))

    num_seen_so_far = k
    for x in it:
        num_seen_so_far += 1
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    return sampling_results


it = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 5

print(online_random_sample(it, k))

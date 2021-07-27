# uniform random number
"""
https://github.com/adnanaziz/EPIJudge/tree/master/epi_judge_python
"""

import random

def zero_one_random():
    return random.randrange(2)

def uniform_random(lower_bound, upper_bound):
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | zero_one_random()
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


# test the function
for i in range(100):
    print(i+1, ' ', uniform_random(1, 10))

    

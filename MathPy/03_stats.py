"""
calculating the mean
"""
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # caculate the mean
    mean = s / N
    return mean

# calculating the median
def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    # find the median
    if N % 2 == 0:
        m1 = N / 2
        m2 = N / 2 + 1

        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N + 1) / 2
        m = int(m) - 1
        median = numbers[m]

    return median

# caculate the mode
from collections import Counter
def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

    # mode = c.most_common(1)
    # return mode[0][0]

if __name__ == '__main__':
    donations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    mean = calculate_mean(donations)
    N = len(donations)
    print('mean donation over the last {0} days is {1}'.format(N, mean))

    median = calculate_median(donations)
    print('Median donation for the last {0} days is {1}'.format(N, median))

    # scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    scores = [5,5,5,4,4,4,9,1,3]
    modes = calculate_mode(scores)
    print('The mode(s) of the list of scores are:')
    for mode in modes:
        print(mode)

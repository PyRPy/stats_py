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


if __name__ == '__main__':
    donations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    mean = calculate_mean(donations)
    N = len(donations)
    print('mean donation over the last {0} days is {1}'.format(N, mean))

    median = calculate_median(donations)
    print('Median donation for the last {0} days is {1}'.format(N, median))

# find the range
def find_range(numbers):

    lowest = min(numbers)
    highest = max(numbers)
    # find range
    r = highest - lowest

    return lowest, highest, r

# find the variance and standard deviation of a list of numbers

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N

    return mean

def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []
    for num in numbers:
        diff.append(num - mean)

    return diff

def calculate_variance(numbers):

    # find the list of differences
    diff = find_differences(numbers)
    # find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance


if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print('lowest: {0} highest: {1} range {2}'.format(lowest, highest, r))

    variance = calculate_variance(donations)
    print('the variation of the list of numbers is {0}'.format(variance))

    std = variance**0.5
    print('the standard deviation of the list of numbers is {0}'.format(std))
    

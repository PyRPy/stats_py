# reading data from a text file
# find the sum of the numbers stored in a file
# version 2 for stats calculations
def read_data(file_name):

    numbers = []
    with open(file_name) as f:
        for line in f:
            numbers.append(float(line))

    return numbers

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N

    return mean

if __name__ == '__main__':
    data = read_data('mydata.txt')
    mean = calculate_mean(data)
    print('print data: {0}'.format(data))
    print('mean : {0}'.format(mean))

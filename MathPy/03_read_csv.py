# read csv files
import csv
import matplotlib.pyplot as plt

def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel("Number")
    plt.ylabel("Square")
    plt.show()

def find_corr_x_y(x, y):
    n = len(x)

    # find the sum of the products
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi*yi)

    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2

    x_square = []
    for xi in x:
        x_square.append(xi**2)

    # find sum for x sqr
    x_square_sum = sum(x_square)
    y_square = []
    for yi in y:
        y_square.append(yi**2)
    # find sum for y sqr
    y_square_sum = sum(y_square)

    # use formula to calculate correlation
    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator / denominator

    return correlation

def read_csv(filename):
    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(int(row[0]))
            squared.append(int(row[1]))
        return numbers, squared

def read_csv2(filename):

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        summer = []
        highest_correlated = []
        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))

    return summer, highest_correlated

if __name__ == '__main__':
    numbers, squared = read_csv('numbers.csv')
    scatter_plot(numbers, squared)

    # read data from different columns
    summer, highest_correlated = read_csv2('correlate-summer.csv')
    print('summer: ', summer)
    print('highest_correlated: ', highest_correlated)
    corr = find_corr_x_y(numbers, highest_correlated)
    print('highest correlation: {0}'.format(corr))
    scatter_plot(summer, highest_correlated)

# correlation coefficient
# example
simple_list1 = [1, 2, 3]
simple_list2 = [4, 5, 6]

for x, y in zip(simple_list1, simple_list2):
    print(x, y)

# define a correlation function
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

def scatter_plot(x, y):
    import matplotlib.pyplot as plt
    plt.scatter(x, y)
    plt.show()


if __name__ == '__main__':
    simple_list1 = [1, 2, 3, 4.5]
    simple_list2 = [2, 4, 6, 8]
    corr_xy = find_corr_x_y(simple_list1, simple_list2)
    print('correlation between x and y: {0}'.format(corr_xy))

    # scatter plot for the data
    scatter_plot(simple_list1, simple_list2)

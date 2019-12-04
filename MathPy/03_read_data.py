# reading data from a text file
# find the sum of the numbers stored in a file
def sum_data(file_name):
    s = 0
    with open(file_name) as f:
        for line in f:
            s = s + float(line)
    print('sum of the numbers: {0}'.format(s))

if __name__ == '__main__':
    sum_data('mydata.txt')
    

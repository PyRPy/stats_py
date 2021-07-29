# iterators in python
# https://www.geeksforgeeks.org/iterators-in-python/

it = 'good'
it_obj = iter(it)

while True:
    try:
        item = next(it_obj)
        print(item)
    except StopIteration:
        break

# print out iteratros in steps
class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration

        self.x = x + 1
        return x

# test numbers
for i in Test(15):
    print(i)

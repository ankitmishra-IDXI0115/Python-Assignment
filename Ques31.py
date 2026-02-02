#Implement the higher order functions map(), filter() and reduce(). (They are built-in but writing them yourself may be a good exercise.)

def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result


def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


def my_reduce(func, iterable):
    iterator = iter(iterable)
    result = next(iterator)

    for item in iterator:
        result = func(result, item)

    return result

print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(my_map(lambda x: x * 2, [1, 2, 3]))


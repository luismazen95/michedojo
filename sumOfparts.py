import functools


def sum_of_parts(list):
    parts = []
    for i in range(len(lis)):
        parts.append((functools.reduce(lambda a, b: a+b, lis)))
        lis.pop(0)
    return(parts)


lis = [0, 1, 3, 6, 10]
print(sum_of_parts(lis))

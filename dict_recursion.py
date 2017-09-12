s = {'a': {'b': {'c': {'d': {'e': {'f': 1, 'g': 50, 'h': [1, 2, 4], 'i': 3, 'j': [7, 9, 6], 'k': [[('x', 'abc')], [('y', 'qwe')], [('z', 'zxc')]]}}}}}}
def get_dict(d):

    if all(not isinstance(b, dict) for a, b in d.items()):
        yield from d.items()

    else:
        new_d = list(d.items())
        

        yield new_d[0][0]
        yield from get_dict(new_d[0][-1])

print(list(get_dict(s)))

def find_maximum(val):
    maximum = val[0]
    final_list = []

    for i, a in enumerate(val):
        new_list = [a]
        for b in val[i+1:]:
            copy = new_list
            copy.append(b)
            if sum(copy) > maximum:
                new_list = copy

        final_list.append(new_list)

    return sorted(final_list, key=sum)[-1]


n = input()
data = [raw_input() for i in range(n)]

data = {i.split()[0]:map(int, i.split()[1:]) for i in data}



print data


for a, b in data.items():
    print a

    print find_maximum(b)

    print sum(b)

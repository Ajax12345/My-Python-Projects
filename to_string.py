import itertools
s = 123456

converter = {i:str(i) for i in range(10)}
heighest = 0

while True:
    if pow(10, heighest) < s:
        heighest += 1

    else:
        break



vals = [s%pow(10, i) for i in range(1, heighest+1)]

new_vals = list(itertools.chain(*[[vals[i], abs(vals[i]-vals[i+1])] for i in range(len(vals)-1)]))

while any(i > 9 for i in new_vals):
    new_vals = [i if i < 10 else i/10 if i%10 == 0 else None for i in new_vals]

final = ''.join(converter[i] for i in new_vals[::-1] if i is not None)

print final

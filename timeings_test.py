import time

def timeit(f):
    _c = time.time()
    _ = f()
    print(f'timeresults for {f.__name__}: {time.time()-_c}')

@timeit
def ajax1234():
    A, B = [1, 5, 2, 4, 3], [0, 2, 1]
    def results(a, b):
        _l = len(b)
        for c in range(len(a)-_l+1):
            _r = a[c:c+_l]
            new_r = [_r[i] for i in b]
            if all(new_r[i] < new_r[i+1] for i in range(len(new_r)-1)):
                yield _r
    return list(results(A, B))

@timeit
def OP():
    A = [1, 5, 2, 4, 3]
    B = [0, 2, 1]
    m = len(A)
    n = len(B)
    for i in range(m - n + 1):
        current_subarray = A[i:i + n]
        # we now do n - 1 comparaisons to check whether the subarray is correctly ordered.
        for B_index in range(n - 1):
            if current_subarray[B[B_index]] > current_subarray[B[B_index + 1]]:
                break
        else:
            print("Subarray found:", current_subarray)

'''
@timeit
def roadrunner():
    from scipy.stats import rankdata

    A = [1, 5, 2, 4, 3]
    B = [0, 2, 1]

    m = len(A)
    n = len(B)

    for i in range(m - n + 1):
        current_subarray = A[i:i + n]

        ranked_numbers = (rankdata(current_subarray).astype(int) - 1).tolist()
        if ranked_numbers == B:
            print("Subarray found:", current_subarray)

'''

#ajax1234()
#roadrunner()
#OP()
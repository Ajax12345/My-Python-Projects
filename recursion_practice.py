import copy

def permutations(l, n):
    permutation_list = []
    if n == 1:
        for i in l:
            permutation_list.append((i,))
        return permutation_list

    for i in l:
        print i
        #l = l.remove(i)
        new_l = l[:]
        #new_l = copy.deepcopy(l)
        new_l.remove(i)
        permutation = join(i, permutations(new_l, n-1))
        permutation_list.extend(permutation)

    return permutation_list

def join(item, list_of_tuples):
    return map(tuple, [[item]+list(i) for i in list_of_tuples])

new_list = permutations([1, 2, 3, 4], 3)
print new_list

def search(l, n):
    if len(l) == 0:
        return False




    else:
        if l[0] == n:
            return True
        else:
            new_l = l[1:]
            return search(new_l, n)


print search([1, 2, 34, 5], 7)

def factorial(n, i):
    if n == 0:
        return i

    else:

        new_n = n -1 #can't use n -= 1
        i *= n
        return factorial(new_n, i)

print factorial(5, 1)

def transverse(the_dict, start):

    if len(the_dict) > 1:
        return the_dict["interests"]

    else:
        new_dict = the_dict[start]
        new_start = new_dict.keys()[0]

        return transverse(new_dict, new_start)




d = {"james":{"info":{"age":17, "interests":["chess", "programming"]}}}

print transverse(d, "james")

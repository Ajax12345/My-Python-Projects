import string
n = 2
letters = string.ascii_lowercase
block1 = letters[:4]
block2 = letters[4:8]
print block1
print block2
matrix = [[1 if b == 0 and i == 0 or b == 2*n+1 and i == 2*n + 1 else 0 for b in range(2*n+2)] for i in range(2*n+2)]
count = 0
flag = False
for i, a in enumerate(matrix[1:-1]): #fix to account for the fact that we are starting at 2, not 0

    if i%2 == 0:
        matrix[i+1][count:count+4] = list(block1)


    else:
        matrix[i+1][count:count+4] = list(block2)


        count += 2

for i in matrix:
    print i

import enchant
from string import ascii_uppercase
message = 'L FDQQRW IRUHFDVW WR BRX WKH DFWLRQ RI UXVVLD LW LV D ULGGOH ZUDSSHG LQ D PBVWHUB LQVLGH DQ HQLJPD ZLQVWRQ FKXUFKLOO'

d = enchant.Dict("en_US")
for i in range(1, 26):
    letters = [k for k in ascii_uppercase]
    new_letters = []

    new_letters.extend(letters[i:])
    new_letters.extend(letters[:i])


    dct = {new_letters[b]:letters[b] for b in range(len(letters))}

    answer = []

    string = ''
    for c in message:
        if c != ' ':
            string += dct[c]

        else:
            answer.append(string)
            string = ''


    checker = [d.check(l) for l in answer]


    if all(checker):
        print ' '.join(answer)

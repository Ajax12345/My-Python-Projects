import string
import enchant
import random
#Vigenere cipher
def main():
    flag = False
    d = enchant.Dict("en_US")

    letters = [i for i in string.ascii_lowercase]
    my_first_dictionary = dictionary_one()
    my_second_dictionary = dictionary_two()

    message = "attack at dawn tomorrow "
    encrypted_message = encryptor(my_first_dictionary, my_second_dictionary, message)



    total_message = []
    final1 = {}
    final2 = {}
    for i in range(2, 15):
        new1 = []
        new1.extend(letters[i:])
        new1.extend(letters[:i])

        first_dict = {new1[i]:letters[i] for i in range(len(letters))}
        first_dict[" "] = " "
        for b in range(2, 15):
            new2 = []
            new2.extend(letters[b:])
            new2.extend(letters[:b])

            second_dict = {new2[i]:letters[i] for i in range(len(letters))}
            second_dict[" "] = " "
            string1 = ''
            for c in range(len(encrypted_message)):

                if c%2 != 0:
                    if encrypted_message[c] != ' ':
                        string1 += first_dict[encrypted_message[c]]

                    else:
                        #print string1
                        if d.check(string1):
                            total_message.append(string1)

                            string1 = ''


                else:
                    if encrypted_message[c] == ' ':

                        if d.check(string1):
                            #print string1
                            total_message.append(string1)

                            string1 = ""
                    else:

                        string1 += second_dict[encrypted_message[c]]


            if len(total_message) == len(encrypted_message.split()):
                for i in total_message:
                    print i,

                flag = True
            if not flag:
                continue
            else:
                break
        if not flag:
            continue

        else:
            break







def dictionary_one():
    letters = [i for i in string.ascii_lowercase]
    key = random.randint(2, 15)
    new_alphabet = []
    new_alphabet.extend(letters[key:])
    new_alphabet.extend(letters[:key])
    final_dict = {letters[i]:new_alphabet[i] for i in range(len(letters))}
    final_dict[" "] = " "
    return final_dict


def dictionary_two():
    letters = [i for i in string.ascii_lowercase]
    key = random.randint(2, 15)
    new_alphabet = []
    new_alphabet.extend(letters[key:])
    new_alphabet.extend(letters[:key])
    final_dict = {letters[i]:new_alphabet[i] for i in range(len(letters))}
    final_dict[" "] = " "
    return final_dict

def encryptor(dct1, dct2, message1):
    new_message = []
    for i in range(len(message1)):
        if i%2 == 0:
            new_message.append(dct2[message1[i]])

        else:
            new_message.append(dct1[message1[i]])

    return ''.join(new_message)


main()

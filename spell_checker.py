import re
import collections
import string
dictionary = [i.strip('\n') for i in open("the_file.txt")]

user_data = [i.strip('\n').split() for i in open("the_file1.txt")]
final_file = open("the_file1-changed.txt", 'w')

for line in user_data:
    new_line = []
    for word in line:
        upper_first = word[0].isupper()
        new_word = word
        trailing = ""
        new_word = re.findall("[a-zA-Z0-9]+", word.lower())[0]

        trailing = ''.join(i for i in word if i in string.punctuation)
        #print "len", len(word)-len(new_word)
        #trailing = word[-(len(word)-len(new_word)):]

        #print "trailing", trailing



        if new_word in dictionary or new_word.isdigit():
            new_line.append(new_word)

        else:
            #print "new_word", new_word
            options = []
            for correct_word in dictionary:
                #print "misspelled word", new_word
                #print "-------------------------"
                if len(correct_word) - len(new_word) <= 2:
                    for i in range(0, len(correct_word), 3): #was 3

                        if correct_word[len(correct_word)-i-3:len(correct_word)-i] == new_word[len(new_word)-i-3:len(new_word)-i]:
                            options.append(correct_word)

                        if correct_word[i:i+3] == new_word[i:i+3]:
                            options.append(correct_word)

            options = [i for i in options if len(i) - len(new_word) <= 2]
            better_options = [i for i in options if all(b in i for b in new_word)]
            final_options = [i for i in better_options if i[0] == new_word[0]]

            final_option = collections.Counter(final_options).most_common(5)[0][0]

            final_word = ""

            if upper_first:
                new_stuff = final_option[0].upper()+final_option[1:]+trailing
                final_word = new_stuff

            else:
                final_word = final_option+trailing







            new_line.append(final_word)

    final_file.write(' '.join(new_line)+"\n")


final_file.close()

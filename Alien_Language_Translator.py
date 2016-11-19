#James Petullo
final_message = []
message = input("Enter the message in Zorktronian, with no capitalization or puncuation: ") 
new_message = list(message)
for i in range(len(new_message)):

    if new_message[i] == 'e':
        new_message[i] = 'a'

    elif new_message[i] == 'i':

        new_message[i]= 'e'

    elif new_message[i] == 'o':

        new_message[i] = 'i'

    elif new_message[i] == 'u':

        new_message[i] = 'o'

    elif new_message[i] == 'a':

        new_message[i] = 'u'

second_list = ''.join(new_message)[::-1]
final_list = ' '.join(second_list.split()[::-1])
print("The message says: ", final_list)

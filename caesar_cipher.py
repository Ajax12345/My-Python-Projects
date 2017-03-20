import string

class Encriptor:
    def __init__(self, key, message):
        self.key = key
        self.message = message

    def scramble(self):
        self.the_alphabet = [i for i in string.ascii_lowercase]
        self.new_list = [0 for i in range(26)]
        for i in range(26):
            if i + self.key < 26:
                self.new_list[i+self.key] = self.the_alphabet[i]


            else:
                for i in range(self.key):
                    self.new_list[i] = self.the_alphabet[26-self.key:][i]

        self.new_alphabet = {}
        for i in range(26):
            self.new_alphabet[self.the_alphabet[i]] = self.new_list[i]

        self.scrambled_message = []
        for i in self.message:
            self.scrambled_message.append(self.new_alphabet[i])

        print ''.join(self.scrambled_message)


    def decrypter(self):
        self.the_alphabet = [i for i in string.ascii_lowercase]
        self.new_list = [0 for i in range(26)]
        for i in range(26):
            if i + self.key < 26:
                self.new_list[i+self.key] = self.the_alphabet[i]


            else:
                for i in range(self.key):
                    self.new_list[i] = self.the_alphabet[26-self.key:][i]

        self.new_alphabet = {}
        for i in range(26):
            self.new_alphabet[self.new_list[i]] = self.the_alphabet[i]

        self.scrambled_message = []
        for i in self.message:
            self.scrambled_message.append(self.new_alphabet[i])

        print ''.join(self.scrambled_message)

the_new_message = Encriptor(4, "attacktomorrow")

the_new_message.scramble()

import random
import csv
import itertools
import urllib
import re
import copy
import wiki
#TODO: may need longer list of nouns
class SpeechBot:
    def __init__(self, user_input):
        self.last_response = user_input
        self.stop_words = ["a", "the", "am", "an", "of", "as", "be"]
        self.total_stop_words = list(itertools.chain.from_iterable(list(csv.reader(open("stop-word-list.csv")))))
        self.nouns = self.get_nouns()
        self.adjectives = self.get_adjectives()
        self.verbs = self.get_verbs()
        self.pronouns = self.get_pronouns()

        self.adverbs = self.get_adverbs()
        self.personal_pronouns = self.get_personal_pronouns()
        #print "personal_pronouns", self.personal_pronouns
        self.query_words = ["what", "when", "where", "which", "who", "whom", "whose", "why", "did"]
        self.w = wiki.Wiki()


    def user_string(self):
        self.last_response = raw_input("What is it you have to say? ")

    def format_response(self):
        converter = {"nouns":self.nouns, "adjectives":self.adjectives, "verbs":self.verbs, "pronouns":self.pronouns, "adverbs":self.adverbs, "personal_pronouns":self.personal_pronouns}
        word_matching = {a:[i.lower() for i in self.last_response.split() if i.lower() in b] for a, b in converter.items()}
        new_dict = copy.deepcopy(word_matching)
        del new_dict["nouns"]
        word_matching["nouns"].extend([i.lower() for i in self.last_response.split() if i.lower() not in itertools.chain.from_iterable(new_dict.values())])
        word_matching["querys"] = [i.lower() for i in self.last_response.split() if i.lower() in self.query_words]

        final_nouns = list(set(i for i in word_matching["nouns"] if i not in itertools.chain.from_iterable([self.verbs, self.adjectives, self.query_words, self.adverbs, self.personal_pronouns, self.pronouns])))
        word_matching["nouns"] = final_nouns
        word_matching["personal_pronouns"] = [i for i in self.last_response.split() if i in self.personal_pronouns]
        word_matching["nouns"] = [i for i in word_matching["nouns"] if i.upper() not in word_matching["personal_pronouns"] or i.lower() not in word_matching["personal_pronouns"]]

        self.determine_response(word_matching)

    def determine_response(self, tree):
        #later, will have to add feature which checks database for previous user entry
        print tree
        #for each, certain keywords will be obtain that will work in each sense. 
        if tree["querys"] and not tree["personal_pronouns"] and tree["nouns"]:
            print "check internal files or wiki for answer"

        elif tree["querys"] and any("you" in i for i in tree["personal_pronouns"]):
            print "asking about computer"

        elif tree["querys"] and "I" in tree["personal_pronouns"]:
            print "asking about himself"


        else:
            if tree["nouns"] and any("you" in i for i in tree["personal_pronouns"]):
                print "refering to computer"


            elif tree["nouns"] and 'I' in tree["personal_pronouns"]:
                print "refering to speaker"

            elif tree["nouns"] and not tree["personal_pronouns"] and tree["pronouns"]:
                print "refering to himself"


            elif tree["nouns"] and not tree["personal_pronouns"]:
                print "purely declarative"

            else:
                print "not sure, tell me"







    def get_nouns(self):
        f = [i.strip('\n').split()[0] for i in open('nouns.txt')]
        return f

    def get_adjectives(self):
        f = [i.strip('\n').strip(" \t") for i in open('adjectives.txt') if len(i) != 1]
        return f

    def get_verbs(self):
        f = [i.strip('\n').split()[1:] for i in open("verbs.txt")]
        return list(itertools.chain.from_iterable(f))

    def get_pronouns(self):
        f = [i.strip('\n') for i in open('pronouns.txt')]

        new_f = [i for i in f if i and i != "\t" and not i.isupper()]
        new_f.append("I")
        #return new_f
        self.query_words = ["what", "when", "where", "which", "who", "whom", "whose", "why", "did"]
        return [i for i in new_f if i not in self.query_words]

    def get_adverbs(self):
        f = [i.strip('\n') for i in open('adverbs.txt')]
        f = [i[1:] if i.startswith('\t') else i for i in f]
        f = [i for i in f if len(i) > 1]
        return f

    def get_personal_pronouns(self):
        f = [i.strip('\n').split() for i in open('ppns.txt')]
        f = [i[-2:] for i in f if i]
        return list(itertools.chain.from_iterable(f))
s = SpeechBot("what are the yankees")

s.format_response()

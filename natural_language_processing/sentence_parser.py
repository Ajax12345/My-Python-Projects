import practice_file1
import urllib
import re
import string
import wiki
import collections

class Parser(practice_file1.SpeechBot):
    def __init__(self):
        practice_file1.SpeechBot.__init__(self, "dummy text")

        self.w = wiki.Wiki()
        self.nouns = self.get_nouns()
        self.adjectives = self.get_adjectives()
        self.verbs = self.get_verbs()
        self.adverbs = self.get_adverbs()
        self.pronouns = self.get_pronouns()
        self.personal_pronouns = self.get_personal_pronouns()
        self.converter = {"nouns":self.nouns, "adjectives":self.adjectives, "verbs":self.verbs, "pronouns":self.pronouns, "adverbs":self.adverbs, "personal_pronouns":self.personal_pronouns}
        self.scrape_main_wiki_page()


    def parse_sentence(self, wiki_data):
        pass

    def check_interal_files(self, full_key_word):
        pass






    def scrape_main_wiki_page(self):

        f = [i.strip('\n') for i in open('wiki_article_list.txt')]
        #print f
        full_results = collections.defaultdict(list)
        for url in f[:1]:

            full_web_data = self.w.get_article_info_by_url(url)
            new_data = [i.split() for i in full_web_data.split(".")]
            converter_1 = [{a:[i for i in b if i in map(str.lower, c)] for a, b in self.converter.items()} for c in new_data]

            print converter_1







p = Parser()

import urllib
import re
import collections
import itertools

class Wiki:
    def __init__(self, query):
        self.query = query
        self.topics = None
        self.disambiguation()
        self.seen_proper_href = False
        self.seen_proper_title = False

    def disambiguation(self):
        data_info = collections.namedtuple("data_info", "extension1 name name1")
        url = "https://en.wikipedia.org/wiki/{}_(disambiguation)".format(self.query)
        data = str(urllib.urlopen(url).read())
        final_data = re.findall('<a href="(.*?)" title="(.*?)">(.*?)</a>', data)[6:-48]
        topics = map(data_info._make, final_data)
        self.topics = topics
        return self.topics

    def get_article_info_by_url(self, article_title):
        url = "https://en.wikipedia.org{}".format(article_title)
        article_data = str(urllib.urlopen(url).read())

        new_data = re.findall("<p>(.*?)</p>", article_data)
        split_data = list(itertools.chain.from_iterable([i.split() for i in new_data]))
        new_stuff = [self.filter_html_and_non_alpha(i) if not all(b.isalpha() for b in i) else i for i in split_data]
        new_stuff = [i for i in new_stuff if i]
        return  ' '.join(new_stuff)


    def get_article_info_by_keyword(self, keyword):
        url = "https://en.wikipedia.org/wiki/{}".format(keyword)
        article_data = str(urllib.urlopen(url).read())

        new_data = re.findall("<p>(.*?)</p>", article_data)
        split_data = list(itertools.chain.from_iterable([i.split() for i in new_data]))
        new_stuff = [self.filter_html_and_non_alpha(i) if not all(b.isalpha() for b in i) else i for i in split_data]
        new_stuff = [i for i in new_stuff if i]
        return  ' '.join(new_stuff)


    def filter_html_and_non_alpha(self, word):
        new_word = re.sub("<(.*?)>", '', word)
        if "href" in new_word:
            if "wiki" in new_word:
                #new_word = re.findall("href='/wiki/'(.*?)", new_word)[0]
                new_word = new_word[new_word.index("/wiki/")+6:]
                self.seen_proper_href = True

            else:
                new_word = ""

        elif "title" in new_word:
            if self.seen_proper_href:
                new_word = ""

                self.seen_proper_href = False
                self.seen_proper_title = True

            else:
                pass

        elif "class=" in new_word:
            new_word = ""

        elif "id" in new_word:
            new_word = ""

        elif "(" in new_word or ")" in new_word:
            new_word = re.sub("\)*\(*", "", new_word)

        elif new_word == "<a":
            new_word = ""

        elif "style=" in new_word:
            new_word = ''

        elif new_word == "<abbr":
            new_word = ''



        else:
            if self.seen_proper_title:
                new_word = ""
                self.seen_proper_title = False

        return new_word







w = Wiki("calculus")
titles = w.disambiguation()
print titles[0].extension1
print w.get_article_info_by_url(titles[3].extension1)

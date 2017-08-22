import urllib
import re
import collections
import itertools
#TODO: build method to garner sources from wikepdia articles
class Wiki:
    def __init__(self):
        #self.query = query
        self.topics = None
        #self.disambiguation()
        self.seen_proper_href = False
        self.seen_proper_title = False

    def disambiguation(self, keyword):
        data_info = collections.namedtuple("data_info", "extension1 name name1")
        url = "https://en.wikipedia.org/wiki/{}_(disambiguation)".format(keyword)
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

    def get_article_sources(self, article_name, **kwargs):
        url = None
        if kwargs.get("full_url", False):
            url = "https://en.wikipedia.org{}".format(article_name)

        else:
            url = "https://en.wikipedia.org/wiki/{}".format(article_name)

        data = str(urllib.urlopen(url).read())
        s = '<li id="cite_note-(.*?)">(.*?)</li>'
        raw_sources = re.findall(s, data)
        final_dict = collections.defaultdict(dict)

        for number, raw_content in raw_sources:
            citation_type = re.findall('<cite class="(.*?)">', raw_content)
            final_dict[number]["citation_type"] = citation_type

            testing_r = '<cite class="(.*?)">(.*?)\.'
            author = re.findall(testing_r, raw_content)

            author = "None" if not author else author
            if author != "None":            #if "<a rel" not in re.findall(testing_r, raw_content)[-1] else "No Author"
                new_author = author[0][-1]

                if "<a rel" in new_author:
                    author = "None"

                else:
                    author = new_author
            final_dict[number]["Author"] = author

            web_url = re.findall('href="(.*?)">', raw_content)
            final_dict[number]["url"] = web_url[-1]
            full_description = re.findall('>"(.*?)"</a>', raw_content)
            final_dict[number]["description"] = full_description[0] if full_description else "None"

            retrieved = re.findall('Retrieved <span class="(.*?)">(.*?)</span>(.*?)</span>\.', raw_content)
            print "retrieved", "N/D" if not retrieved else ' '.join(retrieved[0][1:])
            final_dict[number]["retrieved"] = "N/D" if not retrieved else ' '.join(retrieved[0][1:])

        return final_dict











    def filter_html_and_non_alpha(self, word):
        new_word = re.sub("<(.*?)>", '', word)
        if "href" in new_word:
            if "/wiki/" in new_word:
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






w = Wiki()
#print w.get_article_info_by_keyword("python programming")
#titles = w.disambiguation()

#print [(i.extension1, i.name) for i in titles]
#w.get_article_sources("/wiki/Python_(programming_language)", full_url= True)
print w.get_article_info_by_keyword("Newsmax")
print w.get_article_sources("Newsmax")

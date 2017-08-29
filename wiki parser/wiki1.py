import urllib
import re
import collections
import itertools
import requests
from bs4 import BeautifulSoup as soup
import json


class Wiki:
    def __init__(self, query, **kwargs):
        self.query = query
        self.topics = None
        self.kwargs = kwargs
        self.url = "https://en.wikipedia.org{}".format(self.query) if self.kwargs.get("by_url", False) else "https://en.wikipedia.org/wiki/{}".format(self.query)
        self.header = self.get_header()

    def disambiguation(self):
        data_info = collections.namedtuple("data_info", "extension1 name name1")
        data = str(urllib.urlopen(self.url).read())
        final_data = re.findall('<a href="(.*?)" title="(.*?)">(.*?)</a>', data)[6:-48]
        topics = map(data_info._make, final_data)
        self.topics = topics
        return self.topics

    def get_header(self):
        r = '<h1 id="firstHeading" class="firstHeading" lang="en">(.*?)</h1>'
        return re.findall(r, str(urllib.urlopen(self.url).read()))[0]

    def get_article_data_between_keywords(self, article_data, *args):

        return [sentence for sentence in article_data.split(".") if any(i.lower() in sentence.lower() for i in args)]


    def get_article_info(self):


        req = requests.get(self.url)
        s = soup(req.text, 'lxml')#html.parser

        return [i.text for i in s.find_all("p")]


    def get_article_sources(self):


        data = str(urllib.urlopen(self.url).read())

        s = '<li id="cite_note-(.*?)">(.*?)</li>'
        raw_sources = re.findall(s, data)
        #final_dict = collections.defaultdict(dict)
        final_dict = []

        for number, raw_content in raw_sources:
            secondary_dict = {}

            citation_type = re.findall('<cite class="(.*?)">', raw_content)
            secondary_dict["citation_type"] = citation_type

            testing_r = '<cite class="(.*?)">(.*?)\.'
            author = re.findall(testing_r, raw_content)

            author = "None" if not author else author
            if author != "None":            #if "<a rel" not in re.findall(testing_r, raw_content)[-1] else "No Author"
                new_author = author[0][-1]

                if "<a rel" in new_author:
                    author = "None"

                else:
                    author = new_author
            secondary_dict["Author"] = author

            web_url = re.findall('href="(.*?)">', raw_content)
            secondary_dict["url"] = web_url[-1]
            full_description = re.findall('>"(.*?)"</a>', raw_content)
            secondary_dict["description"] = full_description[0] if full_description else "None"

            retrieved = re.findall('Retrieved <span class="(.*?)">(.*?)</span>(.*?)</span>\.', raw_content)
            #print "retrieved", "N/D" if not retrieved else ' '.join(retrieved[0][1:])
            secondary_dict["retrieved"] = "N/D" if not retrieved else ' '.join(retrieved[0][1:])
            final_dict.append(secondary_dict)
        return final_dict


    def get_bibliography(self):


        page_data = str(urllib.urlopen(self.url).read())
        if '<span class="mw-headline" id="Bibliography">Bibliography</span>' not in page_data:
            return None

        else:
            new_data = page_data.split("\n")
            #print [i for i, a in enumerate(page_data.split("\n")) if "Bibliography" in a]
            final_data = re.findall("<li>(.*?)</li>", '\n'.join(new_data[100:]))

            new_data = [{"full_title":i[:i.index("(<a href")] if "(<a href" in i else i, "ISBN":re.findall('<a href="/wiki/Special:BookSources/(.*?)"', i)[0] if re.findall('<a href="/wiki/Special:BookSources/(.*?)"', i) else "No Exterior ISBN"} for i in final_data]
            return new_data


    def get_external_links(self):

        page_data = str(urllib.urlopen(self.url).read())
        if '<span class="mw-headline" id="External_links">External links</span>' not in page_data:
            return None

        else:

            page_data = page_data.split("\n")
            indices = [i for i, a in enumerate(page_data) if '<span class="mw-headline" id="External_links">External links</span>' in a]
            final_data = '\n'.join(page_data[indices[-1]:])

            sites = re.findall('<a rel="nofollow" class="external text" href="(.*?)">(.*?)</a>', final_data)

            site = collections.namedtuple("site", "url name")
            new_sites = map(site._make, sites)
            return new_sites

    def get_contents(self):


        page_data = str(urllib.urlopen(self.url).read())
        r = '<span class="mw-headline" id="(.*?)">(.*?)</span>'
        contents = re.findall(r, page_data)
        return [i[-1] for i in contents]




    def get_info_box_data(self):

        data = str(urllib.urlopen(self.url).read()).split("\n")
        seen_header = False
        indices = []
        for i, a in enumerate(data):

            if '<table class="infobox' in a:
                seen_header = True
                indices.append(i)

            elif '</table>' in a and seen_header:
                indices.append(i)
                break

        a, b = indices
        infobox_data = data[a:b]
        
        for i in infobox_data:
            s = soup(i, "lxml")
            print s.getText()


            print "---------------"


        new_data = [soup(i, "lxml").getText() for i in infobox_data]
        print new_data
        '''

        for i in infobox_data:
            print i
            s = soup(i, "lxml")

            if s.find("th") is not None:
                print s.find("th").text

            if s.find("td") is not None:
                print s.find("td").text

            if s.find("<span") is not None:
                print s.find("<span").text


            print "--------------------------"

        new_data = []
        temp_list = []
        seen_tr = False
        for i in infobox_data:
            if i == "<tr>":
                seen_tr = True


            elif i == "</tr>":
                seen_tr = False
                new_data.append(temp_list)
                temp_list = []

            else:
                if seen_tr:
                    temp_list.append(i)


        new_filtered_code = [[re.findall('<a href="/wiki/(.*?)" title="(.*?)"', b) if "href" in b else re.findall('>(.*?)</|<span class="(.*?)"><i><b>\w+.&#\d+;(.*?)', b) for b in i] for i in new_data]


        new_filtered_code = [[list(set(b)) for b in i][0] for i in itertools.chain.from_iterable(new_filtered_code) if i]
        new_filtered_code = [[b for b in i if b] for i in new_filtered_code]
        new_filtered_code = [i[-1] for i in new_filtered_code if i]
        for i in new_filtered_code:
            print i
            print "-----------------"
        '''



#w = Wiki("/wiki/C%2B%2B", by_url=True)
#w = Wiki("/wiki/Python_(programming_language)", by_url = True)
#w = Wiki("/wiki/Python_(programming_language)", by_url=True)
w = Wiki("/wiki/W._E._B._Du_Bois", by_url=True)
w.get_info_box_data()

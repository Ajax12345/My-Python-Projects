import os
import re
from bs4 import BeautifulSoup as soup
import urllib
import csv
import itertools
import requests
import time
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
def get_question_list():

    data = str(urllib.urlopen('https://stackoverflow.com/questions/tagged/python').read())
    questions = re.findall('<a href="(.*?)" class="question-hyperlink">(.*?)</a>', data)

    return questions[0]

def strip_contents(url):
    comments = []


    page_data = str(urllib.urlopen("https://stackoverflow.com{}".format(url)).read())
    paragraphs = re.findall("<p>(.*?)</p>", page_data)[:-3]
    #print paragraphs
    #print paragraphs
    keywords = [i for i, a in enumerate(url) if a == "/"]
    question_name = url[keywords[-1]+1:]

    keywords = url[keywords[-1]+1:].split("-")

    #print keywords
    s = soup(page_data, "lxml")
    code = s.findAll('code')
    code_block = [i.text for i in code]

    stopwords = list(itertools.chain.from_iterable(list(csv.reader(open("stop-word-list.csv")))))
    stopwords = [i[1:] if i.startswith(" ") else i for i in stopwords]
    final_key_words = [i for i in keywords if i not in stopwords and i.lower() not in ["python", "error"] and not i.isdigit()]
    print "final_key_words", final_key_words


    if not code_block:
        new_keywords = "+".join(final_key_words[:4]) if len(final_key_words) > 6 else "+".join(final_key_words[:4])
        print "search keywords", new_keywords
        comments.append("please format your code attempts properly as demonstrated here: https://meta.stackexchange.com/questions/22186/how-do-i-format-my-code-blocks")

    else:

        new_keywords = "+".join(final_key_words[:4]) if len(final_key_words) > 6 else "+".join(final_key_words[:4])
        print "search keywords", new_keywords


        #browser = webdriver.Firefox(executable_path="/Users/davidpetullo/Downloads/geckodriver")
        #browser.get("https://stackoverflow.com/search?q={}".format(new_keywords))
        r = requests.get("https://stackoverflow.com/search?q={}".format(new_keywords))
        page_data = r.content
        s = '<a href="/questions/(.*?)/(.*?)" data-searchsession="/questions/(.*?)/(.*?)?s=(.*?)|(.*?)" title="(.*?)"> Q: (.*?) </a>'
        possibilites = re.findall(s, page_data)
        new_s = soup(page_data, "lxml")
        new_data = new_s.findAll("div", {"id": re.compile("question-summary-\d+")})
        new_i = new_s.findAll("div", {"class":"excerpt"})
        new_i = [i.text for i in new_i]
        id_and_summary = {a:b for a, b in zip(new_i, possibilites)}
        id_and_url = {i[0]:i[1] for i in possibilites}

        finall_answers = []
        for i in new_data:
            r = 'id="question-summary-(.*?)">'
            the_id = re.findall(r, str(i))[0]
            answers = re.findall("(.*?)answers", i.text)

            if answers and u'0' not in answers:
                finall_answers.append(the_id)


        #best_answers = [i for i in possibilites if i[0] in [a for a, b in finall_answers] and i[1] != question_name]
        best_answers = [i for i in finall_answers if id_and_url[i] != question_name]

        new_data = []

        for i in best_answers[:4]:


            new_url = "https://stackoverflow.com/questions/{}/{}".format(i, id_and_url[i])
            #print new_url

            data = str(urllib.urlopen(new_url).read())
            if re.findall('class="answer accepted-answer"', data):
                code_object = soup(data, "lxml")
                accepted_answer = code_object.findAll("div", {"class":"answer accepted-answer"})

                accepted_code = '\n'.join(map(str, accepted_answer))

                code_block = soup(accepted_code, "lxml").findAll("code")
                code_block = [i.text for i in code_block]
                final_code = '\n'.join(map(str, code_block))
                if re.findall("\w+", final_code):
                    print "here1"
                    new_data.append(final_code)
            else:
                code_object = soup(data, "lxml")
                accepted_answer = code_object.findAll("div", {"class":"answer"})
                '''
                new_accepted_anser = [i.text for i in accepted_answer]
                accepted_code = '\n'.join(new_accepted_anser)
                if re.findall("\w+", accepted_code):
                    print "here2"
                    new_data.append(accepted_code)
                '''
                accepted_code = '\n'.join(map(str, accepted_answer))

                code_block = soup(accepted_code, "lxml").findAll("code")
                code_block = [i.text for i in code_block]
                final_code = '\n'.join(map(str, code_block))
                if re.findall("\w+", final_code):
                    new_data.append(final_code)
                #print '\n'.join(code_block)
                #code = [soup(i, "lxml").findAll("pre", {"class":"lang-py prettyprint prettyprinted"}) for i in accepted_answer]


        if new_data:
            print "You can try this:"
            print "final_code", new_data[0]




            #pass
strip_contents("/46142487/python-flask-fast-cgi-on-apache-500-internal-server-error-premature-end-of")

'''
while True:
    #TODO: if title is longer than a certain number of characters, shorten
    #TODO: If no code is found in qestion, search for questions ([a-zA-Z]+\?)

    link, title = get_question_list()
    print title
    strip_contents(link)
    time.sleep(60)
    print "---------------------------"
'''

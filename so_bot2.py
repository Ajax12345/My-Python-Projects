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

def post_answer(payload):
    pass

def strip_contents(url):
    comments = []
    flag = False

    page_data = str(urllib.urlopen("https://stackoverflow.com{}".format(url)).read())

    paragraphs = re.findall("<p>(.*?)</p>", page_data)[:-3]
    print "paragraphs", paragraphs
    if "<code>" not in page_data:
        flag = True
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
    if not best_answers:
        if flag:
            post_commments(url, paragraphs)


    #for i in best_answers[:4]:
    for i in best_answers:


        new_url = "https://stackoverflow.com/questions/{}/{}".format(i, id_and_url[i])
        print "new_url", new_url

        data = str(urllib.urlopen(new_url).read())
        tags = re.findall('rel="tag">(.*?)</a>', data)
        print "tags", tags
        if any(i in tags for i in ['python', 'python-2.7', 'python-3.6']):
            if re.findall('class="answer accepted-answer"', data):

                code_object = soup(data, "lxml")
                accepted_answer = code_object.findAll("div", {"class":"answer accepted-answer"})

                accepted_code = '\n'.join(map(str, accepted_answer))

                code_block = soup(accepted_code, "lxml").findAll("code")
                explaination = soup(accepted_code, "lxml").findAll("p")
                code_block = [i.text for i in code_block]
                try:

                    final_code = '\n'.join(map(str, code_block))
                except:
                    pass
                else:
                    if re.findall("\w+", final_code):
                        print "here1"
                        new_data.append(final_code)
            else:
                code_object = soup(data, "lxml")
                accepted_answer = code_object.findAll("div", {"class":"answer"})

                accepted_code = '\n'.join(map(str, accepted_answer))

                code_block = soup(accepted_code, "lxml").findAll("code")
                code_block = [i.text for i in code_block]
                try:
                    final_code = '\n'.join(map(str, code_block))
                except:
                    pass
                else:
                    if re.findall("\w+", final_code):
                        print "here2"
                        new_data.append(final_code)
                #print '\n'.join(code_block)
                #code = [soup(i, "lxml").findAll("pre", {"class":"lang-py prettyprint prettyprinted"}) for i in accepted_answer]


    if new_data:
        print "new_data", new_data
        print "new_url", new_url
        print "You can try this:"
        print "final_code", ''.join(new_data)



last_seen = []
while True:
    #TODO: if title is longer than a certain number of characters, shorten
    #TODO: If no code is found in qestion, search for questions ([a-zA-Z]+\?)
    #IDEA: code from one answer, text from another
    #IDEA: scan answer and question text to see specifically what user is asking for
    #IDEA: potential answer "Here is an example based on what you want to accomplish. "

    link, title = get_question_list()
    if link not in last_seen:
        strip_contents(link)
        last_seen.append(link)

    print "---------------------------"

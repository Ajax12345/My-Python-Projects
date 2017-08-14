import urllib
import random
import re
import pickle
class Data_Gathering:
    def __init__(self):
        self.final_data = {}
        self.collect_data()

    def collect_data(self):
        for i in range(1, 53):
            url = "https://www.daddyleagues.com/maddenrating?page={}".format(i)
            data = str(urllib.urlopen(url).read())
            s = '<a href="https://www.daddyleagues.com/maddenrating/(.*?)" class="">(.*?)</a>'
            names =[i[-1] for i in re.findall(s, data)]
            specs = re.findall("<td>(.*?)</td>", data)
            #specs = [re.sub("\d")]'6&#039;0&#039;&#039;'
            specs = [re.sub("&#\d+;", '`', i) for i in specs]
            specs = [specs[i:i+20] for i in range(0, len(specs), 20)]
            specs = [[int(b) if all(c.isdigit() for c in b) else b for b in i] for i in specs]
            self.final_data.update({a:b for a, b in zip(names, specs)})

data = Data_Gathering()
pickle.dump(data.final_data, open('madden_player_stats.txt', 'a'))

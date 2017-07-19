
import urllib
import re

'''
output_file = open("so_users.txt", 'a')
connection = urllib.urlopen("https://stackexchange.com/leagues/1/week/stackoverflow/2017-07-16?sort=reputationchange&page=2")



filtered = re.findall("<a href=(.*?)</a>", str(connection.read()))

new_data = [re.findall("/users/(.*?)/(.*?)>(.*?)", i) for i in filtered]



new_data = list(set([(i[0][:-1][0], i[0][:-1][1][:-1]) for i in new_data if i]))
print new_data


for user_id, user_name in new_data:
    the_url = "https://stackoverflow.com/users/{}/{}".format(user_id, user_name)

    new_connection = urllib.urlopen(the_url)
    data = re.findall("<p>(.*?)</p>", str(new_connection.read()))
    emails = [re.findall('[a-zA-Z0-9.]{1,}@[a-zA-Z0-9.]{1,}.[a-z]{1,}', i) for i in data]
    final_data = [i[0] for i in emails if i]



    if len(final_data) > 0:

        output_file.write(user_id + " "+user_name + " "+final_data[0]+"\n")

output_file.close()
'''
'''
data = [i.strip('\n').split() for i in open('so_tags.txt').readlines()]

new_data = [i[0] for i in data if len(i) > 0]
output_file = open("so_users.txt", 'a')
for tag in new_data:
    the_new_url = "https://stackoverflow.com/tags/{}/topusers".format(tag)
    connection = urllib.urlopen(the_new_url)



    filtered = re.findall("<a href=(.*?)</a>", str(connection.read()))

    new_data = [re.findall("/users/(.*?)/(.*?)>(.*?)", i) for i in filtered]

    new_data = list(set([(i[0][:-1][0], i[0][:-1][1][:-1]) for i in new_data if i]))


    for user_id, user_name in new_data:
        the_url = "https://stackoverflow.com/users/{}/{}".format(user_id, user_name)

        new_connection = urllib.urlopen(the_url)
        data = re.findall("<p>(.*?)</p>", str(new_connection.read()))
        emails = [re.findall('[a-zA-Z0-9.]{1,}@[a-zA-Z0-9.]{1,}.[a-z]{1,}', i) for i in data]
        final_data = [i[0] for i in emails if i]



        if len(final_data) > 0:

            output_file.write(user_id + " "+user_name + " "+final_data[0]+"\n")



output_file.close()
'''

output_file = open("so_users.txt", 'a')

for page_number in range(2, 51):
    url = "https://stackexchange.com/leagues/1/week/stackoverflow/2017-07-16?sort=reputationchange&page={}".format(page_number)
    connection = urllib.urlopen(url)



    filtered = re.findall("<a href=(.*?)</a>", str(connection.read()))

    new_data = [re.findall("/users/(.*?)/(.*?)>(.*?)", i) for i in filtered]



    new_data = list(set([(i[0][:-1][0], i[0][:-1][1][:-1]) for i in new_data if i]))
    


    for user_id, user_name in new_data:
        the_url = "https://stackoverflow.com/users/{}/{}".format(user_id, user_name)

        new_connection = urllib.urlopen(the_url)
        data = re.findall("<p>(.*?)</p>", str(new_connection.read()))
        emails = [re.findall('[a-zA-Z0-9.]{1,}@[a-zA-Z0-9.]{1,}.[a-z]{1,}', i) for i in data]
        final_data = [i[0] for i in emails if i]



        if len(final_data) > 0:

            output_file.write(user_id + " "+user_name + " "+final_data[0]+"\n")

output_file.close()

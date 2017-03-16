import re
string = input()
pattern1 = re.compile(r'(\(\d\d\d\))(\d\d\d\-\d\d\d\d)')
pattern2 = re.compile(r'(\d\d\d\-\d\d\d\-\d\d\d)')
pattern3 = re.compile(r'(\(\d\d\d) (\d\d\d\-\d\d\d)')
pattern4 = re.compile(r'(\d\d\d\.\d\d\d\.\d\d\d)')
pattern5 = re.compile(r'(\d\d\d\d\d\d\d\d\d\d)')

number1 = pattern1.search(string)
number2 = pattern2.search(string)
number3 = pattern3.search(string)
number4 = pattern4.search(string)
number5 = pattern5.search(string)


answer_list = [number1, number2, number3, number4, number5]

none_count = 0

for i in answer_list:
    if i == None:
        none_count += 1

if none_count < 5:
    print("That is a valid phone number")

else:
    print("That is not a valid phone number")

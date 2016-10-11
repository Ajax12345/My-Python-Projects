import random
MC = ['Fred', 'Ian', 'Michael']
Thurifers = ['Fred', 'Ian', 'Michael', 'James', 'Steve', 'Alex', 'Edmund']
Acolytes =  ['James', 'Matt', 'Sam', 'Pete', 'Lucas', 'Steve', 'Alex']
BB = ['Ryan', 'Gary', 'Lucas', 'Pete']
CB = ['Joe', 'Ryan', 'Gary', 'Lucas']
backups = ['Karl', 'Thomas', 'Joseph', 'Hilaire', 'Edmund']
x = random.sample(MC, 1)
y = random.sample(Thurifers, 1)
z = random.sample(Acolytes, 1)
k = random.sample(Acolytes, 1)
w = random.sample(BB, 1)
t = random.sample(CB, 1)
l = random.sample(backups, 1)


print "For The 9:30 AM: \n"

if x == y:
    print "MC: ", "Fred", "\n"
    print "Th: ", y, "\n"
    print "AC1: ", z, "\n"
    print "AC2: ", l, "\n"
    print "BB: ", w, "\n"
    print "CB: ", t, "\n"

elif y == z:
    print "MC: ", x, "\n"
    print "Th: ", y, "\n"
    print "AC1: ", l, "\n"
    print "AC2: ", k, "\n"
    print "BB: ", w, "\n"
    print "CB: ", t, "\n"
   
   
elif z == w: #this is newline 1
    print "MC: ", x, "\n"
    print "Th: ", y, "\n"
    print "AC1: ", z, "\n"
    print "AC2: ", k, "\n"
    print "BB: ", l, "\n"
    print "CB: ", t, "\n"
   
elif k == w: #this is newline 2
    print "MC: ", x, "\n"
    print "Th: ", y, "\n"
    print "AC1: ", z, "\n"
    print "AC2: ", l, "\n"
    print "BB: ", w, "\n"
    print "CB: ", t, "\n"


elif z == t: #this is newline 3
    print "MC: ", x, "\n"
    print "Th: ", y, "\n"
    print "AC1: ", t, "\n"
    print "AC2: ", k, "\n"
    print "BB: ", w, "\n"
    print "CB: ", l, "\n"



elif z == k:
    print "MC: ", x, "\n"
    print "Th: ", y, "\n"
    print "AC1: ", w, "\n"
    print "AC2: ", k, "\n"
    print "BB: ", l, "\n"
    print "CB: ", t, "\n"

elif w == t:
    print "MC: ", x, "\n"
    print "Th: ", y, "\n"
    print "AC1: ", z, "\n"
    print "AC2: ", k, "\n"
    print "BB: ", w, "\n"
    print "CB: ", 'Karl', "\n"
  
else:
    print "MC: ", x, "\n"
    print "Th: ", y, "\n"
    print "AC1: ", z, "\n"
    print "AC2: ", k, "\n"
    print "BB: ", w, "\n"
    print "CB: ", t, "\n"
   
   
   
   
print "For the 11:00 AM: \n"

list = [MC, Thurifers, Acolytes, BB, CB, backups]
x = random.sample(list, 1)
for i in x:
    b = random.sample(i, 1)
    v = random.sample(i, 1)
    if b == v:
        print "AC1: James \n"
        print "AC2: Joe \n"
    else:
        print "AC1: ", b, "\n"
        print "AC1: ", v, "\n"

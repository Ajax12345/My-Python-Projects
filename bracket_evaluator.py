import re

s = "((2325235)()()()(134143asd){asd}[adsf]())"

s = re.sub("[a-zA-Z0-9]+", '', s)
converter1 = {"[":"]", "{":"}", "(":")", ")":"(", "]":"[", "}":"{"}
converter = {"[":"]", "{":"}", "(":")", "}":"{"}
final_groups = []
if all(s.count(converter1[i]) == s.count(i) for i in s):
    for i, a in enumerate(s):
        for b in s[i+1:]:
            if a in converter.keys():
                if b == converter[a]:
                    final_groups.append((a, b))

                    break

    print "yes" if all(b == converter[a] for a, b in final_groups) else "no"

else:
    print "no"

import re
s = input()
m = re.findall(r'[A|T|C|G]+', s)
maxlen = 0
for tmp in m:
    maxlen = max(len(tmp), maxlen)
print(maxlen)
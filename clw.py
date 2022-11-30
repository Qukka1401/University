'''import re
string = r"sd@.mail.ru sd.21@nf.ru sfg@hf/sg"
p = r"(?:([A-Za-z0-9\._-]+)@(?:[A-z0-9]+\.[A-z]+))"
match = re.findall(p, string)
print(match)'''

import re
import urllib.request
t = urllib.request.urlopen("http://www.summet.ru/dmsi/html/codesamples/addresses.html").read().decode()
p = r"((?:<li>)([^<]+)(?:<br)([^<]+)(?:<br)([^<]+)(?:<br)([^<]+))"
m = p.findall(t)

'''import re
string = r"sd@.mail.ru sd.21@nf.ru sfg@hf/sg"
p = r"(?:([A-Za-z0-9\._-]+)@(?:[A-z0-9]+\.[A-z]+))"
match = re.findall(p, string)
print(match)'''

import re
import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context
t = urllib.request.urlopen("http://www.summet.ru/dmsi/html/codesamples/addresses.html").read().decode()
p = r"((?:<li>)([^<]+)(?:<br)([^<]+)(?:<br)([^<]+)(?:<br)([^<]+))"
m = re.findall(p, t)
print(m)
import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
auto_nums = urllib.request.urlopen("https://moskva1.jsprav.ru/zamena-vozdushnogo-filtra/").read().decode()

pattern = r'(?:class="company-info-name-org">)([^<]*)(?:[\w|\W]+?data-rating=")([^"]+)(?:[\w|\W]*?"company-info-address-full company-info-text">\s*)([^\n]*)(?:[\w|\W]*?data-phone=")([^"]*)'
match = re.findall(pattern, auto_nums)
print(match)

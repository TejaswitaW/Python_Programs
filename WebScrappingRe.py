# read all mobile numbers from redbus.in
import re,urllib
from urllib.request import Request, urlopen
req = Request('http://zcoer.in/contact-us/')
text = urlopen(req).read()
#print(text)
numbers=re.findall('[7-9][\d]{9}',str(text),re.I)
#numbers=re.findall('[0-9]{3}[-][0-9]{8}',str(text),re.I)
for n in numbers:
    print(n)

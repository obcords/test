'''Run in terminal w Python3'''

import urllib.request
from bs4 import BeautifulSoup
f = urllib.request.urlopen("http://www.vetmed.ucdavis.edu/faculty/index.cfm")
s = f.read()
f.close()


soup = (BeautifulSoup(s, 'html.parser'))

inputTag = soup.findAll('option')

for i in inputTag:
    j = str(i)
    output = list()
    if 'Select' not in j and 'Faculty' not in j and 'Anatomy' not in j and 'Molecular' not in j and 'Medicine' not in j and 'Pathology' not in j and 'Population' not in j and 'Surgical' not in j and 'Office' not in j and 'California' not in j and 'Veterinary' not in j and 'Institute' not in j:
            x = str()
            n = 19
            print(j)
            while n <= 23:
                x += (j[n])
                n += 1
            output.append(x)
    print(output)






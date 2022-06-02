import urllib.request
import re
import csv

def addTrans():
    new_row = []
    with open('C:/Users/HP/Desktop/english11.csv') as f:
        for row in f:
            url = f'http://dict.youdao.com/search?q={row}'
            print(url)
            content = urllib.request.urlopen(url)
            pattern = re.compile("</h2.*?</ul>", re.DOTALL)
            # TODO: when the spell is wrong, give some prompt.
            result = pattern.search(content.read().decode()).group()
            pattern2 = re.compile('<li>.*?</li>')
            trans = [row]
            for meta in pattern2.findall(result):
                trans.append(meta.strip('<li>').strip('<li>'))
            new_row.append(trans)
        with open('C:/Users/HP/Desktop/english11.csv', 'w', newline='') as ff:
            writer = csv.writer(ff)
            i = 0
            for nrow in new_row:
                writer.writerow(nrow)
                i += 1
                print(f'{i} row has added.')
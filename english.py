import urllib.request
import re
import csv
import pandas as pd

class English:
    def addTrans(filename):
        file_format = filename.split('.')[1]
        if file_format == 'csv':
            pass
        elif file_format == 'xlsx':
            data = pd.read_excel(filename, index_col=0)
            filename = filename.split('.')[0] + '.csv'
            data.to_csv(filename, encoding='utf-8')

        new_row = []
        with open(filename, encoding='utf-8') as f:
            for row in f:
                print(row)
                start_url = f'http://dict.youdao.com/search?q={row}'
                url = start_url.replace(" ","")
                print(url)
                content = urllib.request.urlopen(url)
                pattern = re.compile("</h2.*?</ul>", re.DOTALL)
                # TODO: when the spell is wrong, give some prompt.
                result = pattern.search(content.read().decode()).group()
                pattern2 = re.compile('<li>.*?</li>')
                trans = [row]
                for meta in pattern2.findall(result):
                    meta = meta.strip('<li>').strip('</li>')
                    print(meta)
                    trans.append(meta)
                new_row.append(trans)
            with open('english.csv', 'w', encoding='utf-8-sig') as ff:
                writer = csv.writer(ff)

                i = 0
                for nrow in new_row:
                    # print(nrow)
                    writer.writerow(nrow)
                    i += 1
                    print(f'{i} row has added.')

    if __name__ == '__main__':
        addTrans('E.xlsx')
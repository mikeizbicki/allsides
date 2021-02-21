#/usr/bin/python3

import csv
import os
import lxml
import lxml.html

xpaths = {
    'name' : '//div[@class="latest_news_source"]/h1',
    'type' : '//div[@class="latest_news_source"]/p',
    'bias' : '//span[@class="first-span"]/strong',
    'url' : '//div[@class="dynamic-grid"]/a/@href',
    }
compiled_xpaths = { key : lxml.etree.XPath(xpath) for key,xpath in xpaths.items() }

with open('allsides.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(reversed(sorted(xpaths.keys()))))
    writer.writeheader()

    folder = 'www.allsides.com/news-source'
    for filename in os.listdir(folder):
        print("filename=",filename)
        path = os.path.join(folder, filename)
        with open(path) as fin:
            html = fin.read()
        doc = lxml.html.fromstring(html)
        row = {}
        for key,compiled_xpath in compiled_xpaths.items():
            elements = compiled_xpath(doc)
            if len(elements) == 0:
                result_str = ''
            else:
                element = elements[0]
                if type(element) is lxml.etree._ElementUnicodeResult:
                    result_str = str(element)
                elif type(element) is lxml.etree._Element:
                    result_str = element.text
                elif type(element) is lxml.html.HtmlElement:
                    result_str = element.text_content()
            row[key] = result_str
        writer.writerow(row)

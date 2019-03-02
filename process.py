import os
import functools
import codecs
'''
* [Initial page](index.md)
'''
 
DIR = "."

def compare(x, y):
    stat_x = os.stat(DIR + "/" + x)
    stat_y = os.stat(DIR + "/" + y)
    if stat_x.st_mtime < stat_y.st_mtime:
        return -1
    elif stat_x.st_mtime > stat_y.st_mtime:
        return 1
    else:
        return 0
 

def process():
    items = os.listdir(DIR)

    # FILTER
    items = [item for item in items if item.endswith("md")]
    
    print(items)
    items.sort(key=functools.cmp_to_key(compare))
    print(items)
    
    for item in items:
        filename = item
        # using the content before the .md
        title = item.split(".md")[0]

        with codecs.open('MARKDOWN_FORMAT_URLS.txt', 'a', "utf-8") as f:
            md_url = '* [' + title + ']' + '(' + filename + ')' + '\n'
            f.write(md_url + '\n')

process()
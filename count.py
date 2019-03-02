import zwc
import os
import functools
import codecs

DIR = "."
cnt_all = 0

def process():
    items = os.listdir(DIR)

    # FILTER
    items = [item for item in items if item.endswith("md")]
    
    
    for item in items:
        with codecs.open(item, 'r', "utf-8") as f:
            print(type(f))
            cnt = zwc.zwc(f.read())
            print(cnt)
            global cnt_all
            cnt_all += cnt


process()
print(cnt_all)
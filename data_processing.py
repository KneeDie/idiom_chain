import json

with open('data/idiom.json','r',encoding='utf-8') as file:
    data = json.load(file)

with open('idiom_list.txt','w',encoding='utf-8') as file:
    for item in data:
        idiom = item['word']
        file.write(idiom + '\n')

with open('data/word.json','r',encoding='utf-8') as file:
    data = json.load(file)

with open('word_list.txt','w',encoding='utf-8') as file:
    for item in data:
        idiom = item['word']
        file.write(idiom + '\n')

with open('SDpinyin_list.txt','w',encoding='utf-8') as file:
    for item in data:
        idiom = item['pinyin']
        file.write(idiom + '\n')

from xpinyin import Pinyin
with open('word_list.txt','r',encoding='utf-8') as file:
    lines = file.readlines()

pinyin_list = []
p = Pinyin()
for line in lines:
    pinyin = p.get_pinyin(line,'')
    pinyin_list.append(pinyin)

with open('WSDpinyin_list.txt','w',encoding='utf-8') as file:
    file.writelines(pinyin_list)
import random

print("欢迎来到成语接龙!")

#导入成语、汉字、拼音列表
with open("idiom_list.txt","r",encoding="utf-8") as file:
    idiom_list = file.read().splitlines()
with open("word_list.txt","r",encoding="utf-8") as file:
    word_list = file.read().splitlines()
with open("WSDpinyin_list.txt","r",encoding="utf-8") as file:
    pinyin_list = file.read().splitlines()
last_idiom = random.choice(idiom_list)
print(last_idiom)
#建立已经用过成语的列表
idioms_used = []

def check_chain(idiom1,idiom2):
    try:
        if pinyin_list[word_list.index(idiom1[0])] == pinyin_list[word_list.index(idiom2[-1])]:
            return True
        else:
            return False
    except:
        return False
#定义判断是否有可以继续的成语
def check_end(last_idiom):
    for idiom in idiom_list:
        if check_chain(idiom,last_idiom) and idiom not in idioms_used:
            return False
    return True

#主程序
while True:
    next_idiom = input("请接龙:")
    #判断是否接龙成功
    if next_idiom in idiom_list:
        #判断是否已经使用
        if next_idiom in idioms_used:
            print("这个成语已经用过了")
        else:
            #判断是否接龙成功
            if check_chain(next_idiom,last_idiom):
                print("接龙成功")
                idioms_used.append(next_idiom)
                last_idiom = next_idiom
                if check_end(last_idiom):
                    print("不可继续接龙,本局结束")
                    break
            else:
                print("接龙失败")
    else:
        print("咋回事，这不是成语吧!")
import re

def conversation(string):
    list_split = re.split('\s', string)
    final_list = []
    i = 0
    for words in list_split:
        word = re.sub('^[^a-zA-Z]|[^a-zA-Z]$','', words)
        if word == '':
            final_list.append(words)
        else:
            word_AKH = word[1:]+word[0]+'ay'
            final_list.append(list_split[i].replace(word, word_AKH))
        i += 1
    talk=''
    for words in final_list:
        talk+= words+' '
    return talk

string = 'hello , what is your name?'
print(conversation(string))

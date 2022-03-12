from re import findall,subn

file_name=input('file address?  ')

new_line_list=['{% load static %}',]
with open(file_name,'r') as f:
    line_list=f.readlines()
    for i in line_list:
        link_range=findall('<\s*(link.*|img.*|script.*)',i)
        if link_range :
            link_range=link_range[0][:link_range[0].find('>')]
            link_range=findall('src.*|href.*',link_range)
            if link_range:
                link_range=link_range[0][:link_range[0].find(' ')]
                link_range=findall('src\s*=[\"\']([a-z|A-Z|\|/|.|:|0-9|_|\-]*)|href\s*=[\"\']([a-z|A-Z|\|/|.|:|0-9|_|\-]*)',link_range)[0]
                for j in link_range:
                    if j:
                        new_line_list.append(subn(j,"{"+f"% static '{j}' %"+"}",i)[0])
        else:
            new_line_list.append(i)

string=''
for i in new_line_list:
    string+=i+'\n'

with open(file_name[:-5]+'_django_template.html','+a') as f:
    f.write(string)
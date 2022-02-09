test="aajjhhhheewwwwwwtt"

def language(value):
    lengh=len(value)/2
    if lengh==int(lengh):
        for i in range(0,int(lengh)):
            slice=value[(2*i):(2*i)+2]
            if slice[0]==slice[1]:continue
            else:return 'Nist'
        return 'Hast'
    else:
        return 'Nist'

print(language(test))
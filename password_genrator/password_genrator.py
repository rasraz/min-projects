import random

# This function is for random selection and using at least one of each in the password
def listing(list):
	arg=list[0:-1].split(',')
	item=random.choices(arg)[0]
	l=list.replace(item+',','')
	return item,l

# This function to create a password with a specified length includes uppercase and lowercase letters, characters and numbers
def password_genrator(number):
	lower=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p' 'q','r','s','t','u','v','w','x','y','z')
	capital=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
	character=('+', '×', '÷', '=', '/', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', ',', '?', '.', '~', '\\', '|', '<', '>', '{', '}', '[', ']', '-', '\'','\"')
	list='low,cap,char,num,'
	password=''
	for i in range(0,number+1):
    	# Random selection of lowercase letters,uppercase letters,characters and number
		randomin={
	'low': lower[random.randint(0,len(lower)-1)],
	'cap': capital[random.randint(0,len(capital)-1)],
	'char': character[random.randint(0,len(character)-1)],
	'num':random.randint(0,10),
		}
		item=listing(list)
		# Delete the once selected type
		list=item[1]
		# Retrieve selected shades after using each at least once
		if list=="":list='low,cap,char,num,'
		# Add the selected type to the password
		password+=str(randomin[item[0]])
	return password


status=True
while status:
	try:
		len_character=int(input('Number of characters (default:8): '))
		status=False
	except ValueError:
		print('please enter a number')
print(password_genrator(len_character))



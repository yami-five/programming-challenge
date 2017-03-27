from random import randint
import sys
vowels="aeiouy"
consonants="bcdfghjklmnprstwz"

def random_vowel():
    a=randint(0,len(vowels)-1)
    return vowels[a]
def random_consonant():
    a=randint(0,len(consonants)-1)
    return consonants[a]
#####################################################
def random_letter():
    a=randint(0,1)
    if a==0:
        return random_vowel()
    else:
        return random_consonant()
#####################################################
def first_syllable_2(name):
	name=random_letter()
	if name[0] not in vowels:
		name+=random_vowel()
	else:
		name+=random_consonant()
	return name
#####################################################
def first_syllable_3(name):
	name=random_letter()
	if name[0] in vowels:
		name+=random_consonant()
		return name
	else: 
		name+=random_letter()
	if name[0] and name[1] not in vowels:
		name+=random_vowel()
	return name
#####################################################
def first_syllable_4(name):
	name=random_letter()
	if name[0] in vowels:
		name+=random_consonant()
		return name
	else: 
		name+=random_letter()
	if name[0] and name[1] not in vowels:
		name+=random_letter()
	if len(name)==3:
		if name[0] and name[1] and name[2] not in vowels:
			name+=random_vowel()
	return name
#####################################################
def first_syllable(name,n):
	if n==2: name=first_syllable_2(name)
	elif n==3: name=first_syllable_3(name)
	elif n>=4: name=first_syllable_4(name)
	else: sys.exit("Wrong number")
	return name.capitalize()
#####################################################
name=""
n=int(input("Write a lenght of the name: "))
name=first_syllable(name, n)
if n>len(name):
 for x in range(len(name),n):
  if name[x-1] and name[x-2] in vowels:
   a=randint(0, len(consonants)-1)
   name+=consonants[a]
  elif name[x-1] and name[x-2] and name[x-3] in consonants:
   a=randint(0, len(vowels)-1)
   name+=vowels[a]
  else: name+=random_letter()
print(name)
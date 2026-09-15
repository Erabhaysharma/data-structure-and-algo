#first method in the string method is strip() method
#this methodd remove leading and trainling whitespace

str='   hello my name is abhay kumar sharma    '.strip()

#op-> hello my name is abhy kumar sharma

#strip method can also remove  any leading and trailing character
str3='##helo i am abhy##'
#op->hello i am abhay
str2=' #### hello i am abhay kumar###'.strip('#')
#op-> " ### hello iam abhay kumar"
#becuse the first chr is whitesoec srip only removce startingand ending character
str4='hello world its python'.strip("pydhn")
print(str4)
#op->'ello world its pytho'

#2nd method lstrip() metthod it remove leading whitesoce only

#e.g
str6='   hello world '.lstrip()
#op-> 'hello world '

# 3rd method is rstrip() method it remove only whitesoace from the right
str7='    helo world     '.rstrip()
#op->'   helo world'

#split metgod split()
str8=' hello!$am$abhay'.split('$',maxsplit=2) #maxplit tell how may split to be doen and fist argument tell from where to split
#if maxsplit=1 the op will be [' hello!', 'am$abhay']
print(str8)
#op->[' hello!', 'am', 'abhay']

str9='hello i am abhay kumar sharma'
print(str.split()) # here no argumnent passed it will bydefult split from -1 meand fromeach index
#op-> ['hello', 'my', 'name', 'is', 'abhay', 'kumar', 'sharma'] 
str10='heloo#iam#abhay#kumar'.rsplit('#',maxsplit=2)
#it split the string from the right side
print(str10)
#op->['heloo#iam', 'abhay', 'kumar']


#join() method
#syntex= separator.join(iterable)
list1=['h','e','l','l','o']
print(''.join(list1)) #op-hello

list2=['iam','abhay','kumar']
print(' '.join(list2)) #op-> iam abhay kumar

list3=['dog','always','bark']
print('_'.join(list3))
#op-> dog_always_bark
dict1={'name':'abhay','contry':'india'}
print(" and ".join(dict1))
#op->name and contry

str11='i love to drint oldmonk'
print(str11.replace('oldmonk','blender pride'))
#op->i love to drint blender pride

print(str11.replace(" ","_",2))
#here 2 is count vale that define  if multile the decide howm nay
#op->i_love_to drint oldmonk
str12='abhaykumarsharma'
print(str12.isalpha())

#op->true
str13='abhay abhay kuar'
print(str13.isalpha())
#op-> false becuse it contain whitespace tat is not alphabate

#isnumeric() return tru eid string contain numeric value only
str14='123444'
print(str14.isnumeric())
#op-true
#isalnum() is methpd return true is all characer are alphanumeri 
str15="abhay1245"
print(str15.isalnum()) #op-> true contain alphanumeric
str16="abhay 123"
print(str16.isalnum()) #op-> false it conat whitespace


#count() method find the no. of occrence of the substring in a given string

str17='i love frute frute amkes me happy'
print(str17.count('frute'))
#op->2
str18=' i love frute . Frute make me heldthy'
print(str18.count('Frute')) #op-.1

print(str18.count('frute',3,20)) #op-> 1

#find() this method thet find the fist occrece of the substring

str19='python is a beautyfull language'
print(str19.find("is"))

#rfind() method this metod return the last occurnece of teh substring

str20='ek sanay ki baat hai ek raja tha raja madharchod tha'
print(str20.rfind('raja'))

#index() method
#its is similar to find metod but the the substing not found then it return exception that
#is value error

print(str20.index('king')) 
#Op-> ValueError: substring not found

#rindex() this method similar to rfind () but it also raise value error 
#only diffrence between rfind and rindex

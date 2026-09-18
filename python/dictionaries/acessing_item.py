#there are multiple method to get value of dict
car_dict={'brand':'tata','model':'siara'}
#acessing value using key method

car_dict['brand']
#op=tata

#2nd get() method

#this is also a method of getting keys valye

car_dict.get('brand')

#3rd acessing keys using key() method
#it return  view object of containing keys as a list
#view object reflects any changes done to the dictonries

#syntex:
#dict_name.keys()

car_keys=car_dict.keys()
#op-.> list of the keys value
#adding new keys to dict
car_dict['fule_type']='cng'

#4th acessing values using value method

#it also return view object of valyes list

car_value=car_dict.values()

#5th  acessing items using item s methos

car_dict.items()
#it also return view object of items of list

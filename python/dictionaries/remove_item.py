#remove item using pop() method

car_dict={'brand':'tata','model':'siara'}

#remove item using pop methos
car_dict.pop('model')
#op=> item deletd from dict and return tahta item i.e siara
#remove item uisng popitem() method
#it remove the last inseted item of dict

car_dict.popitem()
#op=. remove last inseted item

#removing an item using del keyword
del car_dict['model']

#deveoing dict using del keyword
del car_dict

#empty a dict using clear() method

car_dict.clear()